'use client';

import React, { useState, useEffect } from 'react';
import { Circle, PlayCircle, PauseCircle, RotateCcw, BarChart } from 'lucide-react';
import { BarChart as RechartsBarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';

const initialStats = {
  completedPomodoros: 0,
  totalWorkTime: 0,
  totalBreakTime: 0,
  totalPauses: 0,
  pauseTime: 0,
  lastWeekPomodoros: Array(7).fill(0),
  dailyProgress: Array(7).fill(null).map((_, index) => ({
    day: ['Dom', 'Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb'][index],
    pomodoros: 0,
    workTime: 0,
    pauseTime: 0
  }))
};

const PomodoroApp = () => {
    const [timeLeft, setTimeLeft] = useState(25 * 60);
    const [isRunning, setIsRunning] = useState(false);
    const [mode, setMode] = useState('work');
    const [showStats, setShowStats] = useState(false);
    const [stats, setStats] = useState(initialStats);
    const [isLoading, setIsLoading] = useState(true);
    const [sessionStartTime, setSessionStartTime] = useState(null);
    const [lastPauseTime, setLastPauseTime] = useState(null);
  

  // Fetch stats on component mount
  useEffect(() => {
    fetchStats();
  }, []);

  useEffect(() => {
    let interval;
    if (isRunning && timeLeft > 0) {
      interval = setInterval(() => {
        setTimeLeft(time => time - 1);
      }, 1000);
    } else if (timeLeft === 0) {
      handleComplete();
    }
    return () => clearInterval(interval);
  }, [isRunning, timeLeft]);

  const formatTime = (seconds) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  };

  const toggleMode = () => {
    const newMode = mode === 'work' ? 'break' : 'work';
    setMode(newMode);
    setTimeLeft(newMode === 'work' ? 25 * 60 : 5 * 60);
    setIsRunning(false);
    setSessionStartTime(null);
    setLastPauseTime(null);
  };

  const resetTimer = () => {
    setTimeLeft(mode === 'work' ? 25 * 60 : 5 * 60);
    setIsRunning(false);
    setSessionStartTime(null);
    setLastPauseTime(null);
  };

  const fetchStats = async () => {
    try {
      setIsLoading(true);
      const response = await fetch('/api/stats');
      if (!response.ok) {
        throw new Error('Failed to fetch stats');
      }
      const data = await response.json();
      
      // Ensure dailyProgress has the correct day names
      const updatedData = {
        ...data,
        dailyProgress: data.dailyProgress.map((progress, index) => ({
          ...progress,
          day: ['Dom', 'Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb'][index] || progress.day
        }))
      };
      
      setStats(updatedData);
    } catch (error) {
      console.error('Error fetching stats:', error);
      setStats(initialStats);
    } finally {
      setIsLoading(false);
    }
  };

  const saveStats = async (newStats) => {
    try {
      const response = await fetch('/api/stats', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(newStats),
      });
      
      if (!response.ok) {
        throw new Error('Failed to save stats');
      }
      
      // Refresh stats after saving
      await fetchStats();
    } catch (error) {
      console.error('Error saving stats:', error);
    }
  };

  const handlePlayPause = () => {
    const now = Date.now();
    if (!isRunning) {
      setIsRunning(true);
      setSessionStartTime(now);
      if (lastPauseTime) {
        const pauseDuration = Math.floor((now - lastPauseTime) / 1000 / 60);
        updateStatsWithPause(pauseDuration);
      }
    } else {
      setIsRunning(false);
      setLastPauseTime(now);
      if (sessionStartTime) {
        const sessionDuration = Math.floor((now - sessionStartTime) / 1000 / 60);
        updateStatsWithSession(sessionDuration);
      }
    }
  };

  const updateStatsWithPause = (pauseDuration) => {
    const today = new Date().getDay();
    const newStats = {
      ...stats,
      totalPauses: stats.totalPauses + 1,
      pauseTime: stats.pauseTime + pauseDuration,
      dailyProgress: stats.dailyProgress.map((progress, index) => 
        index === today
          ? { ...progress, pauseTime: progress.pauseTime + pauseDuration }
          : progress
      )
    };
    
    setStats(newStats);
    saveStats(newStats);
  };

  const updateStatsWithSession = (sessionDuration) => {
    const today = new Date().getDay();
    const newStats = {
      ...stats,
      dailyProgress: stats.dailyProgress.map((progress, index) => 
        index === today
          ? {
              ...progress,
              workTime: mode === 'work' 
                ? progress.workTime + sessionDuration 
                : progress.workTime
            }
          : progress
      )
    };

    if (mode === 'work') {
      newStats.totalWorkTime += sessionDuration;
    } else {
      newStats.totalBreakTime += sessionDuration;
    }
    
    setStats(newStats);
    saveStats(newStats);
  };

  const handleComplete = () => {
    const today = new Date().getDay();
    const newStats = {
      ...stats,
      completedPomodoros: mode === 'work' ? stats.completedPomodoros + 1 : stats.completedPomodoros,
      totalWorkTime: mode === 'work' ? stats.totalWorkTime + 25 : stats.totalWorkTime,
      totalBreakTime: mode === 'break' ? stats.totalBreakTime + 5 : stats.totalBreakTime,
      lastWeekPomodoros: stats.lastWeekPomodoros.map((count, index) => 
        index === today && mode === 'work' ? count + 1 : count
      ),
      dailyProgress: stats.dailyProgress.map((progress, index) => 
        index === today && mode === 'work'
          ? {
              ...progress,
              pomodoros: progress.pomodoros + 1,
              workTime: progress.workTime + 25
            }
          : progress
      )
    };
    
    setStats(newStats);
    saveStats(newStats);
    toggleMode();
  };

  // Rest of the component remains the same...
  // (keeping the existing UI rendering code and other helper functions)


  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center justify-center p-4">
      <div className="bg-white rounded-xl shadow-lg p-8 max-w-4xl w-full">
        <div className="text-center mb-8">
          <h1 className="text-3xl font-bold text-gray-800 mb-2">Pomodoro Timer</h1>
          <div className="text-sm text-gray-600">
            {mode === 'work' ? 'Tiempo de trabajo' : 'Tiempo de descanso'}
          </div>
        </div>

        <div className="relative w-64 h-64 mx-auto mb-8">
          <Circle 
            className="w-full h-full text-gray-200" 
            strokeWidth={4}
          />
          <div className="absolute inset-0 flex items-center justify-center">
            <span className="text-4xl font-bold text-gray-800">
              {formatTime(timeLeft)}
            </span>
          </div>
        </div>

        <div className="flex justify-center space-x-4 mb-8">
          <button
            onClick={handlePlayPause}
            className="p-2 rounded-full hover:bg-gray-100 transition-colors"
          >
            {isRunning ? 
              <PauseCircle className="w-12 h-12 text-red-500" /> : 
              <PlayCircle className="w-12 h-12 text-green-500" />
            }
          </button>
          <button
            onClick={resetTimer}
            className="p-2 rounded-full hover:bg-gray-100 transition-colors"
          >
            <RotateCcw className="w-12 h-12 text-gray-500" />
          </button>
          <button
            onClick={() => setShowStats(!showStats)}
            className="p-2 rounded-full hover:bg-gray-100 transition-colors"
          >
            <BarChart className="w-12 h-12 text-blue-500" />
          </button>
        </div>

        {showStats && stats && (
          <div className="bg-gray-50 rounded-lg p-4">
            <h2 className="text-xl font-semibold mb-4">Estadísticas</h2>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div className="space-y-2">
                <div className="flex justify-between">
                  <span>Pomodoros completados:</span>
                  <span className="font-bold">{stats.completedPomodoros}</span>
                </div>
                <div className="flex justify-between">
                  <span>Tiempo total de trabajo:</span>
                  <span className="font-bold">{stats.totalWorkTime} min</span>
                </div>
                <div className="flex justify-between">
                  <span>Tiempo total de descanso:</span>
                  <span className="font-bold">{stats.totalBreakTime} min</span>
                </div>
                <div className="flex justify-between">
                  <span>Número de pausas:</span>
                  <span className="font-bold">{stats.totalPauses}</span>
                </div>
                <div className="flex justify-between">
                  <span>Tiempo total en pausas:</span>
                  <span className="font-bold">{stats.pauseTime} min</span>
                </div>
              </div>
              
              <div className="h-64">
                <ResponsiveContainer width="100%" height="100%">
                  <RechartsBarChart data={stats.dailyProgress} margin={{ top: 10, right: 30, left: 0, bottom: 0 }}>
                    <XAxis dataKey="day" />
                    <YAxis />
                    <Tooltip />
                    <Bar dataKey="pomodoros" fill="#3B82F6" name="Pomodoros" />
                    <Bar dataKey="workTime" fill="#10B981" name="Tiempo de trabajo" />
                    <Bar dataKey="pauseTime" fill="#EF4444" name="Tiempo en pausa" />
                  </RechartsBarChart>
                </ResponsiveContainer>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default PomodoroApp;
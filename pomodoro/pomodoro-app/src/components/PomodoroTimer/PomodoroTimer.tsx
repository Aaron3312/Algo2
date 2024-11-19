import { useState, useEffect } from 'react';
import { TimerDisplay } from './TimerDisplay';
import { TimerControls } from './TimerControls';
import { StatsDisplay } from './StatsDisplay';
import { useStats } from './hooks/useStats';
import { useTimer } from './hooks/useTimer';
import { getDayName } from './utils';

const WORK_TIME = 25;
const BREAK_TIME = 5;
const AUTOSAVE_INTERVAL = 1000 * 60; // Autoguardado cada 10 seg

const initialStats = {
  completedPomodoros: 0,
  totalWorkTime: 0,
  totalBreakTime: 0,
  totalPauses: 0,
  pauseTime: 0,
  lastWeekPomodoros: Array(7).fill(0),
  dailyProgress: Array(7).fill(null).map((_, index) => ({
    day: getDayName(index),
    pomodoros: 0,
    workTime: 0,
    pauseTime: 0
  })),
  lastSaved: Date.now()
};

const PomodoroTimer = () => {
  const [mode, setMode] = useState<'work' | 'break'>('work');
  const [showStats, setShowStats] = useState(false);
  const { stats, setStats, saveStats } = useStats(initialStats);
  const [currentDuration, setCurrentDuration] = useState(WORK_TIME * 60);
  const [lastPauseStartTime, setLastPauseStartTime] = useState<number | null>(null);
  const [sessionStartTime, setSessionStartTime] = useState<number | null>(null);
  // Añadimos un estado local para tracking del timer
  const [timerRunning, setTimerRunning] = useState(false);
  const [pauseCount, setPauseCount] = useState(0); // New state for tracking pauses in current session


  // Función para calcular el tiempo acumulado en la sesión actual
  const calculateCurrentSessionTime = () => {
    if (!sessionStartTime || !timerRunning) return 0;
    return Math.floor((Date.now() - sessionStartTime) / 60000);
  };

  const updateStats = (timeElapsed: number, isWorkMode: boolean, pauseDuration: number = 0) => {
    const today = new Date().getDay();
    const currentSessionTime = calculateCurrentSessionTime();
    console.log('currentSessionTime', currentSessionTime);

    // Calculate new pause-related stats
    const newTotalPauses = stats.totalPauses + (pauseDuration > 0 ? 1 : 0);
    //pause duration to 2 decimal places
    const newPauseTime = stats.pauseTime + Math.round(pauseDuration * 100) / 100;


    const newStats = {
      ...stats,
      completedPomodoros: isWorkMode ? stats.completedPomodoros + 1 : stats.completedPomodoros,
      totalWorkTime: isWorkMode ? stats.totalWorkTime + timeElapsed : stats.totalWorkTime,
      totalBreakTime: !isWorkMode ? stats.totalBreakTime + timeElapsed : stats.totalBreakTime,
      totalPauses: newTotalPauses,
      pauseTime: newPauseTime,
      lastWeekPomodoros: stats.lastWeekPomodoros.map((count, index) => 
        index === today && isWorkMode ? count + 1 : count
      ),
      dailyProgress: stats.dailyProgress.map((progress, index) => 
        index === today
          ? {
              ...progress,
              pomodoros: isWorkMode ? progress.pomodoros + 1 : progress.pomodoros,
              workTime: isWorkMode ? progress.workTime + timeElapsed : progress.workTime,
              pauseTime: progress.pauseTime + pauseDuration
            }
          : progress
      ),
      lastSaved: Date.now()
    };
    
    setStats(newStats);
    saveStats(newStats);
  };

  // Autoguardado periódico
  useEffect(() => {
    let autoSaveInterval: ReturnType<typeof setInterval>;
  
    if (timerRunning) {
      autoSaveInterval = setInterval(() => {
        const currentTime = Date.now();
        const timeElapsed = sessionStartTime ? Math.floor((currentTime - sessionStartTime) / 60000) : 0;
        if (timeElapsed > 0) {
          const newStats = {
            ...stats,
            totalWorkTime: mode === 'work' ? stats.totalWorkTime + timeElapsed : stats.totalWorkTime,
            totalBreakTime: mode === 'break' ? stats.totalBreakTime + timeElapsed : stats.totalBreakTime,
            lastSaved: currentTime,
          };
          setStats(newStats); // Actualiza el estado local
          saveStats(newStats); // Persistencia (asume que es una función asincrónica o síncrona)
          setSessionStartTime(currentTime); // Reinicia el tiempo
        }
      }, AUTOSAVE_INTERVAL);
    }
  
    return () => {
      clearInterval(autoSaveInterval); // Limpia el intervalo al desmontar o cuando cambien las dependencias
    };
  }, [stats, timerRunning, mode, sessionStartTime, saveStats]);

  const handleComplete = () => {
    const timeElapsed = mode === 'work' ? WORK_TIME : BREAK_TIME;
    updateStats(timeElapsed, mode === 'work');
    toggleMode();
  };

  const {
    timeLeft,
    isRunning,
    handlePlayPause: originalHandlePlayPause,
    reset,
    setTimeLeft
  } = useTimer(currentDuration, handleComplete);

  // Efecto para sincronizar el estado local con el estado del timer
  useEffect(() => {
    setTimerRunning(isRunning);
  }, [isRunning]);

  const handlePlayPause = () => {
    const now = Date.now();
    
    if (timerRunning) {
      setLastPauseStartTime(now);
      setSessionStartTime(null);
      setPauseCount(prev => prev + 1); // Increment pause count when pausing
      console.log('pauseCount', pauseCount);
    } else {
      if (lastPauseStartTime) {
        const pauseDuration = (now - lastPauseStartTime) / 60000;
        console.log('pauseDuration', pauseDuration);
        //time elapsed in minutes 

        
        updateStats(0, 0 , pauseDuration);
      }
      setLastPauseStartTime(null);
      setSessionStartTime(now);
    }
    
    originalHandlePlayPause();
  };

  useEffect(() => {
    const duration = mode === 'work' ? WORK_TIME * 60 : BREAK_TIME * 60;
    setCurrentDuration(duration);
    setTimeLeft(duration);
  }, [mode, setTimeLeft]);

  const toggleMode = () => {
    const newMode = mode === 'work' ? 'break' : 'work';
    setMode(newMode);
    setLastPauseStartTime(null);
    setSessionStartTime(null);
  };

  const handleSkip = () => {
    const isWorkMode = mode === 'work';
    const totalTime = isWorkMode ? WORK_TIME : BREAK_TIME;

    if (lastPauseStartTime) {
      const pauseDuration = Math.floor((Date.now() - lastPauseStartTime) / 60000);
      if (pauseDuration > 0) {
        updateStats(0, isWorkMode, pauseDuration);
      }
      setLastPauseStartTime(null);
    }
    
    if (timerRunning) {
      originalHandlePlayPause();
    }
    
    updateStats(totalTime, isWorkMode);
    toggleMode();
  };

  const handleReset = () => {
    if (lastPauseStartTime) {
      const pauseDuration = Math.floor((Date.now() - lastPauseStartTime) / 60000);
      if (pauseDuration > 0) {
        updateStats(0, mode === 'work', pauseDuration);
      }
      setLastPauseStartTime(null);
    }
    setSessionStartTime(null);
    reset();
  };

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center justify-center p-2 sm:p-4">
      <div className="bg-white rounded-lg sm:rounded-xl shadow-md sm:shadow-lg p-4 sm:p-6 md:p-8 w-full max-w-sm sm:max-w-md md:max-w-lg lg:max-w-4xl mx-auto">
        <div className="flex flex-col space-y-4">
          <TimerDisplay 
            timeLeft={timeLeft}
            mode={mode}
            className="text-4xl sm:text-5xl md:text-6xl"
          />
          
          <div className="flex items-center space-x-2">
            <div className="flex-1">
              <TimerControls 
                isRunning={timerRunning}
                onPlayPause={handlePlayPause}
                onReset={handleReset}
                onToggleStats={() => setShowStats(!showStats)}
                onSkipStats={handleSkip}
              />
            </div>
          </div>

          {showStats && (
            <div className="mt-4 sm:mt-6">
              <StatsDisplay 
                stats={stats}
                className="text-sm sm:text-base space-y-2 sm:space-y-4"
              />
              <div className="text-xs text-gray-500 mt-2">
                Último guardado: {new Date(stats.lastSaved).toLocaleTimeString()}
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default PomodoroTimer;
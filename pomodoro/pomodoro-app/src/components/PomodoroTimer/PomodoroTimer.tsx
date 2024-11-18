import { useState } from 'react';
import { TimerDisplay } from './TimerDisplay';
import { TimerControls } from './TimerControls';
import { StatsDisplay } from './StatsDisplay';
import { useStats } from './hooks/useStats';
import { useTimer } from './hooks/useTimer';
import { getDayName } from './utils';

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
  }))
};

const PomodoroTimer = () => {
  const [mode, setMode] = useState<'work' | 'break'>('work');
  const [showStats, setShowStats] = useState(false);
  const { stats, setStats, saveStats } = useStats(initialStats);
  
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

  const {
    timeLeft,
    isRunning,
    sessionStartTime,
    lastPauseTime,
    handlePlayPause,
    reset,
  } = useTimer(mode === 'work' ? 25 * 60 : 5 * 60, handleComplete);

  const toggleMode = () => {
    const newMode = mode === 'work' ? 'break' : 'work';
    setMode(newMode);
    reset();
  };

  const handleSkip = () => {
    if (isRunning) {
      handlePlayPause();
    }
    const timeElapsed = mode === 'work' ? 25 - Math.ceil(timeLeft / 60) : 5 - Math.ceil(timeLeft / 60);
    const today = new Date().getDay();
    
    const newStats = {
      ...stats,
      completedPomodoros: mode === 'work' ? stats.completedPomodoros + 1 : stats.completedPomodoros,
      totalWorkTime: mode === 'work' ? stats.totalWorkTime + timeElapsed : stats.totalWorkTime,
      totalBreakTime: mode === 'break' ? stats.totalBreakTime + timeElapsed : stats.totalBreakTime,
      lastWeekPomodoros: stats.lastWeekPomodoros.map((count, index) => 
        index === today && mode === 'work' ? count + 1 : count
      ),
      dailyProgress: stats.dailyProgress.map((progress, index) => 
        index === today && mode === 'work'
          ? {
              ...progress,
              pomodoros: progress.pomodoros + 1,
              workTime: progress.workTime + timeElapsed
            }
          : progress
      )
    };
    
    setStats(newStats);
    saveStats(newStats);
    toggleMode();
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
                isRunning={isRunning}
                onPlayPause={handlePlayPause}
                onReset={reset}
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
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default PomodoroTimer;
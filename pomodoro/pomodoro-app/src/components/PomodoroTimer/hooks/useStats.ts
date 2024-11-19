// Types
interface DailyProgress {
  day: string;
  completed: number;
  interrupted: number;
}

interface PomodoroStats {
  totalPomodoros: number;
  totalTime: number;
  dailyStreak: number;
  dailyProgress: DailyProgress[];
  longestStreak: number;
}

import { useState, useEffect } from 'react';
import { getDayName } from '../utils';

export const useStats = (initialStats: PomodoroStats) => {
  const [stats, setStats] = useState<PomodoroStats>(initialStats);
  const [isLoading, setIsLoading] = useState(true);

  const fetchStats = async () => {
    try {
      setIsLoading(true);
      const response = await fetch('/api/stats');
      if (!response.ok) {
        throw new Error('Failed to fetch stats');
      }
      const data = await response.json();
      
      const updatedData: PomodoroStats = {
        ...data,
        dailyProgress: data.dailyProgress.map((progress: DailyProgress, index: number) => ({
          completed: progress.completed || 0,
          interrupted: progress.interrupted || 0,
          day: getDayName(index)
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

  const saveStats = async (newStats: PomodoroStats) => {
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
      
      await fetchStats();
    } catch (error) {
      console.error('Error saving stats:', error);
    }
  };

  useEffect(() => {
    fetchStats();
  }, []);

  return { stats, setStats, isLoading, saveStats };
};
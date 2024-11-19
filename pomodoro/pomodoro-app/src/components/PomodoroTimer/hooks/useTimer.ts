import { useState, useEffect } from 'react';

export const useTimer = (initialTime: number, onComplete: () => void) => {
  const [timeLeft, setTimeLeft] = useState(initialTime);
  const [isRunning, setIsRunning] = useState(false);
  const [sessionStartTime, setSessionStartTime] = useState<number | null>(null);
  const [lastPauseTime, setLastPauseTime] = useState<number | null>(null);

  // Update timeLeft when initialTime changes
  useEffect(() => {
    setTimeLeft(initialTime);
  }, [initialTime]);

  useEffect(() => {
    let interval: NodeJS.Timeout;
    
    if (isRunning && timeLeft > 0) {
      interval = setInterval(() => {
        setTimeLeft(time => {
          if (time <= 1) {
            setIsRunning(false);
            onComplete();
            return 0;
          }
          return time - 1;
        });
      }, 1000);
    }
    
    return () => clearInterval(interval);
  }, [isRunning, timeLeft, onComplete]);

  const handlePlayPause = () => {
    const now = Date.now();
    if (!isRunning) {
      setIsRunning(true);
      setSessionStartTime(now);
    } else {
      setIsRunning(false);
      setLastPauseTime(now);
    }
  };

  const reset = () => {
    setTimeLeft(initialTime);
    setIsRunning(false);
    setSessionStartTime(null);
    setLastPauseTime(null);
  };

  return {
    timeLeft,
    isRunning,
    sessionStartTime,
    lastPauseTime,
    handlePlayPause,
    reset,
    setTimeLeft
  };
};
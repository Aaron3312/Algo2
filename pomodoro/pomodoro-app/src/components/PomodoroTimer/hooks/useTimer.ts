import { useState, useEffect } from 'react';

export const useTimer = (initialTime: number, onComplete: () => void) => {
  const [timeLeft, setTimeLeft] = useState(initialTime);
  const [isRunning, setIsRunning] = useState(false);
  const [sessionStartTime, setSessionStartTime] = useState<number | null>(null);
  const [lastPauseTime, setLastPauseTime] = useState<number | null>(null);

  useEffect(() => {
    let interval: NodeJS.Timeout;
    if (isRunning && timeLeft > 0) {
      interval = setInterval(() => {
        setTimeLeft(time => time - 1);
      }, 1000);
    } else if (timeLeft === 0) {
      onComplete();
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
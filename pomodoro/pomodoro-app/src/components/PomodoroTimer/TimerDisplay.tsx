// src/components/PomodoroTimer/TimerDisplay.tsx
import React from 'react';
import { Circle } from 'lucide-react';
import { formatTime } from './utils';

type TimerDisplayProps = {
  timeLeft: number;
  mode: 'work' | 'break';
};

export const TimerDisplay: React.FC<TimerDisplayProps> = ({ timeLeft, mode }) => {
  return (
    <>
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
    </>
  );
};
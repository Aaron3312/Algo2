import React from 'react';
import { PlayCircle, PauseCircle, RotateCcw, BarChart, SkipForward } from 'lucide-react';


type TimerControlsProps = {
  isRunning: boolean;
  onPlayPause: () => void;
  onReset: () => void;
  onToggleStats: () => void;
  onSkipStats: () => void;
};

export const TimerControls: React.FC<TimerControlsProps> = ({ 
  isRunning, 
  onPlayPause, 
  onReset, 
  onToggleStats,
  onSkipStats
}) => {
  return (
    <div className="flex justify-center space-x-4 mb-8">
      <button
        onClick={onPlayPause}
        className="p-2 rounded-full hover:bg-gray-100 transition-colors"
      >
        {isRunning ? 
          <PauseCircle className="w-12 h-12 text-red-500" /> : 
          <PlayCircle className="w-12 h-12 text-green-500" />
        }
      </button>
      <button
        onClick={onReset}
        className="p-2 rounded-full hover:bg-gray-100 transition-colors"
      >
        <RotateCcw className="w-12 h-12 text-gray-500" />
      </button>
      <button
        onClick={onToggleStats}
        className="p-2 rounded-full hover:bg-gray-100 transition-colors"
      >
        <BarChart className="w-12 h-12 text-blue-500" />
      </button>
      <button
        onClick={onSkipStats}
        className="p-2 rounded-full hover:bg-gray-100 transition-colors"
      >
         <SkipForward className="w-6 h-6" />
      </button>
    </div>
  );
};


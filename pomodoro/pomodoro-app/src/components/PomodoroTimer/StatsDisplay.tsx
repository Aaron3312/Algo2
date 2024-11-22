import React from 'react';
import { BarChart as RechartsBarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';
import { PomodoroStats } from './types';

type StatsDisplayProps = {
  stats: PomodoroStats;
};

const StatItem = ({ label, value }: { label: string; value: string | number }) => (
  <div className="flex justify-between">
    <span>{label}:</span>
    <span className="font-bold">{value}</span>
  </div>
);

export const StatsDisplay: React.FC<StatsDisplayProps> = ({ stats }) => {
  return (
    <div className="bg-gray-50 rounded-lg p-4">
      <h2 className="text-xl font-semibold mb-4">Estadísticas</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div className="space-y-2">
          <StatItem label="Pomodoros completados" value={stats.completedPomodoros} />
          <StatItem label="Tiempo total de trabajo" value={`${stats.totalWorkTime} min`} />
          <StatItem label="Tiempo total de descanso" value={`${stats.totalBreakTime} min`} />
          <StatItem label="Número de pausas" value={stats.totalPauses} />
          <StatItem label="Tiempo total en pausas" value={`${stats.pauseTime} min`} />
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
  );
};
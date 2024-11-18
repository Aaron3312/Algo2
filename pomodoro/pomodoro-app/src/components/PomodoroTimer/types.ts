export type PomodoroStats = {
  completedPomodoros: number;
  totalWorkTime: number;
  totalBreakTime: number;
  totalPauses: number;
  pauseTime: number;
  lastWeekPomodoros: number[];
  dailyProgress: {
    day: string;
    pomodoros: number;
    workTime: number;
    pauseTime: number;
  }[];
};
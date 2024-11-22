// app/api/stats/route.ts
import { NextResponse } from 'next/server';
import { promises as fs } from 'fs';
import path from 'path';

interface DailyProgress {
  day: string;
  pomodoros: number;
  workTime: number;
  pauseTime: number;
}

interface PomodoroStats {
  completedPomodoros: number;
  totalWorkTime: number;
  totalBreakTime: number;
  totalPauses: number;
  pauseTime: number;
  lastWeekPomodoros: number[];
  dailyProgress: DailyProgress[];
}

const defaultStats: PomodoroStats = {
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

const DATA_DIR = path.join(process.cwd(), 'data');
const STATS_FILE = path.join(DATA_DIR, 'stats.json');

async function ensureDataDirectory() {
  try {
    await fs.access(DATA_DIR);
  } catch {
    await fs.mkdir(DATA_DIR, { recursive: true });
  }
}

async function ensureStatsFile() {
  try {
    await fs.access(STATS_FILE);
  } catch {
    await fs.writeFile(STATS_FILE, JSON.stringify(defaultStats, null, 2));
  }
}

export async function GET() {
  try {
    await ensureDataDirectory();
    await ensureStatsFile();

    const fileContents = await fs.readFile(STATS_FILE, 'utf8');
    const stats = JSON.parse(fileContents);
    
    // Ensure all required properties exist
    const validatedStats = {
      ...defaultStats,
      ...stats,
      dailyProgress: Array(7).fill(null).map((_, index) => ({
        ...defaultStats.dailyProgress[index],
        ...(stats.dailyProgress?.[index] || {})
      }))
    };
    
    return NextResponse.json(validatedStats);
  } catch (error) {
    console.error('Error reading stats:', error);
    return NextResponse.json(
      { error: 'Error al leer las estadísticas' },
      { status: 500 }
    );
  }
}

export async function POST(request: Request) {
  try {
    await ensureDataDirectory();

    const newStats: PomodoroStats = await request.json();

    // Validate required properties
    if (!newStats || 
        typeof newStats.completedPomodoros !== 'number' ||
        !Array.isArray(newStats.dailyProgress) ||
        !Array.isArray(newStats.lastWeekPomodoros)) {
      return NextResponse.json(
        { error: 'Datos inválidos' },
        { status: 400 }
      );
    }

    // Merge with existing stats to prevent data loss
    const existingStats = await fs.readFile(STATS_FILE, 'utf8')
      .then(content => JSON.parse(content))
      .catch(() => defaultStats);

    const mergedStats = {
      ...existingStats,
      ...newStats,
      dailyProgress: newStats.dailyProgress.map((progress, index) => ({
        ...existingStats.dailyProgress[index],
        ...progress
      }))
    };

    await fs.writeFile(
      STATS_FILE,
      JSON.stringify(mergedStats, null, 2)
    );

    return NextResponse.json({ success: true });
  } catch (error) {
    console.error('Error saving stats:', error);
    return NextResponse.json(
      { error: 'Error al guardar las estadísticas' },
      { status: 500 }
    );
  }
}
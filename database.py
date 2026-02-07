import sqlite3
import pandas as pd

def init_db():
    conn = sqlite3.connect('community_relations.db')
    c = conn.cursor()
    
    # 1. جدول أولياء الأمور
    c.execute('''CREATE TABLE IF NOT EXISTS parents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        participation_type TEXT,
        expertise TEXT,
        interaction_level TEXT,
        phone TEXT
    )''')
    
    # 2. جدول خطة العمل
    c.execute('''CREATE TABLE IF NOT EXISTS action_plan (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        objective TEXT,
        activity TEXT,
        responsibility TEXT,
        timeframe TEXT,
        kpi TEXT,
        status TEXT DEFAULT 'قيد التنفيذ',
        priority TEXT,
        task_type TEXT DEFAULT 'معنوي'
    )''')
    
    # 4. جدول سجل اللقاءات والملاحظات التطويرية
    c.execute('''CREATE TABLE IF NOT EXISTS meetings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject TEXT,
        date DATE,
        attendees_count INTEGER,
        summary TEXT,
        ai_recommendations TEXT
    )''')

    # 5. جدول الفعاليات والأنشطة
    c.execute('''CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        date DATE,
        location TEXT,
        attendees_count INTEGER,
        rating INTEGER
    )''')
    
    conn.commit()
    conn.close()

def get_connection():
    return sqlite3.connect('community_relations.db', timeout=20)

if __name__ == "__main__":
    init_db()
    print("Database initialized successfully.")

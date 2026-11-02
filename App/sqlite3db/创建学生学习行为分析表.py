import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, 'dsavd.db')

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS student_learning_behavior (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    chapter TEXT NOT NULL,
    subchapter TEXT NOT NULL,
    attention_score REAL DEFAULT 0,
    total_frames INTEGER DEFAULT 0,
    emotion_count TEXT DEFAULT '{}',
    video_filename TEXT,
    learning_duration INTEGER DEFAULT 0,
    created_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
cursor.close()
conn.close()

print("学生学习行为分析表创建成功")

"""初始化基础项目与智慧教室共用的 MySQL 数据库。"""
from pathlib import Path
import os
import runpy


HERE = Path(__file__).resolve().parent
MIGRATIONS = (
    '创建学生学习行为分析表_mysql.py',
    '创建答题防作弊截图表_mysql.py',
    '创建智慧教室表_mysql.py',
)


def create_user_table():
    import pymysql
    import yaml

    config_path = HERE.parents[1] / 'config.yaml'
    config = yaml.safe_load(config_path.read_text(encoding='utf-8'))['mysql']
    config['password'] = os.environ.get('DSAVD_MYSQL_PASSWORD', config.get('password', ''))
    connection = pymysql.connect(
        host=config['host'], port=config['port'], user=config['user'], password=config['password'],
        database=config['database'], charset='utf8mb4'
    )
    with connection.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS app_user (
                id BIGINT PRIMARY KEY AUTO_INCREMENT,
                username VARCHAR(80) NOT NULL UNIQUE,
                password_hash VARCHAR(255) NOT NULL,
                role VARCHAR(20) NOT NULL DEFAULT 'student',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                INDEX idx_app_user_role (role)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
        """)
    connection.commit()
    connection.close()


def migrate_exam_records():
    """把原 SQLite 答题记录同步到共享 MySQL，保留旧接口兼容。"""
    import sqlite3
    import pymysql
    import yaml

    sqlite_path = HERE / 'dsavd.db'
    if not sqlite_path.exists():
        return
    sqlite_conn = sqlite3.connect(sqlite_path)
    table_exists = sqlite_conn.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name='exam_record'"
    ).fetchone()
    if not table_exists:
        sqlite_conn.execute("""
            CREATE TABLE exam_record (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                username TEXT NOT NULL, chapter TEXT NOT NULL, subchapter TEXT NOT NULL,
                score TEXT NOT NULL, created_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        sqlite_conn.commit()
        print('已补建 SQLite 兼容表 exam_record')
    records = sqlite_conn.execute('SELECT username, chapter, subchapter, score, created_time FROM exam_record').fetchall()
    sqlite_conn.close()

    config = yaml.safe_load((HERE.parents[1] / 'config.yaml').read_text(encoding='utf-8'))['mysql']
    config['password'] = os.environ.get('DSAVD_MYSQL_PASSWORD', config.get('password', ''))
    connection = pymysql.connect(
        host=config['host'], port=config['port'], user=config['user'], password=config['password'],
        database=config['database'], charset='utf8mb4'
    )
    with connection.cursor() as cursor:
        for username, chapter, subchapter, score, created_time in records:
            cursor.execute("""
                INSERT INTO exam_answer_record (username, chapter, subchapter, score, created_time)
                VALUES (%s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE score=VALUES(score), updated_time=CURRENT_TIMESTAMP
            """, (username, chapter, subchapter, float(score), created_time))
    connection.commit()
    connection.close()
    print(f'已同步 SQLite 答题记录到 MySQL: {len(records)} 条')


if __name__ == '__main__':
    for migration in MIGRATIONS:
        print(f'执行: {migration}')
        runpy.run_path(str(HERE / migration), run_name='__main__')
    create_user_table()
    migrate_exam_records()
    print('共享 MySQL 初始化完成：基础账号、学习行为、考试快照和智慧教室使用同一数据库。')

"""
创建答题防作弊截图表（MySQL 版）
运行方式：python 创建答题防作弊截图表_mysql.py
"""
import pymysql
import yaml
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_path = os.path.join(os.path.dirname(BASE_DIR), 'config.yaml')
with open(config_path, encoding='utf-8') as f:
    config = yaml.load(f.read(), Loader=yaml.FullLoader)

mysql_config = config['mysql']
mysql_config['password'] = os.environ.get('DSAVD_MYSQL_PASSWORD', mysql_config.get('password', ''))

conn = pymysql.connect(
    host=mysql_config['host'],
    port=mysql_config['port'],
    user=mysql_config['user'],
    password=mysql_config['password'],
    charset='utf8mb4'
)

cursor = conn.cursor()

cursor.execute(f"CREATE DATABASE IF NOT EXISTS {mysql_config['database']} DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
cursor.execute(f"USE {mysql_config['database']}")

# 截图以 BASE64 字符串方式存储，便于只保留最近 30 张
create_table_sql = """
CREATE TABLE IF NOT EXISTS exam_monitor_snapshot (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(100) NOT NULL,
    chapter VARCHAR(50) NOT NULL,
    subchapter VARCHAR(50) NOT NULL,
    image_base64 LONGTEXT,
    image_filename VARCHAR(255),
    ai_status VARCHAR(20) DEFAULT 'pending',
    phone_detected TINYINT(1) DEFAULT 0,
    phone_confidence FLOAT DEFAULT 0,
    person_count INT DEFAULT 0,
    ai_reason VARCHAR(500),
    analyzed_time TIMESTAMP NULL,
    created_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_username (username),
    INDEX idx_created_time (created_time)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
"""

cursor.execute(create_table_sql)

new_columns = {
    'ai_status': "VARCHAR(20) DEFAULT 'pending'",
    'phone_detected': 'TINYINT(1) DEFAULT 0',
    'phone_confidence': 'FLOAT DEFAULT 0',
    'person_count': 'INT DEFAULT 0',
    'ai_reason': 'VARCHAR(500)',
    'analyzed_time': 'TIMESTAMP NULL',
}
for column_name, column_sql in new_columns.items():
    cursor.execute(f"SHOW COLUMNS FROM exam_monitor_snapshot LIKE '{column_name}'")
    if not cursor.fetchone():
        cursor.execute(f"ALTER TABLE exam_monitor_snapshot ADD COLUMN {column_name} {column_sql}")

cursor.execute("""
CREATE TABLE IF NOT EXISTS exam_behavior_event (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(100) NOT NULL,
    chapter VARCHAR(50) NOT NULL,
    subchapter VARCHAR(50) NOT NULL,
    event_type VARCHAR(50) NOT NULL,
    event_detail VARCHAR(500),
    occurred_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_exam_event_user (username),
    INDEX idx_exam_event_scope (chapter, subchapter),
    INDEX idx_exam_event_time (occurred_time)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS exam_answer_record (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(100) NOT NULL,
    chapter VARCHAR(50) NOT NULL,
    subchapter VARCHAR(50) NOT NULL,
    score FLOAT NOT NULL DEFAULT 0,
    created_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY uk_exam_answer (username, chapter, subchapter),
    INDEX idx_exam_answer_time (created_time)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
""")
conn.commit()

print("答题防作弊截图表创建成功")

cursor.close()
conn.close()

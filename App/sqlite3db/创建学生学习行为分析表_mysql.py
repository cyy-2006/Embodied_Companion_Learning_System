"""
创建学生学习行为分析表（MySQL 版）
运行方式：python 创建学生学习行为分析表_mysql.py
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

create_table_sql = """
CREATE TABLE IF NOT EXISTS student_learning_behavior (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(100) NOT NULL,
    chapter VARCHAR(50) NOT NULL,
    subchapter VARCHAR(50) NOT NULL,
    attention_score FLOAT DEFAULT 0,
    is_distracted TINYINT(1) DEFAULT 0,
    behavior_label VARCHAR(30) DEFAULT '正常学习',
    total_frames INT DEFAULT 0,
    emotion_count TEXT,
    video_filename VARCHAR(255),
    learning_duration INT DEFAULT 0,
    created_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_username (username),
    INDEX idx_chapter (chapter, subchapter),
    INDEX idx_created_time (created_time)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
"""

cursor.execute(create_table_sql)

cursor.execute("SHOW COLUMNS FROM student_learning_behavior LIKE 'is_distracted'")
if not cursor.fetchone():
    cursor.execute("ALTER TABLE student_learning_behavior ADD COLUMN is_distracted TINYINT(1) DEFAULT 0 AFTER attention_score")
cursor.execute("SHOW COLUMNS FROM student_learning_behavior LIKE 'behavior_label'")
if not cursor.fetchone():
    cursor.execute("ALTER TABLE student_learning_behavior ADD COLUMN behavior_label VARCHAR(30) DEFAULT '正常学习' AFTER is_distracted")
cursor.execute("""
    UPDATE student_learning_behavior
    SET is_distracted = IF(attention_score < 40, 1, 0),
        behavior_label = IF(attention_score < 40, '疑似走神', '正常学习')
""")
conn.commit()

print("学生学习行为分析表创建成功")

cursor.close()
conn.close()

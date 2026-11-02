import sqlite3

# 连接到SQLite数据库
# 如果文件不存在，会自动在当前目录创建一个数据库文件
conn = sqlite3.connect('dsavd.db')

# 创建一个Cursor对象并调用其execute()方法执行SQL命令
cursor = conn.cursor()

# 删除表格  删除

# cursor.execute("DROP TABLE IF EXISTS exam_record")
cursor.execute("""
CREATE TABLE IF NOT EXISTS exam_record (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    username TEXT NOT NULL ,
    chapter NOT NULL ,
    subchapter NOT NULL ,
    score TEXT NOT NULL,
    created_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# 根据统计 subchapter 为 6.4出现的次数
cursor.execute("SELECT COUNT(subchapter) FROM exam_record WHERE subchapter = '6.5'")

# 删除学号为10005的数据



count = cursor.fetchone()[0]
print(count)
# 输出总人数

# 删除内容
# cursor.execute("DELETE FROM exam_record")

# 提交事务
conn.commit()

# 关闭Cursor和Connection
cursor.close()
conn.close()

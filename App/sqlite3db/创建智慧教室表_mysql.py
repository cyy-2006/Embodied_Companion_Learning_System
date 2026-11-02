"""创建智慧教室三维场景路线表；学习监管表由对应迁移脚本维护。"""
import os
import pymysql
import yaml

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_path = os.path.join(os.path.dirname(BASE_DIR), 'config.yaml')
with open(config_path, encoding='utf-8') as config_file:
    mysql_config = yaml.safe_load(config_file)['mysql']
mysql_config['password'] = os.environ.get('DSAVD_MYSQL_PASSWORD', mysql_config.get('password', ''))

conn = pymysql.connect(
    host=mysql_config['host'], port=mysql_config['port'], user=mysql_config['user'],
    password=mysql_config['password'], charset='utf8mb4'
)
cursor = conn.cursor()
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {mysql_config['database']} DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
cursor.execute(f"USE {mysql_config['database']}")
cursor.execute("""
CREATE TABLE IF NOT EXISTS rsm_classroom_route (
    id INT PRIMARY KEY AUTO_INCREMENT,
    route_name VARCHAR(100) NOT NULL COMMENT '路线名称',
    route_data TEXT COMMENT '路线数据JSON',
    obstacle_data TEXT COMMENT '障碍物数据JSON',
    create_by VARCHAR(50) COMMENT '创建者',
    create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    update_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    remark VARCHAR(500) COMMENT '备注'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='教室巡视路线表'
""")
conn.commit()
cursor.close()
conn.close()
print('智慧教室三维路线表创建成功: rsm_classroom_route')

import sqlite3

conn = sqlite3.connect('todo.db')
conn.execute("CREATE TABLE todo (id INTEGER PRIMARY KEY, task char(100) NOT NULL,status bool NOT NUll)")
conn.execute("INSERT INTO todo (task,status) VALUES ('加十个小姐姐的微信',0)")
conn.execute("INSERT INTO todo (task,status) VALUES ('赚10个亿',1)")
conn.execute("INSERT INTO todo (task,status) VALUES ('大笑10声',1)")
conn.commit()

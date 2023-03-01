import sqlite3

conn = sqlite3.connect('url.db')
conn.execute("CREATE TABLE url (id INTEGER PRIMARY KEY,longurl char(1000) NOT NULL)")
conn.commit()

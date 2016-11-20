import sqlite3

conn = sqlite3.connect('./database.db')
c = conn.cursor()

c.execute('CREATE TABLE users (id text, creds text)')

c.execute('CREATE TABLE comments (id text, comment text)')

conn.commit()
conn.close()

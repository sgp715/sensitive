import sqlite3


conn = sqlite3.connect('./database.db')
c = conn.cursor()

c.execute('CREATE TABLE users (id text)')

conn.commit()
conn.close()

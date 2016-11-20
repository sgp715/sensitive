import sqlite3
import time

from youtube import youtube

from dandelion import dandelion

DATABASE = './database/database.db'

conn = sqlite3.connect('./database.db')
c = conn.cursor()

while True:

    mins = 1
    sweep_time = mins * 60
    time.sleep(sweep_time)

    for row in c.execute('SELECT * FROM users):
        if row

conn.close()

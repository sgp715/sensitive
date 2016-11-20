import sqlite3
import time
import json

import ast

from youtube import youtube

from dandelion import dandelion

DATABASE = './database/database.db'

conn = sqlite3.connect('./database.db')
c = conn.cursor()

while True:

    mins = 1
    sweep_time = mins * 60
    time.sleep(sweep_time)

    for row in c.execute('SELECT * FROM users'):
        id = row[0]
        creds = json.loads(= ast.literal_eval(row[1]))
        youtube_api = youtube.youtubeAPI(creds)
        threads = get_channel_threads()

        # iterate over comments and rate their sentiment

        # deltd list of negative ones

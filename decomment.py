import sqlite3
import time
import json

import ast

from youtube import youtube

from dandelion import dandelion

DATABASE = './database/database.db'

conn = sqlite3.connect(DATABASE)
c = conn.cursor()

# TODO: look at token refresh https://developers.google.com/youtube/v3/guides/auth/server-side-web-apps#OAuth2_Refreshing_a_Token
for row in c.execute('SELECT * FROM users'):
    youtube_api = youtube.youtubeAPI(row[1])
    comments = youtube_api.get_comments()
    print comments

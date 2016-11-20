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

    temp_row = (u'UCW4C_qVMMbidqni7noNNZDg', u'"{\\"_module\\": \\"oauth2client.client\\", \\"scopes\\": [\\"https://www.googleapis.com/auth/youtube.force-ssl\\"], \\"token_expiry\\": \\"2016-11-20T14:53:32Z\\", \\"id_token\\": null, \\"access_token\\": \\"ya29.CjCcA7Q848RJHXxsV8V-RlCv_5JjiZM9AGaPEX9mufqxjIaaEiIGiSUKoAEEhGAHHW0\\", \\"token_uri\\": \\"https://accounts.google.com/o/oauth2/token\\", \\"invalid\\": false, \\"token_response\\": {\\"access_token\\": \\"ya29.CjCcA7Q848RJHXxsV8V-RlCv_5JjiZM9AGaPEX9mufqxjIaaEiIGiSUKoAEEhGAHHW0\\", \\"token_type\\": \\"Bearer\\", \\"expires_in\\": 3600}, \\"client_id\\": \\"425814746481-rtbl3jnrsdpli44goq4aufmlu84ii4bl.apps.googleusercontent.com\\", \\"token_info_uri\\": \\"https://www.googleapis.com/oauth2/v3/tokeninfo\\", \\"client_secret\\": \\"qOj18iHicJUoeRp3CcTJhMAq\\", \\"revoke_uri\\": \\"https://accounts.google.com/o/oauth2/revoke\\", \\"_class\\": \\"OAuth2Credentials\\", \\"refresh_token\\": null, \\"user_agent\\": null}"')
    temp = [temp_row, temp_row]
    for row in temp:#c.execute('SELECT * FROM users'):
        id = row[0]
        creds = json.loads(= ast.literal_eval(row[1]))
        youtube_api = youtube.youtubeAPI(creds)
        threads = get_channel_threads()

        # iterate over comments and rate their sentiment

        # deltd list of negative ones



conn.close()

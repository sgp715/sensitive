# Usage example:
# python server.py

import json

import flask
import httplib2
from flask import render_template
from googleapiclient.discovery import build
from oauth2client import client

import sqlite3
from flask import g

DATABASE = './database/database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

app = flask.Flask(__name__)

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
  if 'credentials' not in flask.session:
    return flask.redirect(flask.url_for('oauth2callback'))
  credentials = client.OAuth2Credentials.from_json(flask.session['credentials'])
  if credentials.access_token_expired:
    return flask.redirect(flask.url_for('oauth2callback'))
  else:
    http_auth = credentials.authorize(httplib2.Http())
    youtube = build('youtube', 'v3', http_auth)
    response = youtube.channels().list(part="id", mine="true").execute()
    # response = youtube.commentThreads().list(
    #     part="snippet",
    #     allThreadsRelatedToChannelId="UCW4C_qVMMbidqni7noNNZDg",
    #     textFormat="plainText"
    # ).execute()
    id = response.get("items")[0].get("id")

    print 'adding to data'
    c = get_db().cursor()
    c.execute("insert into users values (1)")
    c.close()

    return flask.redirect('user/' + id)

@app.route('/user/<id>')
def user(id):
    return id

@app.route('/oauth2callback')
def oauth2callback():
  flow = client.flow_from_clientsecrets(
      'client_secrets.json',
      scope='https://www.googleapis.com/auth/youtube.force-ssl',
      redirect_uri=flask.url_for('oauth2callback', _external=True))
      #include_granted_scopes=True)
  if 'code' not in flask.request.args:
    auth_uri = flow.step1_get_authorize_url()
    return flask.redirect(auth_uri)
  else:
    auth_code = flask.request.args.get('code')
    credentials = flow.step2_exchange(auth_code)
    flask.session['credentials'] = credentials.to_json()
    return flask.redirect(flask.url_for('login'))


if __name__ == '__main__':
  import uuid
  from optparse import OptionParser

  app.secret_key = str(uuid.uuid4())

  parser = OptionParser()

  parser.add_option("-p", "--prod",
                action="store_true", dest="prod", default=False,
                help="don't print status messages to stdout")
  (options, args) = parser.parse_args()

  if options.prod == True:
      app.run(host='0.0.0.0',port=80)
  else:
      app.run(use_debugger=True, debug=True,
    use_reloader=True)

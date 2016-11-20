import json

import flask
import httplib2

from googleapiclient.discovery import build
from oauth2client import client

import unittest

import httplib2

from googleapiclient.discovery import build

class youtubeAPI():

    def __init__(self, creds):
        credentials = client.OAuth2Credentials.from_json(creds)
        self.http_auth = credentials.authorize(httplib2.Http())


    def _get_channel_id(self):

        self.youtube = build('youtube', 'v3', http_auth)

        response = self.youtube.channels().list(part="id", mine="true").execute()
        #id = response.get("items")[0].get("id")
        return response

    def get_channel_id(self, json_data):

        pass

    def _get_channel_threads(self, channel_id):

        response = self.youtube.commentThreads().list(
            part="snippet, id, replies",
            allThreadsRelatedToChannelId=channel_id,#"UCW4C_qVMMbidqni7noNNZDg",
            textFormat="plainText"
        ).execute()

        return response

    def get_channel_threads(self, json_data):

        pass

    def delete_comment(self, comment_id):

        # returns 204 if successful
        self.youtube.comments().delete(
        id=comment_id
        ).execute()

    def delete_comments(self, list):

        for comment_id in list:
            delete_comment(comment_id)

class TestY(unittest.TestCase):

    unittest.creds = '{"_module": "oauth2client.client", "scopes": ["https://www.googleapis.com/auth/youtube.force-ssl"], "token_expiry": "2016-11-20T15:42:52Z", "id_token": null, "access_token": "ya29.CjCcA1uzo-j58ihT6Rb34Eaoh_5n1f8NxFb0ervV5goMDeWx-xjEAnA68IBm_-9v5r8", "token_uri": "https://accounts.google.com/o/oauth2/token", "invalid": false, "token_response": {"access_token": "ya29.CjCcA1uzo-j58ihT6Rb34Eaoh_5n1f8NxFb0ervV5goMDeWx-xjEAnA68IBm_-9v5r8", "token_type": "Bearer", "expires_in": 3600}, "client_id": "425814746481-rtbl3jnrsdpli44goq4aufmlu84ii4bl.apps.googleusercontent.com", "token_info_uri": "https://www.googleapis.com/oauth2/v3/tokeninfo", "client_secret": "qOj18iHicJUoeRp3CcTJhMAq", "revoke_uri": "https://accounts.google.com/o/oauth2/revoke", "_class": "OAuth2Credentials", "refresh_token": null, "user_agent": null}'
    unittest.youtube =  youtubeAPI(unittest.creds)

    #def test_good(self):
    #    print unittest.youtube_get_channel_id()

    def test_bad(self):
        pass

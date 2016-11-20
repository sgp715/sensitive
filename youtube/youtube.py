import json

from googleapiclient.discovery import build
from oauth2client import client


class youtubeAPI():

    def __init__(self, creds):
        credentials = client.OAuth2Credentials.from_json(creds)
        http_auth = credentials.authorize(httplib2.Http())

        #if credentials.access_token_expired:

        self.youtube = build('youtube', 'v3', http_auth)


    def get_channel_id(self):

        response = youtube.channels().list(part="id", mine="true").execute()
        #id = response.get("items")[0].get("id")
        return response

    def get_channel_threads(self, channel_id):

        response = youtube.commentThreads().list(
            part="snippet, id, replies",
            allThreadsRelatedToChannelId=channel_id,#"UCW4C_qVMMbidqni7noNNZDg",
            textFormat="plainText"
        ).execute()

        return response


    def delete_comment(self, comment_id):

        # returns 204 if successful
        youtube.comments().delete(
        id=comment_id
        ).execute()

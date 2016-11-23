import json

import flask
import httplib2

from googleapiclient.discovery import build
from oauth2client import client

import unittest

import httplib2

from googleapiclient.discovery import build

import itertools

class youtubeAPI():

    def __init__(self, creds):
        credentials = client.OAuth2Credentials.from_json(creds)
        http_auth = credentials.authorize(httplib2.Http())

        self.http_youtube = build('youtube', 'v3', http_auth)

    def _get_channel_id(self):

        channel = None
        try:
            json_data = self.http_youtube.channels().list(part="id", mine="true").execute()
            channel = json_data['items'][0]['id']
        except:
            print 'Could not get channel id'

        return channel

    def _get_channel_uploads(self):

        uploads = None

        try:
            json_data = self.http_youtube.channels().list(part="contentDetails", mine="true").execute()
            uploads = json_data['items'][0]['contentDetails']['relatedPlaylists']['uploads']
        except:
            print 'Could not get channel uploads'

        return uploads

    def _get_video_ids(self, playlist_id):

        response = None
        try:
            response = self.http_youtube.playlistItems().list(
                part='contentDetails',
                playlistId=playlist_id
            ).execute()
        except:
            print 'Could not get video ids'
            return response

        items = response['items']

        video_ids = []
        for content in items:
            video_ids.append(content['contentDetails']['videoId'])

        return video_ids

    def _get_comment_thread(self, video_id):

        json_data = None
        try:
            json_data = self.http_youtube.commentThreads().list(
                part='id, snippet',
                videoId=video_id,
                textFormat='plainText'
            ).execute()
        except:
            print 'Could not get comment thread'
            return json_data

        comments = []

        for comment in json_data['items']:
            comments.append((comment['id'], comment['snippet']['topLevelComment']['snippet']['textOriginal']))

        return comments

    def _get_comment_threads(self, video_ids):

        comments = []

        for v_id in video_ids:
            comments = itertools.chain(comments, self._get_comment_thread(v_id))

        return list(comments)

    def get_comments(self):

         uploads = self._get_channel_uploads()
         video_ids = self._get_video_ids(uploads)
         return self._get_comment_threads(video_ids)


    def _delete_comment(self, comment_id):

        try:
            response = self.http_youtube.comments().delete(id=comment_id).execute()
        except:
            print "Couldn't delete..."

    def delete_comments(self, comments):

        for comment in comments:

            id = comment[0]
            text = comment[1]
            print "Deleting comment: " + text + "with id: " + id
            self._delete_comment(id)


# if __name__ == "__main__":
#
#     creds = '{"_module": "oauth2client.client", "scopes": ["https://www.googleapis.com/auth/youtube.force-ssl"], "token_expiry": "2016-11-23T05:42:54Z", "id_token": null, "access_token": "ya29.Ci-fAz4L0v5CyI_PjTUa7maXdRdw_UuDe8T3tIQ2YCUDxLRVZrg4AN08sWE3I7furw", "token_uri": "https://accounts.google.com/o/oauth2/token", "invalid": false, "token_response": {"access_token": "ya29.Ci-fAz4L0v5CyI_PjTUa7maXdRdw_UuDe8T3tIQ2YCUDxLRVZrg4AN08sWE3I7furw", "token_type": "Bearer", "expires_in": 3600, "refresh_token": "1/oUkp3CTGC5X3B6bzlv2zjDIPk4ycgC_SBAvVCFeRPv0"}, "client_id": "425814746481-rtbl3jnrsdpli44goq4aufmlu84ii4bl.apps.googleusercontent.com", "token_info_uri": "https://www.googleapis.com/oauth2/v3/tokeninfo", "client_secret": "qOj18iHicJUoeRp3CcTJhMAq", "revoke_uri": "https://accounts.google.com/o/oauth2/revoke", "_class": "OAuth2Credentials", "refresh_token": "1/oUkp3CTGC5X3B6bzlv2zjDIPk4ycgC_SBAvVCFeRPv0", "user_agent": null}'
#
#     youtube = youtubeAPI(creds)
#
#     uploads = youtube.get_channel_uploads()
#     vids = youtube.get_video_ids(uploads)
#     comment = youtube.get_comment_thread(vids[0])
#     print comment[0][0]
#     print comment[0][1]
#     youtube.delete_comment( comment[0][0])

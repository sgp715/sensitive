import json

import flask
import httplib2

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client import client

import httplib2

from googleapiclient.discovery import build

import itertools

def handle_http_error(request):

    try:
        resp = request.execute()
        return resp
    except HttpError, e:
        print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)

class youtubeAPI():

    def __init__(self, creds):
        credentials = client.OAuth2Credentials.from_json(creds)
        http_auth = credentials.authorize(httplib2.Http())

        self.http_youtube = build('youtube', 'v3', http_auth)

    def _get_channel_id(self):

        channel = None
        #try:
        json_data = handle_http_error(self.http_youtube.channels().list(part="id", mine="true")) #.execute()
        channel = json_data['items'][0]['id']
        #except:
        #    print 'Could not get channel id'

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
            comments.append((comment['id'], comment['snippet']['topLevelComment']['snippet']['textDisplay']))

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
        # doesn't work for some reason...

        for comment in comments:

            id = comment[0]
            text = comment[1]
            print "Deleting comment: " + text + " with id: " + id
            self._delete_comment(id)

    def _mark_spam(self, comment_id):

        try:
            response = self.http_youtube.comments().markAsSpam(id=comment_id).execute()
        except HttpError, e:
            print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)

    def mark_spam(self, comments):

        for comment in comments:

            id = comment[0]
            text = comment[1]
            self._mark_spam(id)

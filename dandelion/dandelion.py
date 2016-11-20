import requests
import json
import unittest

json_data = ''
with open('./dandelion/creds.json') as f:
    json_data = json.load(f)

key = json_data.get('key')
lang = json_data.get('lang')

def _make_url(text):
    """
    take text to send and make it sendable
    """

    text_array = text.split()

    url_text = ''
    for w in text_array:
        url_text += (w + '%20')

    return url_text

def request_sentiment(text):
    """
    query dandelion for sentiment
    """

    url_text = _make_url(text)

    r = requests.get('https://api.dandelion.eu/datatxt/sent/v1/?lang=' + lang + '&text=' + url_text + '&token=' + key)

    val = None
    if r.status_code == 200:
        val = r.json()
    
    print val

    return val

def sentiment_list(list):
    """
    given list of comments return list of sentiments
    """

    ids = []
    for t in list:

        s = get_score(request_sentiment(t[1]))

        if s < 0:
            ids.append(t[0])

    return ids


def get_score(json_data):
    """
    extract score from data
    """

    return json_data.get('sentiment').get('score')


class TestStringMethods(unittest.TestCase):


    def test_good(self):
        g = 'I really love your APIs'
        good = get_score(request_sentiment(g))
        self.assertGreater(good, 0)

    def test_bad(self):
        b = 'Suck my dick'
        bad = get_score(request_sentiment(b))
        self.assertLess(bad, 0)

if __name__ == "__main__":

    unittest.main()

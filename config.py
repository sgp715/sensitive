from authomatic.providers import oauth2

CONFIG = {

    'g': {

        'class_': oauth2.Google,

        'consumer_key': '425814746481-rtbl3jnrsdpli44goq4aufmlu84ii4bl.apps.googleusercontent.com',
        'consumer_secret': 'qOj18iHicJUoeRp3CcTJhMAq',

        'scope': ['https://www.googleapis.com/auth/youtube.force-ssl'],
    }
}

from social.backends.oauth import BaseOAuth2
from urllib import urlencode, urlopen
import json

class ChangeTipOAuth2(BaseOAuth2):
    """ChangeTip OAuth authentication backend"""
    name = 'changetip'
    AUTHORIZATION_URL = 'https://www.changetip.com/o/authorize/'
    ACCESS_TOKEN_URL = 'https://www.changetip.com/o/token/'
    ACCESS_TOKEN_METHOD = 'POST'
    SCOPE_SEPARATOR = ' '

    def get_user_details(self, response):
        """Return user details from ChangeTip account"""
        return {'username': response['username'],
                'email': response['email'] or ''}

    def user_data(self, access_token, *args, **kwargs):
        """Loads user data from service"""
        url = 'https://www.changetip.com/v2/me/?' + urlencode({
            'oauth_consumer_key': access_token
        })
        try:
            return json.load(urlopen(url))
        except ValueError:
            return None
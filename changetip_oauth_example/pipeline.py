import requests


def verify_channel_user(strategy, user, request, **kwargs):
    social = user.social_auth.get(provider='changetip')
    requests.post(
        'https://www.changetip.com/v2/verify-channel-user/',
        {
            'access_token': social.extra_data['access_token'],
            'channel_uid': user.id,
            'channel_username': user.username,
        }
    )

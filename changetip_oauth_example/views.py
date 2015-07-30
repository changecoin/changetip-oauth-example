from django.shortcuts import render_to_response
from django.template.context import RequestContext

import requests


def home(request):
    try:
        social = request.user.social_auth.get(provider='changetip')
        response = requests.get(
            'https://www.changetip.com/v2/me/',
            params={'access_token': social.extra_data['access_token']}
        )

        context = RequestContext(request, {'user': request.user, 'data': response.json()})
    except AttributeError:
        context = RequestContext(request, {'user': request.user})

    return render_to_response('home.html',
                              context_instance=context)
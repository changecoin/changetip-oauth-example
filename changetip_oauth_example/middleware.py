from django.shortcuts import redirect


from social.apps.django_app.middleware import SocialAuthExceptionMiddleware
from social import exceptions as social_exceptions

class SocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
    def process_exception(self, request, exception):
        if hasattr(social_exceptions, 'AuthCanceled'):
            # Note: You'll probably want to update this for your own specific application
            # and do something more than just redirect to the homepage.
            return redirect('/')
        else:
            raise exception
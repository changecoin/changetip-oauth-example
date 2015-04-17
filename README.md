# changetip-oauth-example

###Prerequisites:

This tutorial assumes you already have the basics for a Python-based development environment. It also assumes some knowledge of setting up a Django project.

- [Python 2.7](https://www.python.org/) (other versions may work, but only 2.7 has been tested)
- [MySQL](http://www.mysql.com/)
- [pip](https://pip.pypa.io/en/latest/)
- [Django](https://www.djangoproject.com/)
- [ngrok](https://ngrok.com/)

You'll also need an account on [ChangeTip](https://www.changetip.com/).

###Installation:

- Create a directory for your project, and clone this repository there
- open a terminal and change to that directory
- in MySQL, execute the following command: `CREATE DATABASE changetip_oauth_example;`
- run the following command: `pip install -r requirements.txt`
- set up the initial database by running: `python manage.py migrate`
- start the server by running: `python manage.py runserver`
- if you're running an app locally (localhost) you'll need to use a tunnel so you can receive external Http requests needed for Oauth2. Ngrok is a good solution. Start ngrok by running: `ngrok 8000`, and make a note of your ngrok url (e.g. http://ABCDEFG.ngrok.com)

###Registration of your application on ChangeTip

- Log in to [ChangeTip](https://www.changetip.com/)
- [Visit the application registration form on ChangeTip](https://www.changetip.com/o/applications/register/)
- Give your application a name, such as `myTestApp`
- In the "redirect_uris", enter your ngrok url, followed by /complete/changetip/ - it should look something like: `http://ABCDEFG.ngrok.com/complete/changetip/`
- Make a note of your `client_id` and `client_secret`, as you'll need these for the next section

###Setup:

You will need to configure a few things before getting started. In `changetip-oauth-example/settings.py`, edit the following settings:

- `SOCIAL_AUTH_CHANGETIP_KEY = client_id` (use your application's Client ID)
- `SOCIAL_AUTH_CHANGETIP_SECRET = client_secret` (use your application's Client Secret)

###Testing the example application:

Open your browser to the URL provided by ngrok - you should be presented with a simple page that
has a "Sign in with ChangeTip" button.

Click the button - you should be taken to a page on ChangeTip that asks if you'd like to authorize
the application to connect to your account. Click "Allow".

Upon your return, you should see a page that acknowledges you as logged in, and displays some
basic data from your user account on ChangeTip.

###How it works:

Because the OAuth2 spec is implemented consistently between many sites, most of the heavy lifting for
the actual authorization and linkage of accounts is taken care of by the `python-social-auth` and
`oauthlib` packages without much additional work. Until `python-social-auth` includes a ChangeTip
"backend" by default, one is manually added in [backends.py](https://github.com/changecoin/changetip-oauth-example/blob/master/backends.py)

For an example of how the API call is made by the server, see [views.py](https://github.com/changecoin/changetip-oauth-example/blob/master/changetip_oauth_example/views.py)

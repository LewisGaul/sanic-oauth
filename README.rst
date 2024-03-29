Sanic OAuth
-----------


Simple OAuth library to work with sanic. Basically, just rewrited version of aioauth_client_ with async/await syntax and some optimization.

Available providers (in alphabetic order):

- Amazon
- BitBucket
- BitBucket v2
- Discord (thanks to @smlbiobot)
- Eventbrite
- Facebook
- Flickr
- Foursquare
- Github
- GitLab
- Google
- LinkedIn
- Meetup
- Naver
- ok.ru
- Pinterest
- Plurk
- Tumblr
- Twitter
- Vimeo
- vk.com
- Yahoo
- Yandex


Requirements
============

* python >= 3.6


Installation
============

1. Download Zip of this repository: `https://github.com/TrulyBright/sanic-oauth/archive/master.zip`
2. Install via pip:

.. code::

    pip install <path_to_the_zip_file>

Note, that to use blueprint correctly, you need to additionally install :code:`sanic>=20.0` and :code:`sanic-session`.


Usage
=====

Simple way for use this is blueprint with oauth configuration.

But, before use it you need to:

1. Create :code:`aiohttp.ClientSession` and bind to app like :code:`async_session` variable.
2. Create session interface from :code:`sanic-session` package and bind it to app like :code:`session_interface` variable.
3. Configure :code:`app.config` settings. You should pass :code:`OAUTH_PROVIDER, OAUTH_REDIRECT_URI, OAUTH_SCOPE` and another settings, for example, :code:`OAUTH_CLIENT_ID, OAUTH_CLIENT_SECRET`. Every setting with :code:`OAUTH` prefix will be passed to oauth provider construction.
4. Apply blueprint
5. Add decorator :code:`login_required` to routes, that required oauth.


You can see example_ for more details.


Advanced usage
==============

If you don't like current blueprint, you always can use providers directly and implements you own logic, like in old_example_.



.. _example: ./example.py
.. _old_example: ./old_example.py
.. _aioauth_client: https://github.com/klen/aioauth-client

"""
views.py

URL route handlers

Note that any handler params must match the URL route params.
For example the *say_hello* handler, handling the URL route '/hello/<username>',
  must be passed *username* as the argument.

"""


from google.appengine.api import users
from google.appengine.runtime.apiproxy_errors import CapabilityDisabledError

from flask import render_template, flash, url_for, redirect

from application.models import ExampleModel
from application.decorators import login_required, admin_required
from application.forms import ExampleForm

import passlib

def home():
  return render_template('home.html')


def say_hello(username):
  """Contrived example to demonstrate Flask's url routing capabilities"""
  return 'Hello %s' % username


def warmup():
  """App Engine warmup handler
  See http://code.google.com/appengine/docs/python/config/appconfig.html#Warming_Requests

  """
  return ''


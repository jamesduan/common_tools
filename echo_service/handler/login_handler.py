
import logging

import pyrestful.rest
from pyrestful import mediatypes
from pyrestful.rest import get, post

class LoginHandler(pyrestful.rest.RestHandler):

	@post(_path='/login', _types=[str, str, str],
			_produces=mediatypes.APPLICATION_JSON)

	def login_h(self, username, password, email):

		user = dict(usr_name = username,
					passwd = password,
					mail = email)
		return user

class EchoService(pyrestful.rest.RestHandler):

	@get(_path="/echo/{name}", _produces=mediatypes.APPLICATION_JSON)
	def sayHello(self, name):
		return {"hello" : name}


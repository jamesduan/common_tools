#!/usr/bin/env python

import os
import logging

from tornado.options import define, options, parse_command_line
from tornado.ioloop import IOLoop
import pyrestful.rest
from pyrestful import mediatypes
from pyrestful.rest import get, post

define("port", default=8888, type=int)

class EchoService(pyrestful.rest.RestHandler):

	@get(_path="/echo/{name}", _produces=mediatypes.APPLICATION_JSON)
	def sayHello(self, name):
		return {"hello" : name}

class LoginService(pyrestful.rest.RestHandler):

	@post(_path='/login', _types=[str, str, str], _produces=mediatypes.APPLICATION_JSON)
	def login_h(self, username, password, email):

		user = dict(usr_name = username,
					passwd = password,
					mail = email)
		return user

def create_server():

	logging.debug("parse command line...")
	parse_command_line()
	service_list = [
		EchoService,
		LoginService
	]
	logging.debug("create app by service list...")
	app = pyrestful.rest.RestService(service_list)
	logging.debug("listening in " + str(options.port))
	app.listen(options.port)
	logging.debug("instance start ...")
	IOLoop.instance().start()

if __name__ == "__main__":

	try:
		create_server()
	except KeyboardInterrupt, e:
		print "Canceled by user typed : Ctrl+C ", e
	except Exception, e:
		print e


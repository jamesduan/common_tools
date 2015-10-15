#!/usr/bin/env python

import json
import uuid

from bs4 import BeautifulSoup
from tornado.web import Application, RequestHandler
from tornado.httpserver import HTTPServer
from tornado.options import define, options, parse_command_line
from tornado.ioloop import IOLoop

define("port", default=8888, type=int)

class Session(object):
	"session_id, "

	def __init__(self):
		self.session_id = str(uuid.uuid4()).replace('-', '')

class UploadHtmlHandler(RequestHandler):

    def post(self):
        soup = BeautifulSoup(self.request.body)
        print 'title: ', str(soup.find_all('title'))[0]
        print 'body: ', soup.find_all('body')
        self.write('200')

class LoginHandler(RequestHandler):

	def post(self):

		username = self.request.body_arguments['username'][0]
		password = self.request.body_arguments['passwd'][0]

		if username == "jamesduan" and password == "bios_suererdlxmn":
			print "login success and create session."
			session = Session()
			session.__setattr__('username', username)
			print "write to page"
			self.write(session.session_id + session.username)
		else:
			print "login error, please try again.!"
			self.write("login error!")

class MyApplication(Application):

    def __init__(self):

        handlers = [
            (r'/upload_html', UploadHtmlHandler),
            (r'/login', LoginHandler),
        ]

        settings = dict()

        Application.__init__(self, handlers, settings)

def create_server():
    parse_command_line()
    http_server = HTTPServer(MyApplication())
    http_server.listen(options.port)
    IOLoop.instance().start()


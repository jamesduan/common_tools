#!/usr/bin/env python

#import json
#import uuid

#from bs4 import BeautifulSoup
##from tornado.web import Application, RequestHandler
#from tornado.httpserver import HTTPServer
#from tornado.options import define, options, parse_command_line
#from tornado.ioloop import IOLoop
#
#define("port", default=8888, type=int)
#
import tornado.ioloop
import pyrestful.rest

from pyrestful import mediatypes
from pyrestful.rest import get

class EchoService(pyrestful.rest.RestHandler):

	@get(_path="/echo/{name}", _produces=mediatypes.APPLICATION_JSON)
	def sayHello(self, name):
		return {"hello" : name}

#class UploadHtmlHandler(RequestHandler):
#
#    def post(self):
#        soup = BeautifulSoup(self.request.body)
#        print 'title: ', str(soup.find_all('title'))[0]
#        print 'body: ', soup.find_all('body')
#        self.write('200')
#
#class LoginHandler(RequestHandler):
#
#	def post(self):
#
#		username = self.get_argument("username")
#		password = self.get_argument("password")
#
#		print username, password
#
#		if username == "jamesduan" and password == "bios_suererdlxmn":
#			print "login success and create session."
#			session = Session()
#			session.__setattr__('username', username)
#			print "write to page"
#			self.set_header("Access-Control-Allow-Origin", "*")
#			self.write(session.session_id + session.username)
#		else:
#			print "login error, please try again.!"
#			self.write("login error!")

#class MyApplication(Application):
#
#    def __init__(self):
#
#        handlers = [
#            (r'/upload_html', UploadHtmlHandler),
#            (r'/login', LoginHandler),
#        ]
#
#        settings = dict()
#
#        Application.__init__(self, handlers, settings)

def create_server():
	print "start echo service..."
	app = pyrestful.rest.RestService([EchoService])
	app.listen(9999)
	tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
	try:
		create_server()
	except Exception, e:
		print e


from SimpleXMLRPCServer import SimpleXMLRPCServer
import logging
import os

PORT=9020
HOST='0.0.0.0'

logging.basicConfig(level=logging.DEBUG)
server = SimpleXMLRPCServer((HOST, PORT), logRequests=True)

# Expose a function

def list_contents(dir_name):
	logging.debug('list_contents({dirname})'.format(dirname=dir_name))
	return os.listdir(dir_name)

server.register_function(list_contents)

try:
	print "Listening on ", HOST, PORT
	print "Use Control + c to exit."
	server.serve_forever()
except KeyboardInterrupt, e:
	print "Good Bye.", e


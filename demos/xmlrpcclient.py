
import xmlrpclib

proxy = xmlrpclib.ServerProxy('http://localhost:9020')
print proxy.list_contents('/tmp')


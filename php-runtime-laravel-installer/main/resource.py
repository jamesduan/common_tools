''' this is a resource class for os resource operation.
	can use it to action include: file , directory,
	template for config.
'''

import os, sys, shutil, zipfile, tarfile
import subprocess, logging
from subprocess import call
import urllib2

from colors import red

from settings import logger

def check_permission(func):

	def check(*args, **kargs):

		uid, gid = os.getuid(), os.getgid()

		if uid != 0 and gid != 0:
			logger.error("please use root privilege to exec.")
			sys.exit(1)

		return func(*args, **kargs)

	return check

@check_permission
def directory(path="", mode=0755, recursive=False, action='create'):

	if not path:
		logger.warn("please sepecific the directory name.")
		sys.exit(1)


	if action == "create":

		is_exists_dir = os.path.exists(path)

		if is_exists_dir:
			try:
				shutil.rmtree(path)
			except OSError, e:
				logger.error("rm path: %s error" % (path) + str(e))
				sys.exit(1)

		if not recursive:
			try:
				os.mkdir(path, mode)
				#logger.info("Create directory done.")
				return True
			except OSError, e:
				print e, "exit."
				sys.exit(1)
		elif recursive:

			try:
				os.makedirs(path)
				#logger.info("create directory done.")
				return True
			except OSError, e:
				logger.error(str(e) + "exit.")
				sys.exit(1)

	if action == "delete":

		if os.path.exists(path):

			if not recursive:
				try:
					os.rmdir(path)
					return 0
				except OSError, e:
					logger.error(str(e) + "exit.")
					sys.exit(1)
			elif recursive:
				try:
					os.system("rm -rf " + path)
				except OSError, e:
					logger.error(str(e) + "exit.")
					sys.exit(1)
		else:
			logger.error("path : %s is not exists." % (path))

@check_permission
def r_file(filename, mode=None, content="", action=""):

	is_exists_file = os.path.exists(filename)

	if action == "create":

		if is_exists_file:

			try:
				os.remove(filename)
				os.mknod(filename)
				logger.info("Create File Ok.")

				with open(filename , 'w+') as f:
					f.write(content)

			except OSError, e:
				logger.error("filename: %s " % (filename) + str(e) )
				sys.exit(1)
		else:

			try:
				os.mknod(filename)
				logger.info("Create File Ok.")

				with open(filename , 'w+') as f:
					f.write(content)

			except OSError, e:
				logger.error("filename: %s" % (filename) + str(e))
				sys.exit(1)

	if action == "delete":

		if is_exists_file:
			try:
				os.remove(filename)
			except OSError, e:
				logger.error("path: %s " % (filename) + str(e))
				sys.exit(1)
		else:
			logger.error("path: %s" % (filename) + "is not exists.")
			sys.exit(1)

def create_user(username):

	if username:
		try:
			ps = subprocess.Popen(['/usr/sbin/useradd', username], stdout=subprocess.PIPE,
								stderr=subprocess.PIPE)
			output = ps.communicate()

			if not output[0] and not output[1]:
				logger.info("Add user: %s Ok." % (username))
				return True
			print output
		except OSError, e:
			logger.error("command: /usr/sbin/useradd %s" % str(e))
			sys.exit(1)
		except ValueError, e:
			logger.error("username : {user}".format(user=username) + "%s." % str(e))
			sys.exit(1)

def del_user(username):

	if username:

		try:

			ps = subprocess.Popen(['/usr/sbin/userdel', '-r', username], stdout=subprocess.PIPE,
								stderr=subprocess.PIPE)
			output = ps.communicate()
			if not output[0] and not output[1]:
				logger.info("Del user: %s Ok." % (username))

		except OSError, e:
			logger.error("command: /usr/sbin/userdel %s" %(str(e)))
			sys.exit(1)
		except ValueError, e:
			logger.error("username : %s, %s" % ( username , str(e)))
			sys.exit(1)

def is_exists_user(username):

	if username:
		try:
			ps = subprocess.Popen(['id', username], stdout=subprocess.PIPE,
								stderr=subprocess.PIPE)
			output = ps.communicate()
			if output[0]:
				return True
			elif output[1]:
				return False
		except OSError, e:
			logger.error("command: id %s " % str(e))
			sys.exit(1)
		except ValueError, e:
			logger.error("username : %s, %s" % ( username , str(e)))
			sys.exit(1)

@check_permission
def user(username):

	if username:
		if is_exists_user(username):
			del_user(username)
			create_user(username)
		else:
			create_user(username)

def group(): pass

@check_permission
def package(pkg_name, option="-y"):

	if pkg_name:
		command_line_str = "yum " + option + " install " + pkg_name
		if os.system(command_line_str)!=0:
			logger.error("exec: %s error" % (command_line_str))
			sys.exit(1)

def is_exists_rpmpkg(pkg_name):

	if pkg_name:
		command_line_str = "rpm -qa " + pkg_name
		if not os.popen(command_line_str).read():
			logger.info("%s is not exists!" % (pkg_name))
			return False
		return True

@check_permission
def unpack(pkg_name, workdir):

	if pkg_name:

		if '.zip' == pkg_name[-4:]:

			try:
				zipf = zipfile.ZipFile(pkg_name, 'r')
				zipf.extractall(workdir)
				return True

			except OSError, oserr:

				logger.error(str(oserr))
				directory(path=workdir, action="delete")
				sys.exit(1)

			except KeyboardInterrupt, e:

				logger.error('exit on user cancel.')
				directory(path=workdir, action="delete")
				sys.exit(1)

		elif '.tar.gz' == pkg_name[-7:] or '.tar.bz2' == pkg_name[-8:]:

			try:
				tf = tarfile.open(pkg_name, 'r')
				tf.extractall(workdir)
				return True
			except OSError, oserr:
				logger.error(str(oserr))
				directory(path=workdir, action="delete")
				sys.exit(1)
			except KeyboardInterrupt, e:
				logger.error('exit on user cancel.')
				directory(path=workdir, action="delete")
				sys.exit(1)

		print "is not a compressed file."

def symble_link(src_path, sym_link_path, action="create"):

	if not os.path.exists(src_path):
		print red("src directory is not exists, can't create soft link.")
		sys.exit(1)

	is_exists_sym_link = os.path.exists(sym_link_path)

	if action == "create":

		if is_exists_sym_link:

			try:
				r_file(sym_link_path, action="delete")
			except OSError, e:
				logger.error("delete link filename: %s " % (sym_link_path) + str(e))
				sys.exit(1)
		else:
			try:
				os.symlink(src_path, sym_link_path)
				logger.info("Create Sym Link Ok.")
			except OSError, e:
				logger.error("Create Sym Link : %s" % (sym_link_path) + str(e))
				sys.exit(1)

	print "your action is invalid."

def exec_command(command_list = []):
	# command_list = ['ls', '-l']
	try:
		if call(command_list) != 0:
			logger.error("exec " + ''.join(command_list)+ " error!")
			sys.exit(1)
	except OSError, oserr:
		logger.error(str(oserr))
		sys.exit(1)
	except KeyboardInterrupt, kbit:
		logger.error(str(kbit))
		sys.exit(1)
	return True

def send_http_request(url):

	try:
		request = urllib2.Request(url)
		request.add_header('User-Agent', 'Chrome')
		response = urllib2.urlopen(request)
		return response
	except urllib2.HTTPError, e:
		return "http_error"
	except Exception, e:
		logger.error(str(e))
		sys.exit(1)

#if __name__ == "__main__":
#	print send_http_request("http://10.0.0.145:8081/nexus/service/local/repositories/BiboCloudSnapshot/content/com/magima/appcenterservice/1.0.58.10-develop/appcenterservice-1.0.58.10-develop.ip")

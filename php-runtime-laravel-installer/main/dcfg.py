
import os, sys

from settings import logger, mysql_boot_script, mysql_home, tomcat_bootstrap
from resource import exec_command

class Dcfg(object):

	is_exists_boot_script = False
	do_init_system_tables = False

	state = {}

	def preVerify(self):
		# scanning mysqld processs is exists? 
		# mysql.server status ? 
		# mysql.server file is exists ? 
		# support file is exists? 
		# /etc/my.cnf exists?
		# check user exists?
		pass

	def postVerify(self):
		pass

	def exec_dcfg(self):

		# first exec support script to install system tables.
		try:
			logger.info("============MYSQL DEFAULT CONFIG===========")
			logger.info("install system db.")
			os.chdir(mysql_home)
			exec_command('./scripts/mysql_install_db --user=mysql')

			logger.info("copy boot script to correct directory.")
			exec_command('cp ' + mysql_boot_script + ' /etc/init.d/')

			# sed config
			exec_command('sed -i -e "46s/basedir=/basedir=\/opt\/magima\/mysql/g" /etc/init.d/mysql.server')

			exec_command('sed -i -e "47s/datadir=/datadir=\/opt\/magima\/mysql\/data/g" /etc/init.d/mysql.server')

			exec_command("/etc/init.d/mysql.server start")
			exec_command("/etc/init.d/mysql.server status")
			exec_command("/etc/init.d/mysql.server stop")
			logger.info("==============TOMCAT DEFAULT CONFIG==============")
			logger.info("copy tomcat bootscript to /etc/init.d/")
			exec_command("cp " + tomcat_bootstrap + " /etc/init.d/tomcat6")
			exec_command("sudo /etc/init.d/tomcat6 start")
			exec_command("sudo /etc/init.d/tomcat6 status")
			exec_command("sudo /etc/init.d/tomcat6 stop")

		except OSError , oserr:
			logger.error("os error: %s " % str(oserr))
			sys.exit(1)

		except KeyboardInterrupt, kbit:
			logger.error("cancelled by user.")
			sys.exit(1)

		except NameError, nameerr:
			logger.error("name error:" + str(nameerr))
			sys.exit(1)

		except Exception, e:
			logger.error("..." + str(sys.exc_info()[0]))
			logger.error(str(sys.exc_info()[1]))
			sys.exit(1)

#Dcfg().exec_dcfg()


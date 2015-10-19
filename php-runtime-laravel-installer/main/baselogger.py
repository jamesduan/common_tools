#!/usr/bin/env python

import logging, os, sys
import logging.handlers

class BaseLogger():

	''' logger_name :  object name of logger.
		log_filename: logs to saved in.
		logger_level: log level , DEBUG, INFO, WARN, ERROR, CRITICAL
		rotate_file_max_size: the log file max size defualt set MB.
	'''

	def __init__(self, logger_name, log_filename, logger_level,
				rotate_file_max_size):

		if type(logger_name) != type('logger'):
			print "your logger name is not valid.!"

		self.logger_name = logger_name
		self.log_filename = log_filename
		self.logger_level = logger_level
		self.rotate_file_max_size = rotate_file_max_size

	def getLogger(self):

		try:
			# setting up logger name
			logger = logging.getLogger(self.logger_name)
			# set global log level.
			logger.setLevel(self.logger_level)
			# set rotate file config
			file_rotate_handler = logging.handlers.RotatingFileHandler(self.log_filename,
											maxBytes=self.rotate_file_max_size*1024*1024,
											backupCount=5)
			# create a new handler to handle console ouput message.
			streamHandler = logging.StreamHandler()
			streamHandler.setLevel(logging.DEBUG)
			# create a formatter to describe output message format.
			formatter = logging.Formatter('%(asctime)s  %(name)s  %(levelname)s: %(message)s')
			# add formatter to handler
			file_rotate_handler.setFormatter(formatter)
			streamHandler.setFormatter(formatter)
			# add handler to logger obj
			logger.addHandler(file_rotate_handler)
			logger.addHandler(streamHandler)
			return logger
		except Exception, e:
			print "BaseLogger.getLogger throws Exception:", e
			sys.exit(1)


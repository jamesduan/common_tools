
import ConfigParser
import logging

from baselogger import BaseLogger

config_path = "../conf/properties.ini"

cfg = ConfigParser.ConfigParser()
cfg.read(config_path)

logger = BaseLogger('php_laravel',
					cfg.get('php', 'log_filename'),
					logging.DEBUG,
					500).getLogger()





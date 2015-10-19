
import installer

from settings import logger, cfg
from resource import exec_command
from colors import green, red
from usefull_character import success, error

class PHPRuntimeInstaller(installer.Installer):

	def __init__(self):
		pass

	def prepare(self):
		logger.info("step1: beging prepare func")
		logger.info("exec atomic")
		if exec_command(['bash', cfg.get('php', 'atomic_script_path')]):
			logger.info(green("exec atomic script success... ", success))

	def install(self):
		pass
	def verify(self): pass

	def run(self):
		self.prepare()

	def clean(self):
		pass

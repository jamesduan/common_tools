#!/usr/bin/env python
# encoding:utf8

import sys

from php_runtime_installer import PHPRuntimeInstaller

if __name__ == "__main__":

	try:
		PHPRuntimeInstaller().run()

	except KeyboardInterrupt, interrupt:
		logger.error("cancelled by user type Ctrl + c.")
		sys.exit(1)


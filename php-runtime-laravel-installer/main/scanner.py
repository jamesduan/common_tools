#!/usr/bin/env python

import nmap
import sys

from colors import green, red
from resource import send_http_request
from usefull_character import success, error

def getNetworkScanState(ip='', port=''):

	nm = nmap.PortScanner()
	nm.scan(ip, port)
	state_result = nm[ip].state()
	tcp_port_state = nm[ip].tcp(int(port))['state']
	return state_result, tcp_port_state

def scan_baseline_packages(file_path):

	fault_line = []
	success_line = []

	try:
		with open(file_path, 'r') as baseline:
			for line in baseline.readlines():
				response = send_http_request(line)
				if response == "http_error":
					fault_line.append(line.strip())
					print line.split('/')[-1].strip(), red(error)
				elif response.code==200:
					success_line.append(line.strip())
					print line.split('/')[-1].strip(), green(success)

		return success_line, fault_line

	except Exception, e:
		print "error", e
		sys.exit(1)

if __name__ == "__main__":
	print scan_baseline_packages('./SERVICE_URL')


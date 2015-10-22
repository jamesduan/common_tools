
import psutil

class ProcessManager(object):

	def __init__(self):
		self._process_list = psutil.get_process_list()

	def query_name(self, name):

		assert self._process_list is not None

		t_processes = []

		for process in self._process_list:
			if name in process.name():
				t_processes.append(process)
		return t_processes

print ProcessManager().query_name("bash")

#!/usr/bin/env python
# encoding:utf-8

class Operation(object):

	def getResult(self):
		pass

class OperationAdd(Operation):

	def getResult(self):
		return self.op1+self.op2

class OperationSub(Operation):

	def  getResult(self):
		return self.op1-self.op2

class OperationMul(Operation):

	def getResult(self):
		return self.op1*self.op2

class OperationDiv(Operation):

	def getResult(self):

		try:
			return self.op1 / self.op2
		except Exception, e:
			print e, "divided is can't be zero."
			return False

class OperationUndf(Operation):
	def getResult(self):
		print "operation undefined."
		return False

class OperationFactory(object):

	def __init__(self):
		self.operation = {}
		self.operation['+'] = OperationAdd()
		self.operation['-'] = OperationSub()
		self.operation['*'] = OperationMul()
		self.operation['/'] = OperationDiv()

	def createOperation(self, operator):
		if operator in self.operation:
			return self.operation[operator]
		else:
			return OperationUndf()

if __name__ == "__main__":
	operation = OperationFactory().createOperation('/')
	operation.op1 = 1
	operation.op2 = 2.531231
	print operation.getResult()


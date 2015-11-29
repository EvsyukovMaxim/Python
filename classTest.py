import datetime

class Factory():

	def factory(name):

		if name == "odd":
			myoddClass = oddClass()
			return myoddClass

		elif name == "any":
			myanyClass = anyClass()
			return myanyClass

		elif name == "even":
			myevenClass = evenClass()
			return myevenClass
		else:
			raise AttributeError('This nonExisting object and raising especial AttributeError')

	factory = staticmethod(factory)


class oddClass():

	def process(self):
		print "ODD now!"

class evenClass():

	def process(self):
		print "SOME EVENt happend!!!"

class anyClass():

	def process(self):
		print "CAN'T wait for ANY!"


		

oddClass = Factory.factory("odd")
oddClass.process()

evenClass = Factory.factory("even")
evenClass.process()

anyClass = Factory.factory("any")
anyClass.process()


try:
	nonExists = Factory.factory("SHOOT")
	nonExists.process()
except AttributeError as err:
	print err.args


now = datetime.datetime.now()
print "Current date and time using strftime:"
print now.strftime("%Y-%m-%d %H:%M")

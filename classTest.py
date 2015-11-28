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
			print "I do not know what is this"
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

#Factory.factory("SHOOT")

#nonExists = Factory.factory("smth")
#nonExists.process()
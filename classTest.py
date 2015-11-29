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
			try:
				raise ValueError('Exception masage')
			except ValueError as err:
				print(err.args)
				print "Usual print via Else"
			
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

## Сделай так, чтобы код внизу выполнился

# Now I'm trying to create a non-existing class name
nonExists = Factory.factory("SHOOT")
# And now I'm trying to call process() on non-existing bject
nonExists.process()

## Далее обычный код, он должен выполниться 

now = datetime.datetime.now()
print "Current date and time using strftime:"
print now.strftime("%Y-%m-%d %H:%M")

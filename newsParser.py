import sys

if len(sys.argv) != 2:
	print "!!! Attention!!! Please, put exactly one argument!"
	sys.exit()

newsSource = sys.argv[1]

class NewsStrategyException(Exception):
	pass

class NewsStrategy():
	@staticmethod
	def getStrategy(newsSource):
		if newsSource == 'Village':
			myVillageStrategy = VillageStrategy()
			return myVillageStrategy
		elif newsSource == 'Afisha':
			myAfishaStrategy = AfishaStrategy()
			return myAfishaStrategy
		else:
			raise NewsStrategyException('Would you be kind dont put any other stuFf in here !!!')


class VillageStrategy():
	def parse(self):
			
		newObject1 = ("http://www.the-village.ru/")
		newObject2 = ("http://www.the-village.ru/news")
		newObject3 = ("http://www.the-village.ru/village/city/moscow-morning/227313-3-dekabrya")
		newObject4 = ("http://www.the-village.ru/village/city/people/227157-scientists")
		newObject5 = ("http://ads.adfox.ru/5024/goLink?pr=cvpfmkj&p5=defwo&p1=ccsi&p2=cbf")

		villageList = []
		villageList.append(newObject1)
		villageList.append(newObject2)
		villageList.append(newObject3)
		villageList.append(newObject4)
		villageList.append(newObject5)

		for villageLink in villageList:
			print villageLink

class AfishaStrategy():
	def parse(self):

		newObject1 = ("http://www.afisha.ru/")
		newObject2 = ("http://www.afisha.ru/novosibirsk/cinema/")
		newObject3 = ("http://www.afisha.ru/novosibirsk/concerts/")
		newObject4 = ("http://www.afisha.ru/novosibirsk/exhibitions/")
		newObject5 = ("http://www.afisha.ru/novosibirsk/theatre/")

		afishaList = []
		afishaList.append(newObject1)
		afishaList.append(newObject2)
		afishaList.append(newObject3)
		afishaList.append(newObject4)
		afishaList.append(newObject5)

		for afishaLink in afishaList:
			print afishaLink

#VillageStrategy = NewsStrategy.getStrategy(newsSource)
#VillageStrategy.parse()

try:
	newsSource != 'Afisha', 'Village'
	VillageStrategy = NewsStrategy.getStrategy(newsSource)
	VillageStrategy.parse()
except NewsStrategyException as err:
	print err.args
	sys.exit()
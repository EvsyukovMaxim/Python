# -*- coding: utf-8 -*-

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

		villageList = []
		villageList.append(myNewsObject)
		return villageList

		
class AfishaStrategy():
	def parse(self):

		afishaList = []
		afishaList.append(myNewsObject1)
		return afishaList


class NewsObject():
	title = ''
	preview = ''	
myNewsObject = NewsObject()
myNewsObject.title = "Moscow morning!"
myNewsObject.preview = "fourth december"


class NewsObject1():
	title = ''
	preview = ''
myNewsObject1 = NewsObject1()
myNewsObject1.title = u"Шпионский Мост!"
myNewsObject1.preview = u"Исторический триллер про холодную войну от Стивена Спилберга"


try:
	VillageStrategy = NewsStrategy.getStrategy(newsSource)
	VillageStrategy.parse()
except NewsStrategyException as err:
	print err.args
	sys.exit()
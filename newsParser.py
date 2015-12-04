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

		myNewsObject = NewsObject()
		myNewsObject.title = "Moscow vs Batman"
		myNewsObject.preview = "Spider-Man was seen in Novosibirsk"
		villageList = []
		villageList.append(myNewsObject)
		return villageList

		
class AfishaStrategy():
	def parse(self):

		myNewsObject = NewsObject()
		myNewsObject.title = "There was Hitler cought under the bridge"
		myNewsObject.preview = "Hitler got a tail!!!"
		afishaList = []
		afishaList.append(myNewsObject)
		return afishaList


class NewsObject():
	title = ''
	preview = ''
NewsObject.title = "Moscow morning!"
NewsObject.preview = "fourth december"


try:
	VillageStrategy = NewsStrategy.getStrategy(newsSource)
	VillageStrategy.parse()
except NewsStrategyException as err:
	print err.args
	sys.exit()
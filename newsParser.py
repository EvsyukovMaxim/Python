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
		myNewsObject1 = NewsObject()
		myNewsObject1.title = "mosmosmos"
		myNewsObject1.preview = "spispispis"
		myNewsObject2 = NewsObject()
		myNewsObject2.title = "vilvilvil"
		myNewsObject2.preview = "vilagevilagevilage"
		villageList = []
		villageList.append(myNewsObject)
		villageList.append(myNewsObject1)
		villageList.append(myNewsObject2)
		return villageList

		
class AfishaStrategy():
	def parse(self):

		myNewsObject = NewsObject()
		myNewsObject.title = "There was Hitler cought under the bridge"
		myNewsObject.preview = "Hitler got a tail!!!"
		myNewsObject1 = NewsObject()
		myNewsObject1.title = "blabla"
		myNewsObject1.preview = "tratata"
		myNewsObject2 = NewsObject()
		myNewsObject2.title = "tururu"
		myNewsObject2.preview = "klaklakla"
		afishaList = []
		afishaList.append(myNewsObject)
		afishaList.append(myNewsObject1)
		afishaList.append(myNewsObject2)
		return afishaList

class NewsObject():
	title = ''
	preview = ''


try:
	Strategy = NewsStrategy.getStrategy(newsSource)
	var = Strategy.parse()
	for news in var:
		print news.title
		print news.preview
except NewsStrategyException as err:
	print err.args
	sys.exit()
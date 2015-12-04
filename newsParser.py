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
		villageList.append(myNewsObject.title)
		villageList.append(myNewsObject.preview)

		for villageLink in villageList:
			print villageLink

class AfishaStrategy():
	def parse(self):

		newsObject1 = ("http://www.afisha.ru/")
		newsObject2 = ("http://www.afisha.ru/novosibirsk/cinema/")
		newsObject3 = ("http://www.afisha.ru/novosibirsk/concerts/")
		newsObject4 = ("http://www.afisha.ru/novosibirsk/exhibitions/")
		newsObject5 = ("http://www.afisha.ru/novosibirsk/theatre/")

		afishaList = []
		afishaList.append(newsObject1)
		afishaList.append(newsObject2)
		afishaList.append(newsObject3)
		afishaList.append(newsObject4)
		afishaList.append(newsObject5)

		for afishaLink in afishaList:
			print afishaLink

class NewsObject():
	title = ''
	preview = ''
myNewsObject = NewsObject
myNewsObject.title = u"Утром Москвы!"
myNewsObject.preview = u'УТРО В МОСКВЕ - 4 декабря'


try:
	VillageStrategy = NewsStrategy.getStrategy(newsSource)
	VillageStrategy.parse()
except NewsStrategyException as err:
	print err.args
	sys.exit()
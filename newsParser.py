# -*- coding: utf-8 -*-

import sys
import urllib2
import re

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

		villageRequest = urllib2.Request('http://www.the-village.ru/village/city')
		villageResponse = urllib2.urlopen(villageRequest)
		the_page = villageResponse.read()
		matchObj = re.findall(r'<h2 class="post-title">(.*?)</h2>', the_page, re.DOTALL)

		i = 0

		for p in matchObj:
			i = i+1
			myNewsObject = NewsObject()
			myNewsObject.title = p
			villageList.append(myNewsObject)
			if i > 10:
				break

		return villageList

		
class AfishaStrategy():
	def parse(self):

		afishaList = []

		afishaRequest = urllib2.Request('http://www.afisha.ru/novosibirsk/cinema/')
		afishaResponse = urllib2.urlopen(afishaRequest)
		the_page = afishaResponse.read()
		matchObj = re.findall(r'<p class="m-margin-btm-min">(.*?)</p>', the_page, re.DOTALL)

		i = 0

		for p in matchObj:
			i = i+1
			myNewsObject = NewsObject()
			myNewsObject.title = p
			afishaList.append(myNewsObject)
			if i > 6:
				break

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
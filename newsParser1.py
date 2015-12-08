# -*- coding: utf-8 -*-
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            print "     attr:", attr
    def handle_data(self, data):
        print "Data     :", data

parser = MyHTMLParser()

parser.feed('<a class="fn permalink" href="http://www.afisha.ru/movie/216037/" title="">В сердце моря</a>')
parser.feed('<a class="fn permalink" href="http://www.afisha.ru/movie/222499/" title="">Он — дракон</a>')
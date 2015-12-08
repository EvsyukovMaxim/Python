# -*- coding: utf-8 -*-
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

class MyHTMLParser(HTMLParser):
    #def handle_starttag(self, tag, attrs):
     #   print "Encountered a start tag:", tag
    #def handle_endtag(self, tag):
    #    print "Encountered an end tag :", tag
    def handle_data(self, data):
        print "Encountered some data  :", data

parser = MyHTMLParser()

parser.feed('<a class="fn permalink" href="http://www.afisha.ru/movie/216037/" title="">В сердце моря</a>')
parser.feed('<a class="fn permalink" href="http://www.afisha.ru/movie/222499/" title="">Он — дракон</a>')
#!/usr/bin/python

import urllib2, re

class Weather:
   
	def __init__(self):
		self.key = "204df492f224d7c8"
	
	def main(self):
		self.state = raw_input("Enter State Initials: ")
		print "\n"
		city = raw_input("Enter City: ")
		self.checkName(city)
	
	def checkName(self, city):
		if " " in city: #Check if name has spaces
			self.city = city.replace (" ", "_") #Swap Spaces with underscores for URL use
			self.grabPage()
		else:
			self.grabPage()
	
	def grabPage(self):
		url = "http://api.wunderground.com/api/%s/conditions/q/%s/%s.json" % (self.key, self.state, self.city)
		try:
			request = urllib2.Request(url)
			self.page = urllib2.urlopen(request).read()
			self.grab_F()
		except urllib2.HTTPError, error:
			print "Error Loading Page"
			contents = error.read()

	def grab_F(self):
		FahrenheitLine = self.page.split(",")
		FahrenheitParse = FahrenheitLine[45].split(":")
		print "It is currently %s in %s, %s" % (FahrenheitParse[1], self.city, self.state)
		self.grab_C()
		
	def grab_C(self):
		CelsiusLine = self.page.split(",")
		CelsiusParse = CelsiusLine[46].split(":")
		print "It is currently %s in %s, %s" % (CelsiusParse[1], self.city, self.state)

if __name__ == "__main__":
        ObjW = Weather()
        ObjW.main()

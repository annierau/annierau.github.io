''''
This code takes values calulated and puts them into a variable called f which consists of an baseURL which is specific for your project
since it is defined by the api_key. The variable f is the link including the new value that inserts a new measurment point to your
thingspeak channel. the f.read() command opens this link and the f.close command closes it. The variable that is transmitted can be
changed as you want to. In this case it calculates Fibonnaci Numbers.
''''


import sys
import RPi.GPIO as GPIO
from time import sleep
import urllib2

a = 0
b = 1
c = 0
baseURL = 'http://api.thingspeak.com/update?api_key=PG5DXW4ILDR1ZG12&field1='
while(a < 1000):
	print a
	f = urllib2.urlopen(baseURL +str(a))
	f.read()
	f.close()
	sleep(5)
	c = a
	a = a + b
	b = c
print "Program has ended"

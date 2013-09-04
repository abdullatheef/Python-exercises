# Program to print external ip address of the machine

import urllib
import json
print 'Loading.....'
print json.load(urllib.urlopen('http://httpbin.org/get'))['origin']


#!/usr/bin/env python

import urllib,json

TMPPATH = '/Users/greggt/Library/Caches/Cleanup At Startup'
htmlheader = '''
<!DOCTYPE html>
<html>
<head>
    <title>Reddit?</title>
</head>
<body>
'''
htmlfooter = '''
</body>
</html>
'''

class RedditFetcher(urllib.FancyURLopener):
    version = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"

getter = RedditFetcher()

a = getter.open('http://www.reddit.com/r/programming/.json')

try:
    j = json.load(a)['data']
except KeyError:
    print "Fail."
    exit()
storieslist = j['children']
htmlstring = ''
for x in storieslist:
    title = x['data']['title']
    URL = x['data']['url']
    htmlstring += '<p><a href="'+ URL.encode("utf-8", "ignore") + '">' + title.encode("utf-8", "ignore") + '</a></p>'

filestring = htmlheader + htmlstring + htmlfooter

f = open(TMPPATH + '/reddit.html', 'w')
f.write(filestring)
f.close()

# Author: LJF
# Time: 2017/04/16
# Coding: utf-8

import urllib  
import sys
import http.cookiejar 
import string
import re

# Get the page after posting form data
def GetPageAfterPostData(hosturl, posturl, postDataStr, headers):

	# Save the cookie to prepare for other pages after logging in
	cookie_filename = 'cgcSimsCookie.txt'
	cookie = http.cookiejar.MozillaCookieJar(cookie_filename)   
	handler  = urllib.request.HTTPCookieProcessor(cookie)               
	opener = urllib.request.build_opener(handler) 
	urllib.request.install_opener(opener)

	# Open the main page and set postdata
	host = urllib.request.urlopen(hosturl)
	postdata = urllib.parse.urlencode(postDataStr)
	postdata = postdata.encode('gb2312') 

	# Opener opens the request
	req = urllib.request.Request(hosturl, postdata, headers)
	try:
	    res = opener.open(req)
	    page = res.read()
	except urllib.error.URLError as e:
	    print(e.code, ':', e.reason)

	# Save the cookie to the cgcSimsCookie.txt
	cookie.save(ignore_discard=True, ignore_expires=True)  
	print(cookie)	
	for item in cookie:
	    print('Name = ' + item.name)
	    print('Value = ' + item.value)
    # post_req = urllib.request.Request(posturl, headers)
    # post_res = opener.open(get_request)
   
	# Post form data to the server
	res = urllib.request.urlopen(hosturl, postdata)	
	print(res.status, res.reason)
	if(res.status != 200):
	    exit()
	html = res.read()
	return html

# Save the text to the path
def SaveText(path, text):
	# Save_path's file unnecessary to be exist 
	save_path = path
	f_obj = open(save_path,'wb') 
	f_obj.write(text)
	print("Save successfully.")

# Set url and postDataStr
hosturl = "******"
posturl = "******"
user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
headers = {'User-Agent': user_agent, 'Connection': 'keep-alive'}
postDataStr = {'buildingName': '', 'roomName': '', 'buildingId':''}
html = GetPageAfterPostData(hosturl, posturl, postDataStr, headers)

# Set path and save html
path = "******"
SaveText(path, html)

# To be continued...


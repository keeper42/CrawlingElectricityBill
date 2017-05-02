# Author: LJF
# Coding: UTF-8
# The version of python: 3.5
# Created time: from 2017/04/29 to 2017/04/30
# This is a general function file

import sys
import urllib
import http.cookiejar
import re
import pymysql
from pyquery import PyQuery as pq

#
#
# Start to define the function
# 
# 
# Get the html file for the page
# Enter url and headers to return the html file
def GetHtmlFileOfUrl(url):
	res = urllib.request.urlopen(url)	
	if(res.status != 200):
	    exit()
	html = res.read().decode('gb2312')
	return html

# Get the page after posting form data
# Enter url, postdata and headers to return the html file
def GetPageAfterPostData(url, postDataObj, headers):

	# Save the cookie to prepare for other pages after logging in
	cookie = http.cookiejar.MozillaCookieJar()
	handler  = urllib.request.HTTPCookieProcessor(cookie)               
	opener = urllib.request.build_opener(handler)  
	urllib.request.install_opener(opener)

	# Open the main page and set postdata
	postdata = urllib.parse.urlencode(postDataObj)
	postdata = postdata.encode('gb2312') 

	# Opener opens the request
	req = urllib.request.Request(url, postdata, headers)
	try:
	    res = opener.open(req)
	    page = res.read()
	except urllib.error.URLError as e:
	    print(e.code, ':', e.reason)
	
	# Post form data to the server
	res = urllib.request.urlopen(url, postdata)	
	if(res.status != 200):
	    # exit()
	    return -1
	else:
		html = res.read()
		return html

# Save the text to the path
def SaveText(path, text):
	# Save_path's file unnecessary to be exist 
	save_path = path
	text = text.encode()
	f_obj = open(save_path,'wb') 
	f_obj.write(text)

# Get roomId from the login.do page
# Enter buildingId and roomName to return roomId
def GetRoomIdFromTheLogindoPage(postDataObj, headers):
	
	# Set url and headers
	hosturl = "http://192.168.84.3:9090/cgcSims/" 
	loginUrl = hosturl + "login.do"
	html = GetPageAfterPostData(loginUrl, postDataObj, headers)
	htmlDecode = html.decode('gb2312')
	source = pq(htmlDecode)
	inputField = source("input[name='roomId']")
	if(len(inputField) > 0):
		for room in inputField:
			roomId = room.value
		return roomId
	else:
		return "-1"

# Store the information of the building into the database
def StoreBuildingInformation(url, cursor, connect):
	html = GetHtmlFileOfUrl(url)
	source = pq(html)
	option = source("option")
	pos = 4
	if(url == "http://192.168.84.3:9090/cgcSims/login.do?task=station&client=172.21.101.11"):
		sql = "INSERT IGNORE INTO `xili_building` (`xili_building_id`,`building_name`) VALUES (%s, %s)"
	elif(url == "http://192.168.84.3:9090/cgcSims/login.do?task=station&client=192.168.84.110"):
		pos += 9
		sql = "INSERT IGNORE INTO `south_building` (`south_building_id`,`building_name`) VALUES (%s, %s)"
	elif(url == "http://192.168.84.3:9090/cgcSims/login.do?task=station&client=192.168.84.1"):
		sql = "INSERT IGNORE INTO `north_building` (`north_building_id`,`building_name`) VALUES (%s, %s)"
	for i in range(pos, len(option)):
		buildingId = int(pq(option[i]).val())
		buildingName = str(pq(option[i]).text())
		data = (buildingId, buildingName)
		cursor.execute(sql, data)
		connect.commit()
#
#
# End define the function
#
#

# Author: LJF
# Coding: UTF-8
# The version of python: 3.5
# Created time: from 2017/04/29 to 2017/05/01
# This is a crawling function file

import io
import sys
import re
import pymysql
import time
import GeneralFunction
from pyquery import PyQuery as pq

#
#
# Start to define the function
# 
# 
# Change the default encoding for standard output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

# Post the form data to the selectList.do page
# And store the electricity bill into the database
def PostDataToTheSelectlistPage(url, postDataObj, headers, cursor, connect):

	# Set url and headers
	hosturl = "http://192.168.84.3:9090/cgcSims/" 
	selectListUrl = hosturl + "selectList.do"
	html = GeneralFunction.GetPageAfterPostData(selectListUrl, postDataObj, headers)

	# Regular match for electricity bill
	pattern = re.compile(r'\d{1,5}\.\d{1,2}')

	# Analyze html and extract electricity bills
	htmlStr = str(html)
	electricityBill = pattern.findall(htmlStr)
	length = len(electricityBill)
	# print(length)
	
	# Analyze html and extract electricity bills to make electricityBill2 as a candidate
	htmlDecode = html.decode('gb2312')
	source = pq(htmlDecode)
	td = source('td')
	tdStr = str(pq(td).text())
	electricityBill2 = pattern.findall(tdStr)
	length2 = len(electricityBill2)
	if(length2 >= 4):
		for i in range(length2 - 4, length2 - 1):
			bill2 = electricityBill2[i]

	# Store the electricity bill information into the database
	if(url == "http://192.168.84.3:9090/cgcSims/login.do?task=station&client=172.21.101.11"):

		if(length >= 4):
			sql = "INSERT IGNORE INTO `xili_room_bill` (`room_id`,`xili_building_id`,`room_name`,`type`,`remain`,`total_use`,`total_buy`) VALUES (%d, %d, %d, %d, %f, %f, %f)"
			data = (int(postDataObj['roomId']), int(postDataObj['buildingId']), int(postDataObj['roomName']), int(postDataObj['type']), float(electricityBill[length - 4]), float(electricityBill[length - 3]), float(electricityBill[length - 2]))
			cursor.execute(sql % data)

		else:
			sql = "INSERT IGNORE INTO `xili_room_bill` (`room_id`,`xili_building_id`,`room_name`,`type`) VALUES (%d, %d, %d, %d)"
			data = (int(postDataObj['roomId']), int(postDataObj['buildingId']), int(postDataObj['roomName']), int(postDataObj['type']))
			cursor.execute(sql % data)

		connect.commit()
		print("Insert successfully.")

	elif(url == "http://192.168.84.3:9090/cgcSims/login.do?task=station&client=192.168.84.110"):

		if(length >= 4):
			sql = "INSERT IGNORE INTO `south_room_bill` (`room_id`,`south_building_id`,`room_name`,`type`,`remain`,`total_use`,`total_buy`) VALUES (%d, %d, %d, %d, %f, %f, %f)"
			data = (int(postDataObj['roomId']), int(postDataObj['buildingId']), int(postDataObj['roomName']), int(postDataObj['type']), float(electricityBill[length - 4]), float(electricityBill[length - 3]), float(electricityBill[length - 2]))
			cursor.execute(sql % data)
		
		else:
			sql = "INSERT IGNORE INTO `south_room_bill` (`room_id`,`south_building_id`,`room_name`,`type`) VALUES (%d, %d, %d, %d)"
			data = (int(postDataObj['roomId']), int(postDataObj['buildingId']), int(postDataObj['roomName']), int(postDataObj['type']))
			cursor.execute(sql % data)

		connect.commit()
		print("Insert successfully.")

	elif(url == "http://192.168.84.3:9090/cgcSims/login.do?task=station&client=192.168.84.1" + "0"):

		if(length >= 4):
			sql = "INSERT IGNORE INTO `zhaiqu_room_bill` (`room_id`,`north_building_id`,`room_name`,`type`,`remain`,`total_use`,`total_buy`) VALUES (%d, %d, %d, %d, %f, %f, %f)"
			data = (int(postDataObj['roomId']), int(postDataObj['buildingId']), int(postDataObj['roomName']), int(postDataObj['type']), float(electricityBill[length - 4]), float(electricityBill[length - 3]), float(electricityBill[length - 2]))
			cursor.execute(sql % data)

		else:
			sql = "INSERT IGNORE INTO `zhaiqu_room_bill` (`room_id`,`north_building_id`,`room_name`,`type`) VALUES (%d, %d, %d, %d)"
			data = (int(postDataObj['roomId']), int(postDataObj['buildingId']), int(postDataObj['roomName']), int(postDataObj['type']))
			cursor.execute(sql % data)

		connect.commit()
		print("Insert successfully.")

	elif(url == "http://192.168.84.3:9090/cgcSims/login.do?task=station&client=192.168.84.1" + "1"):

		if(length >= 4):
			sql = "INSERT IGNORE INTO `southwest_room_bill` (`room_id`,`north_building_id`,`room_name`,`type`,`remain`,`total_use`,`total_buy`) VALUES (%d, %d, %d, %d, %f, %f, %f)"
			data = (int(postDataObj['roomId']), int(postDataObj['buildingId']), int(postDataObj['roomName']), int(postDataObj['type']), float(electricityBill[length - 4]), float(electricityBill[length - 3]), float(electricityBill[length - 2]))
			cursor.execute(sql % data)

		else:
			sql = "INSERT IGNORE INTO `southwest_room_bill` (`room_id`,`north_building_id`,`room_name`,`type`) VALUES (%d, %d, %d, %d)"
			data = (int(postDataObj['roomId']), int(postDataObj['buildingId']), int(postDataObj['roomName']), int(postDataObj['type']))
			cursor.execute(sql % data)

		connect.commit()
		print("Insert successfully.")

	elif(url == "http://192.168.84.3:9090/cgcSims/login.do?task=station&client=192.168.84.1" + "2"):

		if(length >= 4):
			sql = "INSERT IGNORE INTO `qiaoyuan_room_bill` (`room_id`,`north_building_id`,`room_name`,`type`,`remain`,`total_use`,`total_buy`) VALUES (%d, %d, %d, %d, %f, %f, %f)"
			data = (int(postDataObj['roomId']), int(postDataObj['buildingId']), int(postDataObj['roomName']), int(postDataObj['type']), float(electricityBill[length - 4]), float(electricityBill[length - 3]), float(electricityBill[length - 2]))
			cursor.execute(sql % data)

		else:
			sql = "INSERT IGNORE INTO `qiaoyuan_room_bill` (`room_id`,`north_building_id`,`room_name`,`type`) VALUES (%d, %d, %d, %d)"
			data = (int(postDataObj['roomId']), int(postDataObj['buildingId']), int(postDataObj['roomName']), int(postDataObj['type']))
			cursor.execute(sql % data)

		connect.commit()
		print("Insert successfully.")

#
# Crawl the electricity bill information of all campuses
#
# Crawl the xili campus' electricity bill information and store it into the database
def CrawlElectricityInfoOfXiliCampus(url, headers, cursor, connect):

	# Set up three arrays of buildingId, floors and rooms so that traversal all of rooms
	buildingIdList = [10057, 10934, 10935]
	floorNum = [25, 10, 12]
	roomNum = [40, 50, 30]

	# Start traversing
	count = 0
	for pos in range(0, 3):
		buildingId = buildingIdList[pos]
		for i in range(3, floorNum[pos]):
			for j in range(1, roomNum[pos]):
				if(0 <= j <= 9):
					roomName = str(i) + '0' + str(j)
				else:
					roomName = str(i) + str(j)
				postDataStr1 = "{'buildingName': '', 'buildingId':'" + str(buildingId) + "', 'roomName': '" + roomName +"', 'client': '172.21.101.11'}"
				postDataObj1 = eval(postDataStr1)
				# Get roomId from the login.do page
				roomId = GeneralFunction.GetRoomIdFromTheLogindoPage(postDataObj1, headers)
				print(buildingId, roomName, roomId)
				if(roomId != "-1"):
					count += 1
					today = time.strftime("%Y-%m-%d")
					postDataStr2 = "{'beginTime': '" + str(today) + "', 'endTime': '" + str(today) + "', 'type': '2', 'roomId':'" + roomId + "', 'roomName': '" + roomName + "', 'buildingId': '" + str(buildingId) + "', 'client': '172.21.101.11'}";
					postDataObj2 = eval(postDataStr2)
					# Post the form data to the selectList.do page
					PostDataToTheSelectlistPage(url, postDataObj2, headers, cursor, connect)
	print(count)

# Crawl the south campus' electricity bill information and store it into the database
def CrawlElectricityInfoOfSouthCampus(url, headers, cursor, connect):

	# Set up three arrays of buildingId, floors and rooms so that traversal all of rooms
	buildingIdList = [6875, 6876, 6877, 6878, 7119, 7828, 8240, 8241, 8242]
	floorStart = [3, 3, 3, 3, 9, 9, 7, 11, 15]
	floorEnd = [9, 18, 9, 7, 18, 18, 11, 15, 18]
	roomNum = [36, 17, 40, 55, 36, 40, 55, 55, 55]

	# Start traversing
	count = 0
	for pos in range(0, 9):
		buildingId = buildingIdList[pos]
		for i in range(floorStart[pos], floorEnd[pos]):
			for j in range(1, roomNum[pos]):	
				if(0 <= j <= 9):
					roomName = str(i) + '0' + str(j)
				else:
					roomName = str(i) + str(j)
				postDataStr1 = "{'buildingName': '', 'buildingId':'" + str(buildingId) + "', 'roomName': '" + roomName +"', 'client': '192.168.84.110'}"
				postDataObj1 = eval(postDataStr1)
				# Get roomId from the login.do page
				roomId = GeneralFunction.GetRoomIdFromTheLogindoPage(postDataObj1, headers)
				print(buildingId, roomName, roomId)
				if(roomId != "-1"):
					count += 1
					today = time.strftime("%Y-%m-%d")
					postDataStr2 = "{'beginTime': '" + str(today) + "', 'endTime': '" + str(today) + "', 'type': '2', 'roomId':'" + roomId + "', 'roomName': '" + roomName + "', 'buildingId': '" + str(buildingId) + "', 'client': '192.168.84.110'}";
					postDataObj2 = eval(postDataStr2)
					# Post the form data to the selectList.do page
					PostDataToTheSelectlistPage(url, postDataObj2, headers, cursor, connect)	
	print(count)

# Crawl the north campus' electricity bill information and store it into the database
def CrawlElectricityInfoOfNorthCampus(url, headers, cursor, connect, area):

	# Set zhaiquBuildingIdList, southwestBuildingIdList and qiaoyuanBuildingIdList
	zhaiquBuildingIdList = [54, 55, 56, 57, 58, 59, 60, 61, 5374, 5375, 5376, 5377]
	southwestBuildingIdList = [63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77]
	qiaoyuanBuildingIdList = [6121, 6122, 6363, 6364, 6875, 6876, 6877, 6878, 7724, 7725]

	# Set up three arrays of buildingId, floors and rooms so that traversal all of rooms
	buildingIdList = []
	if(area == 0):
		buildingIdList.extend(zhaiquBuildingIdList)
		posNum = 12
		floorStart = [1, 1, 1, 1, 1, 1, 1, 1, 9, 2, 9, 2]
		floorEnd = [9, 9, 7, 7, 7, 7, 7, 7, 12, 9, 16, 9]
		roomNum = [16, 16, 16, 16, 16, 20, 32, 28, 35, 35, 38]

	elif(area == 1):
		buildingIdList.extend(southwestBuildingIdList)
		posNum = 14
		floorStart = [1] * 14
		floorEnd = [6, 6, 8, 7, 7, 8, 8, 8, 8, 8, 13, 8, 8, 8, 8]
		roomNum = [28, 30, 18, 18, 18, 18, 18, 13, 18, 13, 22, 18, 30, 34, 20]

	elif(area == 2):
		buildingIdList.extend(qiaoyuanBuildingIdList)
		posNum = 10
		floorStart = [1, 1, 11, 11, 2, 11, 2, 11, 2, 11]
		floorEnd = [11, 11, 13, 13, 11, 21, 11, 21, 11, 21]
		roomNum = [25] * 10

	# Start traversing
	count = 0
	for pos in range(0, posNum):
		buildingId = buildingIdList[pos]
		for i in range(floorStart[pos], floorEnd[pos]):
			for j in range(1, roomNum[pos]):
				if(0 <= j <= 9):
					roomName = str(i) + '0' + str(j)
				else:
					roomName = str(i) + str(j)
				postDataStr1 = "{'buildingName': '', 'buildingId':'" + str(buildingId) + "', 'roomName': '" + roomName +"', 'client': '192.168.84.1'}"
				postDataObj1 = eval(postDataStr1)
				# Get roomId from the login.do page
				roomId = GeneralFunction.GetRoomIdFromTheLogindoPage(postDataObj1, headers)
				print(buildingId, roomName, roomId)
				if(roomId != "-1"):
					count += 1
					today = time.strftime("%Y-%m-%d")
					postDataStr2 = "{'beginTime': '" + str(today) + "', 'endTime': '" + str(today) + "', 'type': '2', 'roomId':'" + roomId + "', 'roomName': '" + roomName + "', 'buildingId': '" + str(buildingId) + "', 'client': '192.168.84.1'}";
					postDataObj2 = eval(postDataStr2)
					# Post the form data to the selectList.do page
					PostDataToTheSelectlistPage(url + str(area), postDataObj2, headers, cursor, connect)
	print(count)

#
#
# End define the function
#
#

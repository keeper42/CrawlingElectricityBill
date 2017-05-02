# Author: LJF
# Coding: UTF-8
# The version of python: 3.5
# Created time: from 2017/05/02
# This function just a test about thread

import datetime
import threading
import pymysql
import Database
import CrawlingFunction
from time import ctime, sleep

# Connect to the database
connect = Database.connect

# Set the cursor
cursor = connect.cursor()

# Set headers 
user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
headers = {'User-Agent': user_agent, 'Connection': 'keep-alive'}

# Set url
baseUrl = "http://192.168.84.3:9090/cgcSims/login.do?task=station&client="
northCampusUrl = baseUrl + "192.168.84.1"
southCampusUrl = baseUrl + "192.168.84.110"
xiliCampusUrl = baseUrl + "172.21.101.11"

# Start the timer
start = datetime.datetime.now()

postDataObj1 = { 'beginTime': '2017-05-02', 'endTime': '2017-05-02', 'type': '2', 'roomId':'10198', 'roomName': '710', 'buildingId': '10057', 'client': '172.21.101.11'}
postDataObj2 = { 'beginTime': '2017-05-02', 'endTime': '2017-05-02', 'type': '2', 'roomId':'7387', 'roomName': '508', 'buildingId': '6876', 'client': '192.168.84.110'}
postDataObj3 = { 'beginTime': '2017-05-02', 'endTime': '2017-05-02', 'type': '2', 'roomId':'6227', 'roomName': '606', 'buildingId': '6121', 'client': '192.168.84.1'}
postDataObj4 = { 'beginTime': '2017-05-02', 'endTime': '2017-05-02', 'type': '2', 'roomId':'10198', 'roomName': '710', 'buildingId': '10057', 'client': '172.21.101.11'}
postDataObj5 = { 'beginTime': '2017-05-02', 'endTime': '2017-05-02', 'type': '2', 'roomId':'7387', 'roomName': '508', 'buildingId': '6876', 'client': '192.168.84.110'}
postDataObj6 = { 'beginTime': '2017-05-02', 'endTime': '2017-05-02', 'type': '2', 'roomId':'6227', 'roomName': '606', 'buildingId': '6121', 'client': '192.168.84.1'}
postDataObj7 = { 'beginTime': '2017-05-02', 'endTime': '2017-05-02', 'type': '2', 'roomId':'10198', 'roomName': '710', 'buildingId': '10057', 'client': '172.21.101.11'}
postDataObj8 = { 'beginTime': '2017-05-02', 'endTime': '2017-05-02', 'type': '2', 'roomId':'7387', 'roomName': '508', 'buildingId': '6876', 'client': '192.168.84.110'}
postDataObj9 = { 'beginTime': '2017-05-02', 'endTime': '2017-05-02', 'type': '2', 'roomId':'6227', 'roomName': '606', 'buildingId': '6121', 'client': '192.168.84.1'}

CrawlingFunction.PostDataToTheSelectlistPage(xiliCampusUrl, postDataObj1, headers, cursor, connect)
CrawlingFunction.PostDataToTheSelectlistPage(southCampusUrl, postDataObj2, headers, cursor, connect)
CrawlingFunction.PostDataToTheSelectlistPage(northCampusUrl + "2", postDataObj3, headers, cursor, connect)
CrawlingFunction.PostDataToTheSelectlistPage(xiliCampusUrl, postDataObj4, headers, cursor, connect)
CrawlingFunction.PostDataToTheSelectlistPage(southCampusUrl, postDataObj5, headers, cursor, connect)
CrawlingFunction.PostDataToTheSelectlistPage(northCampusUrl + "2", postDataObj6, headers, cursor, connect)
CrawlingFunction.PostDataToTheSelectlistPage(xiliCampusUrl, postDataObj7, headers, cursor, connect)
CrawlingFunction.PostDataToTheSelectlistPage(southCampusUrl, postDataObj8, headers, cursor, connect)
CrawlingFunction.PostDataToTheSelectlistPage(northCampusUrl + "2", postDataObj9, headers, cursor, connect)

# Middle timer
mid = datetime.datetime.now()
print("The program is time consuming: " + str(mid - start))

threads = []
thread1 = threading.Thread(target = CrawlingFunction.PostDataToTheSelectlistPage, args = (xiliCampusUrl, postDataObj1, headers, cursor, connect))
threads.append(thread1)
thread2 = threading.Thread(target = CrawlingFunction.PostDataToTheSelectlistPage, args = (southCampusUrl, postDataObj2, headers, cursor, connect))
threads.append(thread2)
thread3 = threading.Thread(target = CrawlingFunction.PostDataToTheSelectlistPage, args = (northCampusUrl + "2", postDataObj3, headers, cursor, connect))
threads.append(thread3)
thread4 = threading.Thread(target = CrawlingFunction.PostDataToTheSelectlistPage, args = (xiliCampusUrl, postDataObj4, headers, cursor, connect))
threads.append(thread4)
thread5 = threading.Thread(target = CrawlingFunction.PostDataToTheSelectlistPage, args = (southCampusUrl, postDataObj5, headers, cursor, connect))
threads.append(thread5)
thread6 = threading.Thread(target = CrawlingFunction.PostDataToTheSelectlistPage, args = (northCampusUrl + "2", postDataObj6, headers, cursor, connect))
threads.append(thread6)
thread7 = threading.Thread(target = CrawlingFunction.PostDataToTheSelectlistPage, args = (xiliCampusUrl, postDataObj7, headers, cursor, connect))
threads.append(thread7)
thread8 = threading.Thread(target = CrawlingFunction.PostDataToTheSelectlistPage, args = (southCampusUrl, postDataObj8, headers, cursor, connect))
threads.append(thread8)
thread9 = threading.Thread(target = CrawlingFunction.PostDataToTheSelectlistPage, args = (northCampusUrl + "2", postDataObj9, headers, cursor, connect))
threads.append(thread9)

for t in threads:
	# Guardian threads
	t.setDaemon(True)
	t.start()

for t in threads:
	# The parent thread will always be blocked until the child thread completes the run
	t.join()

# End the timer
end = datetime.datetime.now()
print("The program is time consuming: " + str(end - mid))

# Close cursor and connect
cursor.close()
connect.close()

#
#
# End ThreadTest
#
#
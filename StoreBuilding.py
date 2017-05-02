# Author: LJF
# Coding: UTF-8
# The version of python: 3.5
# Created time: 2017/04/30
# This is the function of storing the information of the building into the database

import timeit
import datetime
import pymysql
import Database
import GeneralFunction

# Connect to the database
connect = Database.connect

# Set the cursor
cursor = connect.cursor()

# Set url
baseUrl = "http://192.168.84.3:9090/cgcSims/login.do?task=station&client="
northCampusUrl = baseUrl + "192.168.84.1"
southCampusUrl = baseUrl + "192.168.84.110"
xiliCampusUrl = baseUrl + "172.21.101.11"

# Start the timer
start = datetime.datetime.now()

# Store the information of the building into the database
crawlXiliBuilding = str(GeneralFunction.StoreBuildingInformation(xiliCampusUrl, cursor, connect))
crawlSouthBuilding = str(GeneralFunction.StoreBuildingInformation(southCampusUrl, cursor, connect))
crawlNorthBuilding = str(GeneralFunction.StoreBuildingInformation(northCampusUrl, cursor, connect))

# End the timer
end = datetime.datetime.now()
print("The program is time consuming: " + str(end - start))

# Calculate the time required to execute the function
timeOfCrawlXiliBuilding = timeit.timeit(crawlXiliBuilding, 'from __main__ import GeneralFunction')
timeOfCrawlSouthBuilding = timeit.timeit(crawlSouthBuilding, 'from __main__ import GeneralFunction')
timeOfCrawlNorthBuilding = timeit.timeit(crawlNorthBuilding, 'from __main__ import GeneralFunction')

print("The time required to crawl the building information of the xili campus: ", timeOfCrawlXiliBuilding)
print("The time required to crawl the building information of the south campus: ", timeOfCrawlSouthBuilding)
print("The time required to crawl the building information of the north campus: ", timeOfCrawlNorthBuilding)

# Close cursor and connect
cursor.close()
connect.close()

#
#
# End StoreBuilding
#
#
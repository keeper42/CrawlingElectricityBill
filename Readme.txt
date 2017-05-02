Crawling electricity bill version 1.0

This version has not been multi-threaded to crawl electricity information, so crawling time is relatively
 
long, running on my machine is about two and a half hours.

Here are some steps to run this program: 

Configure information about the database in Database.py.

Build the database named electricity_bill, and import the sql file under the sql path into the database.

Run the Schedule.py program: python Schedule.py, Schedule.py is used to run Main.py periodically.


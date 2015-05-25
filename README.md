# Web-Crawler
1.Python Script:
I have developed two python scripts one (first.py) to crawl the web page with infinite scroll and collect data which requires webdriver and virtual display and second one (test.py) which crawls the web pages and collects data and stores data in the database.
	Libraries and Packages used:
	requests: To request the required webpage url  
	beautifulsoup4: To parse the data and get required elements from the page
    time: To set the crawler for particular amount of time
    pyvirtualdisplay: Start virtual display for crawling 
    selenium: to access the browser using their webdriver
    MySQLdb: to connect to the database and store data.

2. HTML page
test.html uses jQuery for Ajax call to PHP script to search and fetch data and for Bootstrap usage which makes the page more interactive and interesting and helps in designing the mobile web page in the same html document.

3. PHP Script
It uses JSON data format to store the data retrieved from database and the JSON data is sent back to the HTML page for display.


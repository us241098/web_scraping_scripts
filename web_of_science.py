from selenium import webdriver
import time
driver = webdriver.Chrome()
from bs4 import BeautifulSoup

from openpyxl import load_workbook

workbook_name = 'result.xlsx'
wb = load_workbook(workbook_name)
page = wb.active


driver.get("http://apps.webofknowledge.com/WOS_GeneralSearch_input.do?SID=C6qXiidVpPyJbWb81HP&product=WOS&search_mode=GeneralSearch")
time.sleep(5)
username=raw_input("Search: ")
#password=raw_input("Password: ")
#po=input("Page to start scraping: ")

#soup = BeautifulSoup(html)	
driver.find_element_by_id("value(input1)").send_keys(username)
#driver.find_element_by_id("textfield4").send_keys(password)
driver.find_element_by_class_name("searchButton").click()
time.sleep(5)
counter=1
while(1):
	for i in range(11):
		k=driver.find_elements_by_xpath("//*[@class='smallV110 snowplow-full-record']")
		print k
		if (i==10):
			break
 		print i
		k[i].click()
		time.sleep(2)
		ab=driver.find_element_by_xpath("//*[@id='records_form']/div/div/div/div[1]/div/div[4]/div//following-sibling::p")
		dp=driver.find_element_by_xpath("//*[@id='records_form']/div/div/div/div[1]/div/div[3]/p[4]/value")
		source=driver.find_element_by_xpath("//*[@id='records_form']/div/div/div/div[1]/div/div[3]/p[1]/span/value")
		print dp.text,source.text
		line1="AB  "+ str(ab.text)
		line2="Date Published  "+ str(dp.text)
		line3="Source  "+ str(source.text)

		file1 = open(str(counter),"w") 
		file1.write("%s\n%s\n%s\n" % (line1, line2, line3))
		file1.close()
		
		counter=counter+1
		driver.execute_script("window.history.go(-1)")
	driver.find_element_by_xpath("//*[@id='summary_navigation']/nav/table/tbody/tr/td[3]/a").click()

	
	



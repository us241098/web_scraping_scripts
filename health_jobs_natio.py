from selenium import webdriver
import time
driver = webdriver.Chrome()
from bs4 import BeautifulSoup

from openpyxl import load_workbook

workbook_name = 'result_health.xlsx'
wb = load_workbook(workbook_name)
page = wb.active

username=raw_input("Username: ")
password=raw_input("Password: ")
po=input("Page to start scraping: ")

driver.get("https://www.healthjobsnationwide.com/user/login?current=node/172")
time.sleep(5)

driver.find_element_by_id("edit-name").send_keys(username)
driver.find_element_by_id("edit-pass").send_keys(password)
driver.find_element_by_id("edit-submit").click()

p=''



while(1):

	try:
		driver.get("https://www.healthjobsnationwide.com/search/resume?page="+str(po))
	except:
		print "all pages finished or some error fetching the page"

		
		#elems = driver.find_elements_by_xpath("//a[@href]")
		soup1 = BeautifulSoup(driver.page_source,"html.parser")
		#lll=soup1.find_all("a", class_="recruiter-resume-link")
		#lll=driver.find_element_by_class("recruiter-resume-link")
		

	try:
		for i in range(0,19):
			time.sleep(2)
			lll= driver.find_elements_by_class_name("recruiter-resume-link")
			print lll[i]
			lll[i].click()
			try:

				h1_title = driver.find_elements_by_class_name('page-title')
				elements = driver.find_elements_by_class_name('field__item')
				n_mail = driver.find_elements_by_class_name('field-item')
			
			except:
				print "some info might be missing"

			try:
				title=(h1_title[0]).text
				#print "TITLE "+ title
			except:
				print "title missing"

			try:
				name=(n_mail[0]).text
				#print "NAME "+ name
			except:
				print "name missing"
			
			try:
				address=(elements[1]).text
				#print "ADD "+ address
			except:
				print "address missing"

			try:
				phone=(elements[2]).text
				#print "PHONE "+ phone
			except:
				print "phone missing"
			
			try:
				email=(n_mail[1]).text
				#print "EMAIL "+ email
			except:
				print "email missing"

			try:
				info = [title, name, email, phone, address]
				page.append(info)
				print "row written"
				wb.save(filename=workbook_name)
			except:
				print "some error while saving"

			time.sleep(4)
			driver.execute_script("window.history.go(-1)")

	except:

		print "all the profiles in page are finsihed starting next page"



	print "page number finished: " + po	
	po=po+1






































































































































































			try:

				h1_title = driver.find_elements_by_class_name('page-title')
				elements = driver.find_elements_by_class_name('field__item')
				n_mail = driver.find_elements_by_class_name('field-item')
			
			except:
				print "some info might be missing"

			try:
				title=(h1_title[0]).text
				#print "TITLE "+ title
			except:
				print "title missing"

			try:
				name=(n_mail[0]).text
				#print "NAME "+ name
			except:
				print "name missing"
			
			try:
				address=(elements[1]).text
				#print "ADD "+ address
			except:
				print "address missing"

			try:
				phone=(elements[2]).text
				#print "PHONE "+ phone
			except:
				print "phone missing"
			
			try:
				email=(n_mail[1]).text
				#print "EMAIL "+ email
			except:
				print "email missing"

			try:
				info = [title, name, email, phone, address]
				page.append(info)
				print "row written"
				wb.save(filename=workbook_name)
			except:
				print "some error while saving"

			time.sleep(4)
			driver.execute_script("window.history.go(-1)")

	except:

		print "all the profiles in page are finsihed starting next page"



	print "page number finished: " + po	
	po=po+1





















































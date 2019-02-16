from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from openpyxl import load_workbook

workbook_name = 'result_indeed.xlsx'
wb = load_workbook(workbook_name)
page = wb.active

username=raw_input("Username: ")
password=raw_input("Password: ")
po=input("Page to start scraping: ")

driver.get("https://secure.indeed.com/account/login?service=my&hl=en_IN&co=IN&continue=https%3A%2F%2Fwww.indeed.co.in%2F")
time.sleep(5)

driver.find_element_by_id("signin_email").send_keys(username)
driver.find_element_by_id("signin_password").send_keys(password)
wait = WebDriverWait(driver, 15)
submit = wait.until(EC.presence_of_element_located((By.CLASS_NAME,'icl-Button--primary')))
submit.click()

p=''



while(1):

	try:
		driver.get("https://employers.indeed.com/c#candidates?id=0&p="+str(po))
	except:
		print "all pages finished or some error fetching the page"

		
		#elems = driver.find_elements_by_xpath("//a[@href]")
		soup1 = BeautifulSoup(driver.page_source,"html.parser")
		#lll=soup1.find_all("a", class_="recruiter-resume-link")
		#lll=driver.find_element_by_class("recruiter-resume-link")
		

	try:

		for i in range(0,19):

			time.sleep(5)
			lll= driver.find_elements_by_class_name("cpqap-CandidatesTable-name")
			print lll

			try:
				lll[i].click()
				time.sleep(8)
				wait.until(EC.presence_of_element_located((By.ID, 'msg-resume')))
			except:
				continue

			content = BeautifulSoup(driver.page_source, 'html.parser')
			header = content.find('div', attrs={'id': 'stickyCandidateHeader'})


			try:
				resume = content.find('div', attrs={'id': 'resume'}).get_text().replace('Download', '')
			except:
				resume = ''



			try:
				title = header.find('h4', class_='job-title').get_text()
			except:
				title = ''


			try:
				name = header.find('h3', class_='name').get_text()
			except:
				name = ''

			try:
				address = header.find('h4', class_='location').get_text()
			except:
				address = ''



			try:
				email = header.find('a', attrs={'id': 'candEmailLink'}).get_text()
			except:
				email = ''


			try:
				phone = header.find('div', attrs={'id': 'report-call-candidate-head-form'}).get_text()
			except:
				phone = ''



			

			try:
				info = [title,name,email,phone,resume,address]
				page.append(info)
				print "row written"
				print name
				wb.save(filename=workbook_name)
			except:
				print "error while saving"
			#time.sleep(2)


			driver.execute_script("window.history.go(-1)")





	except Exception as e:
		print "exception"
		#print e

	if po >1:
		print "page number finished: " + str(po)


	po=po+1






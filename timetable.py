from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime

today = datetime.datetime.now()
str_today = str(today.day).zfill(2) + "/" + str(today.month).zfill(2) + "/" + str(today.year)
start_hour  = "09:00"
number_hours = "9"
user = "plucena@br.ibm.com"
pwd = "xxx"

if(today.weekday()<6):
	driver = webdriver.Firefox()
	driver.get("https://docs.google.com/forms/d/1bnbH5z-qV_LCsg5I_mdkd1T5kK0L3UF5T3MFbwXaCYs/viewform?edit_requested=true#")
	#assert "Python" in driver.title
	element = driver.find_element_by_id("entry_444885743")
	element.send_keys(str_today)
	element = driver.find_element_by_id("entry_645594624")
	element.send_keys(start_hour)
	element = driver.find_element_by_id("entry_235408508")
	element.send_keys(number_hours)
	elem = driver.find_element_by_id("ss-submit")
	elem.send_keys(Keys.RETURN)
	driver.close()
	print("Enviado")


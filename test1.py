from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
import config1 as config
import re
import xlrd
import csv
import types
from selenium.common.exceptions import NoSuchElementException


def login():
	user = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div/div[1]/div/form/div[2]/div[1]/input')
	user.send_keys('FamilusiAdmin')
    
    password = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div/div[1]/div/form/div[2]/div[1]/input')
	password.send_keys(config1.PWORD)
    
	login_attempt = browser.find_element_by_xpath("//*[contains(text(), 'Log In')]")
	login_attempt.submit()

	sleep(2)
	



#Open website
browser = webdriver.Chrome()
browser.get('https://{loogin-url-address}.com/#/categoryManagement')
browser.maximize_window()
browser.implicitly_wait(10)

#Login
login()

#Open the desired MD Lookup
sleep(2)
opnLKUP = browser.find_element_by_xpath("//*[contains(text(), 'assistantVP')]")
opnLKUP.click()





print("SUCCESS")

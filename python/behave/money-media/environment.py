from behave import *

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def before_all(context):
	#for x in context.__dict__:
	#	print x
	pass

def before_scenario(context, scenario):

	if ('browser' in context.config.userdata.keys()):
		if (context.config.userdata['browser'] == 'chrome'): 		
			chrome_driver_path = "C:\\Documents and Settings\\chuck\Desktop\\shri\\Development\\test_tools\\selenium\\chromedriver.exe"
			context.driver = webdriver.Chrome(chrome_driver_path) 
		else:
			context.driver = webdriver.Firefox()	
	else:
		context.driver = webdriver.Firefox()	
	
	context.driver.implicitly_wait(10) #waits 10s for any element to appear in DOM
	
def after_scenario(context, scenario):
	context.driver.quit()


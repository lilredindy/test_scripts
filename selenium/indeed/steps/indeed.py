from behave import *
from types import *

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def login(context, username, password):
	email_field = context.driver.find_element_by_id('signin_email')
	email_field.clear()
	email_field.send_keys(username)

	pwd_field = context.driver.find_element_by_id('signin_password')
	pwd_field.clear()
	pwd_field.send_keys(password)

	submit_btn = context.driver.find_element_by_class_name('input_submit')
	submit_btn.click()


@given('I am on the login screen')
def step_impl(context):
	context.driver.get("https://secure.indeed.com/account/login")

@when('I submit valid credentials')
def step_impl(context):
	login(context, "shri.amin@gmail.com", "maverick")

'''
@when('I enter a valid username')
def step_impl(context):
	email_field = context.driver.find_element_by_id('signin_email')
	email_field.send_keys("shri.amin@gmail.com")
'''

'''
@when('I enter a valid password')
def step_impl(context):
	pwd_field = context.driver.find_element_by_id('signin_password')
	pwd_field.send_keys("maverick")
'''

'''
@when('I click submit')
def step_impl(context):
	submit_btn = context.driver.find_element_by_class_name('input_submit')
	submit_btn.click()
'''

@then('I should be logged in')
def step_impl(context):
	signout_link = context.driver.find_element_by_link_text('sign out')
	#txt = "sign out"
	#assert txt in context.driver.page_source #not element...implicit wait not enforced

@then('I should see my account settings')
def step_impl(context):
	txt = "Account Settings"
	assert txt in context.driver.page_source

'''
@when('I enter the invalid credentials "{username}" and "{password}"')
def step_impl(context, username, password):
	email_field = context.driver.find_element_by_id('signin_email')
	email_field.send_keys(username)
	pwd_field = context.driver.find_element_by_id('signin_password')
	pwd_field.send_keys(password)
'''

@when('I submit invalid credentials "{username}" and "{password}"')
def step_impl(context, username, password):
	login(context, username,password)


@then('I should see bad credentials error message')
def step_impl(context):
	txt = "Incorrect login or password"
	assert txt in context.driver.page_source

'''
@given ('I am already logged in')
def step_impl(context):
	context.driver.get("https://secure.indeed.com/account/login")
	email_field = context.driver.find_element_by_id('signin_email')
	email_field.send_keys('shri.amin@gmail.com')
	pwd_field = context.driver.find_element_by_id('signin_password')
	pwd_field.send_keys('maverick')
	submit_btn = context.driver.find_element_by_class_name('input_submit')
	submit_btn.click()
	signout_link = context.driver.find_element_by_link_text('sign out')
'''


@given('I am already logged in')
def step_impl(context):
	context.execute_steps(u'given I am on the login screen')
	context.execute_steps(u'when I submit valid credentials')
	context.execute_steps(u'then I should be logged in')
	

@when('I attempt to access login page')
def step_impl(context):
	context.driver.get("https://secure.indeed.com/account/login")


@then('I should be redirected to my account page')
def step_impl(context):
	url = 'https://secure.indeed.com/account/view?hl=en'
	assert context.driver.current_url == url


@then('I should not see a sign in link')
def step_impl(context):
	try:
		context.driver.find_element_by_link_text('sign in')
	except NoSuchElementException:
		assert True
	else:
		assert False
'''
@when('I submit an invalid password three times')
def step_impl(context):
	for row in context.table:
		pwd_field = context.driver.find_element_by_id('signin_password')
		pwd_field.send_keys(row['bad_pwd'])
		submit_btn = context.driver.find_element_by_class_name('input_submit')
		submit_btn.click()
'''

@when('I submit valid email with invalid password three times')
def step_impl(context):
	for row in context.table:
		login(context, 'shri.amin@gmail.com', row['bad_pwd'])

@then('I should see retry in five minutes error message')
def step_impl(context):
	txt = 'sorry, please try again in 5 minutes'
	assert txt in context.driver.page_source

@then('the username and password fields should be blank')
def step_impl(context):
	email_txt = context.driver.find_element_by_id('signin_email').text
	assert email_txt == ""
	pwd_txt = context.driver.find_element_by_id('signin_password').text
	assert pwd_txt == ""

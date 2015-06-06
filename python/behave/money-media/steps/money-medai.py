from behave import *
from types import *

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


@when('I enter the search term "{text}"')
def step_impl(context, text):
	context.driver.find_element_by_css_selector("input[name=q]").send_keys(text)

@when('I click search button')
def step_impl(context):
	context.driver.find_element_by_css_selector("form#nav-search div.search-box input:nth-child(2)").click()

@then('I should see the search results')
def step_impl(context):
	assert context.driver.find_element_by_class_name("results")


@given('I am on the main page')
def step_impl(context):
	context.driver.get("http://www.financialadvisoriq.com/")

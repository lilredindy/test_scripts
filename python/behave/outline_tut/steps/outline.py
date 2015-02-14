from behave import *

@given('I put "{thing}" in a blender')
def step_impl(context, thing):
	assert True

@when('I switch the blender on')
def step_impl(context):
    assert True

@then('it should transform into "{other_thing}"')
def step_impl(context, other_thing):
    assert True

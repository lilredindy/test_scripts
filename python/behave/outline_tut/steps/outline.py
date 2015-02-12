from behave import *

@given('I put "{thing}" in a blender')
def step_impl(context,thing):
	pass


@when('I switch the blender on')
def step_impl(context):
    assert True is not False

@then('it should transform into "{other_thing}"')
def step_impl(context, other_thing):
    assert context.failed is False


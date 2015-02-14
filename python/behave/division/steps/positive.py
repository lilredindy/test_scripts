from behave import *
from types import *

@given('we have two positive integers "{a}" and "{b}"')
def step_impl(context, a, b):
	assert type(a).__name__ == 'unicode'
	assert type(b) == UnicodeType
	a = int(a)
	b = int(b)
	assert isinstance(a, int)
	assert isinstance(b, int)
	assert a > 0
	assert b > 0

@when('we divide "{a}" by "{b}"')
def step_impl(context,a,b):
    context.c = int(a) / int(b)

@then('the result "{c}" will be positive')
def step_impl(context,c):
	assert context.c == int(c)
	assert int(c) > 0

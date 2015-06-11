def get_text(name):
   return "lorem ipsum, {0} dolor sit amet".format(name)

def p_decorate(func):
   def func_wrapper(name):
       return "<p>{0}</p>".format(func(name))
   return func_wrapper

my_get_text = p_decorate(get_text)

print my_get_text("John")

#$$#########################################
############################################
import string 

def get_message(msg_part):
	return "this is the message %s" % (msg_part)

def p_decorate(func):
	def func_wrapper(msg):
		msg = string.rstrip(msg, "lo")
		return func(msg)
	return func_wrapper

my_func_wrapper = p_decorate(get_message)
print my_func_wrapper("hello")


import unittest
from selenium import webdriver
import new, sys

def repeat(times=1):
    def decorator(base_class): 
        module = sys.modules[base_class.__module__].__dict__
    	for x in range(times):
    		d = dict(base_class.__dict__)
    		name = "%s_%s" % (base_class.__name__, x + 1)
    		print name
    		module[name] = new.classobj(name, (base_class,),d)
    return decorator


def repeat2(times=1):
    def decorator(f): 
        def new_f(*args):
            for x in range(times):
                f(*args) #args[0] is self parameter
        return new_f
    return decorator


class ElephantTestCase(unittest.TestCase):

	def setUp(self):
		print("hello world")
		chrome_path = "C:\\Documents and Settings\\chuck\\Desktop\\shri\\Development\\test_tools\\selenium\\chromedriver.exe";
		#chrome_options = webdriver.ChromeOptions()
		#chrome_options.add_argument('--chrome_path=%s' % chrome_path)
		#System.setProperty("webdriver.chrome.driver", chrome_path);
		self.driver = webdriver.Chrome(executable_path=chrome_path)

	@repeat2(2)
	def test_get_page(self):
		print("sad times")
		self.driver.get('http://www.theguardian.com/environment/2015/jul/07/zimbabwe-activists-deplore-sale-of-24-elephant-calves-to-china#comment-55235133')

	def tearDown(self):
		print("bye bye")
		self.driver.quit() 

if __name__ == '__main__':
	unittest.main()

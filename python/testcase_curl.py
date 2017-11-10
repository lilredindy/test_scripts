from subprocess import call
import unittest

class curl_tests(unittest.TestCase):

        def setUp(self):
            pass

        def test_get_homepage(self):
			call(["curl", "--head", "-o", "curl_output.txt","https://www.theatlantic.com"])
			with open("curl_output.txt") as file:
				found = any("200" in line.split() for line in file)	#done on 1st True 		   
				#if not found:
				self.assertTrue(found)


        def tearDown(self):
        	pass

       	def test_latency(self): 
			pass #call(["curl", "-o","" "curl_output.txt","https://www.theatlantic.com"])


if __name__ == '__main__':
        unittest.main()

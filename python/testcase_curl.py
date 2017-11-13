from subprocess import call, check_output
import unittest
import random
import os


class pageTests(unittest.TestCase):
	if (os.name is 'posix'):
		device_file = '/dev/null'
	elif (os.name is 'windows'):
		device_file = 'NUL'
	else:
		device_file = ''

class google_homepage_tests(unittest.TestCase):

        def setUp(self):
            pass

        def test_GET(self):
			call(["curl","-s", "-D", "curl-headers.txt", "-o", "curl-body.txt", "https://www.google.com"])
			with open("curl-headers.txt") as file:
				found = any("200" and "OK" in line.split() for line in file)	#done on 1st True 		   
				#if not found:
				self.assertTrue(found)
			file.closed

        def test_GET_with_key_value_query_str(self): #check with db??
			call(["curl","-s", "-D", "curl-headers.txt", "-o", "curl-body.txt", "https://www.google.com?foo=bar"])
			with open("curl-headers.txt") as file:
				found = any("200" and "OK" in line.split() for line in file)	#done on 1st True 		   
				#if not found:
				self.assertTrue(found)
			file.closed

        def test_POST_homepage(self): #is this good test?? better to check db??
			call(["curl","-s", "-D", "curl-headers.txt", "-o", "curl-body.txt", "-d", "foo=bar","https://www.google.com"])
			with open("curl-headers.txt") as file:
				found = any("405 Method Not Allowed" in line for line in file)	#done on 1st True 		   
				#if not found:
				self.assertTrue(found)
			file.closed		

        #@unittest.skip("")
       	def test_size(self):  			#this should be run in scheduled time interval?
			download_size = check_output(["curl","-s","-D","curl-headers.txt", "-o", "curl-body.txt","-w", "%{size_download}", "https://www.google.com?{}".format(random.randint(1,1000))])
			assert int(download_size) < 15000 #CHECK FOR ~ APROX. AROUND ETC

        #@unittest.skip("")
       	def test_latency(self):  			#this should be run in scheduled time interval?
			#call(["curl","-s","-D", "curl-headers.txt", "-o", "curl-body.txt","-w", "@curl-format.txt", "https://www.google.com"], stdout=file)
			total_time = check_output(["curl","-s","-D","curl-headers.txt", "-o", "curl-body.txt","-w", "%{time_total}", "https://www.google.com?{}".format(random.randint(1,1000))])
			assert float(total_time) < 3

        def tearDown(self):
        	pass



class theAtlantic_tests(unittest.TestCase):

        def setUp(self):
            pass

        def tearDown(self):
        	pass


if __name__ == '__main__':
        unittest.main()

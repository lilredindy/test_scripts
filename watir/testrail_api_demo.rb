#require "rubygems"
require "test/unit"
require "watir-webdriver"
require "./testrail.rb"
 
class TestTestRail < Test::Unit::TestCase

####################################################

	def setup 
		#@browser ||= Watir::Browser.new :firefox
        @client = TestRail::APIClient.new('https://lilredindy.testrail.com')
        @client.user = 'shri.amin@gmail.com'
        @client.password = 'aOF6OtED/3S01miFVnw6'

	end
   
	def teardown 
		#@browser.close
	end

#####################################################  


######################################################
=begin

	def test_testrail_get_users
		c = @client.send_get('get_users')
		puts c 
	end

    def test_testrail_get_case
        c = @client.send_get('get_case/1')
        puts c
    end


	def test_testrail_update_result_4_fail
		r = @client.send_post('add_result_for_case/1/1',
			{ :status_id => 5, :comment => 'This test has failed!' })
		puts r
	end


	def test_get_project
		result = @client.send_get('get_project/1')
		puts result
	end
=end

	def test_del_prj
		result = @client.send_post('delete_project/1', {})
		puts result
	end

end

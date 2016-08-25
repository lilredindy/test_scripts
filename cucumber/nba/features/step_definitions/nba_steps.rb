require "watir-webdriver"
require "rspec/expectations"
 
#Note: the browser open and close call is in env.rb




Given(/^I am on the nba home page$/) do
	@browser.goto "nba.com"
	expect(@browser.url).to eq("http://www.nba.com/")
end

###################################################################
###################################################################
Given(/^sitemap link title "([^"]*)" is present$/) do |link_title|
	expect(@browser.link(:text => link_title).present?).to be true 
end

When(/^I click on the sitemap link titled "([^"]*)"$/) do |link_title|
	@browser.link(:text => link_title).click
end


Then(/^I should arrive at correct "([^"]*)"$/) do |dest_url|
	expect(@browser.url).to eq dest_url
end

###################################################################
###################################################################


Then(/^I should see six big blocks of content$/) do
	blocks = @browser.divs(:class => "nbaTPanel")
	expect(blocks.count).to eq 6
	blocks.each do |block|
		#url = block.link(:class => "nbaTImage").attribute_value("href")
		#puts url
		block_link = block.link(:class => "nbaTImage") 
		if (block_link.present?)
			block_img = block_link.img(:class => "nbaTMainImage")
			expect(block_img.present?).to be true
		end
	end
end



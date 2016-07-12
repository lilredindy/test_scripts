require 'watir-webdriver'


Before do
	# Do something before each scenario.
	@browser ||= Watir::Browser.new :firefox

end

After do |scenario|
	# Do something after each scenario.
	@browser.close
end


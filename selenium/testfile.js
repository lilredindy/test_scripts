<!-- http://engineering.wingify.com/posts/e2e-testing-with-webdriverjs-jasmine/ -->

var webdriver = require('selenium-webdriver');

var driver = new webdriver.Builder().
    withCapabilities(webdriver.Capabilities.firefox()).
    build();

driver.get('http://www.wingify.com');

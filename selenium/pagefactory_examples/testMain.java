package test.selenium.pagefactory;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.PageFactory;

public class testMain {
	
	public static void main(String[] args) {

		// Create a new instance of the Firefox driver
		WebDriver driver = new FirefoxDriver();

		// Now use the firefox instance driver to open a page URL
		driver.get("http://www.whiteboxtest.com/selenium-test1.php");
		// driver.navigate().to("http://www.google.com"); alternative to open a
		// URL
		
		SeleniumTest1 seleniumTest1 = PageFactory.initElements(driver, SeleniumTest1.class);
		seleniumTest1.clickButtonPresentByID_id012();
		SeleniumTest2 seleniumTest2 = seleniumTest1.clickSeleniumTest2();
		seleniumTest2.inputTextBox("hello");
		seleniumTest1 = seleniumTest2.clickSeleniumTest1();

		// Close and clean firefox driver instance
		driver.quit();
	}

}

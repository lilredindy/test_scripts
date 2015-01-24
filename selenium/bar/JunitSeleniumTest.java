package bar;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.sele  nium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
//import org.testng.annotations.*;
//import org.testng.Assert;
import org.junit.Test;
import org.junit.Assert;
import org.junit.*;

public class JunitSeleniumTest {
	 
	// create a WebDriver
	private WebDriver driver;
	 
	// use the Firefox browser and go to the wikipedia site
	@Before
	public void setUp(){
		driver = new FirefoxDriver();
		driver.get("http://en.wikipedia.org/wiki/Main_Page");
	}
	 
	// quit from WebDriver
	@After
	public  void tearDown(){
		driver.quit();
	}
	 
	@Test
	public void testFindElements()throws Exception{
		 
		//find the About link
		WebElement about= driver.findElement(By.xpath("//*[@id='n-aboutsite']/a"));
		 
		// click to the link
		about.click();
		 
		// wait for 5 seconds
		Thread.sleep(5000);
		 
		// write out the title of the page in console
		System.out.println(driver.getTitle());
	}

}
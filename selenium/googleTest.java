import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
//import org.testng.annotations.*;
//import org.testng.Assert;
import org.junit.Test;
import org.junit.Assert;
import org.junit.*;

public class googleTest {
	 
	// create a WebDriver
	private static WebDriver driver;
	 
	// use the Firefox browser and go to the wikipedia site
	@BeforeClass
	public static void setUp() {
		driver = new FirefoxDriver();
		driver.get("http://www.google.com");
		//driver.manage().deleteAllCookies(); //delete all cookies

	}
	 
	// quit from WebDriver
	@AfterClass
	public static void tearDown(){
		//driver.quit();
	}
	 

	@Test
	public void testGoogle()throws Exception{
		//driver.findElement(By.cssSelector("input.gbqfif")).sendKeys("tut+ code");
		driver.findElement(By.cssSelector("input[name=q]")).sendKeys("tut+ code");
		driver.findElement(By.cssSelector("button.gbqfb")).click();
		Thread.sleep(5000); //dont use this method of waiting
		driver.findElement(By.linkText("Tuts+ Free Code Tutorials")).click();

	}

}
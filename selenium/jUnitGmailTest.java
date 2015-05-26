import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
//import org.testng.annotations.*;
//import org.testng.Assert;
import org.junit.Test;
import org.junit.Assert;
import org.junit.*;

public class jUnitGmailTest {
	 
	// create a WebDriver
	private static WebDriver driver;
	 
	// use the Firefox browser and go to the wikipedia site
	@Before
	public void setUp() {
		driver = new FirefoxDriver();
		driver.get("http://www.gmail.com");
		//driver.manage().deleteAllCookies(); //delete all cookies

	}
	 
	// quit from WebDriver
	@After
	public void tearDown(){
		driver.quit();
	}
	 

	private void gmailLogin(String username, String password){

		driver.findElement(By.id("Email")).sendKeys(username);
		driver.findElement(By.id("Passwd")).sendKeys(password);
		driver.findElement(By.id("signIn")).click();

	}

	@Test
	public void login()throws Exception{
		gmailLogin("lilredindy", "flower45");
		//driver.findElement(By.partialLinkText("Forth Estate")).click();

	}

}
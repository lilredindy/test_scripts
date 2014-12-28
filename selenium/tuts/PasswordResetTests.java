import org.openqa.selenium.WebDriver;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.openqa.selenium.support.*;

//import org.testng.annotations.*;
//import org.testng.Assert;

//class variables & setUp and tearDown 
//need to be static for junit, but not for TestNG
import org.junit.Test;
import org.junit.Assert;
import org.junit.*;

public class PasswordResetTests {
	 
	private static WebDriver driver;
	private static TutsActions actions;
 

	@BeforeClass
	public static void setUp(){
		driver = new FirefoxDriver();
		actions = PageFactory.initElements(driver, TutsActions.class);
		driver.get("https://tutsplus.com/account/password_resets/new");
	}
	 
	// quit from WebDriver
	@AfterClass
	public static void tearDown(){
		//driver.quit();
	}
	 
	@Test
	public void PasswordRestAcceptanceTest()throws Exception{

		//accepts the entire reset password workflow
		//it must do verification at each stage 
		
		actions.SendPasswordResetVerficationLink();
	 
		//now check db to see if password reset token is generated 
	}

	@Test
	public void CheckIfEmailInputFieldIsDisabled()throws Exception{
	 
	}



}

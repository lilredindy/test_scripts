import org.openqa.selenium.WebDriver;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.openqa.selenium.support.*;

//import org.testng.annotations.*;
//import org.testng.Assert;

//class variables & setUp and tearDown 
//need to be static for junit, but not for TestNG
import org.junit.Test;
import org.junit.Assert;
import org.junit.*;



public class LibertyTests{


	private static WebDriver driver;

	@BeforeClass
	public static void setUp(){
		//driver = new FirefoxDriver();
		String chrome_path = "C:\\Documents and Settings\\chuck\\Desktop\\shri\\Development\\test_tools\\selenium\\chromedriver.exe";
		System.setProperty("webdriver.chrome.driver", chrome_path);
		WebDriver driver = new ChromeDriver();
		//actions = PageFactory.initElements(driver, TutsActions.class);

	}
	 
	// quit from WebDriver
	@AfterClass
	public static void tearDown(){

	}


	@Test
	public void run_this_test()throws Exception{

				driver.get("http://www.google.com");

		//System.out.println("whatever");
	 	//driver.quit();
		
	}
}

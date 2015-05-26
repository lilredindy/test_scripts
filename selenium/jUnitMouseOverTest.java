import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebDriver.Window;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;
//import org.testng.annotations.*;
//import org.testng.Assert;
import org.junit.Test;
import org.junit.Assert;
import org.junit.*;
import java.util.concurrent.TimeUnit;


public class jUnitMouseOverTest {
	 
	// create a WebDriver
	private WebDriver driver;
	 
	// use the Firefox browser and go to the wikipedia site
	@Before
	public void setUp(){
		//String chrome_path = "C:\\Documents and Settings\\chuck\\Desktop\\shri\\Development\\test_tools\\selenium\\chromedriver.exe";
		//System.setProperty("webdriver.chrome.driver", chrome_path);
		//driver = new ChromeDriver();

		driver = new FirefoxDriver();
		driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
		driver.get("http://skreened.com/theredsun/chak-chel");
	}
	 
	// quit from WebDriver
	@After
	public  void tearDown(){
		//driver.quit();
	}
	 
	@Test
	public void mouseOverElementTest()throws Exception{
		
		driver.manage().window().maximize();//maximise the window

		WebElement close_popup_btn = driver.findElement(By.cssSelector("a.ltkmodal-close:nth-child(1)"));
		close_popup_btn.click();

		WebElement btn = driver.findElement(By.cssSelector("#checkout-btn"));

		Actions action = new Actions(driver);
		action.moveToElement(btn).perform();
		
	}

}
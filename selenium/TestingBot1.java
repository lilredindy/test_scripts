//import junit.framework.TestCase;
import org.openqa.selenium.*;
import org.openqa.selenium.remote.*;
import java.net.URL;
import java.util.concurrent.TimeUnit;
import org.openqa.selenium.remote.SessionId;


import org.junit.Test;
import org.junit.Assert;
import org.junit.*;


import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;
import org.junit.runner.notification.RunListener;


public class TestingBot1 extends RunListener{

	private WebDriver driver;
	
	public void testFailure(Failure failure){ //override RunListener

		System.out.println("Failed test: " + failure.getDescription().getMethodName());
		System.out.println("Failed test: " + failure.getException());
		try{
		
			System.out.println("SessionID: " + ((RemoteWebDriver)this.driver).getSessionId().toString());
		}
		catch (Exception e){
			System.out.println("Exception:" + e.getMessage());
		}

	}
	

	@Before
	public void setUp() throws Exception {
		DesiredCapabilities capabilities = DesiredCapabilities.firefox();
		capabilities.setCapability("version", "latest");
		capabilities.setCapability("platform", Platform.WINDOWS);
		capabilities.setCapability("name", "Custom Test Runner run11");

		this.driver = new RemoteWebDriver(
		   new URL("http://e9119262abca817b6e89829a3f3b39ed:10b7b3f28b761a8190a08d262506b227@hub.testingbot.com/wd/hub"),
		   capabilities);
		driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);

	}


	@Test
	public void testSimple1() throws Exception {
		this.driver.get("http://www.espn.com");
		Assert.assertEquals("ESPN: The Worldwide Leader in Sports", this.driver.getTitle());
	}


	@Test
	public void testSimple2() throws Exception {
		this.driver.get("http://www.google.com");
		Assert.assertEquals("Gooogle", this.driver.getTitle());
	}


	@After
	public void tearDown() throws Exception {
		this.driver.quit();
	}

}
import org.junit.*;
import org.openqa.selenium.*;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import java.util.concurrent.TimeUnit;
import java.util.Random;


public class CrowdTwistTests {
	
	private WebDriver driver;
	String registered_email = "foobar23@gmail.com";
	String unregistered_email = "";

	@Before 
	public void setUp() throws Exception{

		String browser = System.getProperty("browser");

		if (browser.equals("chrome"))
			driver = new ChromeDriver();
		else if (browser.equals("firefox")){
			
			System.setProperty("webdriver.gecko.driver", "/usr/local/bin/geckodriver");
			DesiredCapabilities dc = DesiredCapabilities.firefox();
			dc.setCapability("marionette", true);
			driver = new FirefoxDriver(dc); 

			//driver = new FirefoxDriver();
		}
		else
			driver = new ChromeDriver(); //default 4 now

		driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
	}
	
	@After
	public void tearDown() throws Exception {
		driver.quit();
	}

	@Test //@Ignore
	public void invalidEmailTest() throws Exception {
		RegisterPage page = new RegisterPage(driver);
		page.open();
		page.registerEmail("fake_email");
		
		WebElement errorBox = driver.findElement(By.id("create_account_error"));
	}

	@Test //@Ignore
	public void blankEmailTest() throws Exception {
		RegisterPage page = new RegisterPage(driver);
		page.open();
		page.registerEmail("");
		
		WebElement errorBox = driver.findElement(By.id("create_account_error"));
	}

	@Test //@Ignore
	public void duplicateEmailTest() throws Exception {
		RegisterPage page = new RegisterPage(driver);
		page.open();
		page.registerEmail(registered_email);

		WebElement errorBox = driver.findElement(By.id("create_account_error"));
	}

	@Test //@Ignore
	public void blankFirstnameTest() throws Exception {
		RegisterPage page = new RegisterPage(driver);
		page.open();
		page.registerEmail("foobar00@gmail.com");
		page.registerFullForm(RegisterPage.Gender.MRS,
								"", //blank firstname is invalid
								"bar",
								"",
								"pass1234",
								"12",
								"March",
								"1979",
								false,
								false,
								"", 
								"",
								"Adobe Systems",
								"801 N 34th St",
								"Suite 201",
								"Seattle",
								"Washington",
								"98103",
								"United States",
								"Additional info",
								"206-675-7000",
								"206-218-8370",
								"");

		WebElement e = driver.findElement(By.cssSelector("#center_column div.alert.alert-danger"));
	}



	@Test //@Ignore
	public void registerTest1() throws Exception {

		Random r = new Random();
		unregistered_email = "foobar" + String.valueOf(r.nextInt(10000)) + "@gmail.com"; //hack
		//System.out.println(unregistered_email);

		RegisterPage page = new RegisterPage(driver);
		page.open();
		page.registerEmail(unregistered_email);
		page.registerFullForm(RegisterPage.Gender.MRS,
								"foo",
								"bar",
								"", //email from step 1
								"pass1234",
								"12",
								"March",
								"1979",
								false,
								false,
								"", //auto-injects foo
								"", //auto-injects bar
								"Adobe Systems",
								"801 N 34th St",
								"Suite 201",
								"Seattle",
								"Washington",
								"98103",
								"United States",
								"Additional info",
								"206-675-7000",
								"206-218-8370",
								""); //place-holder text exists

		WebElement e = driver.findElement(By.cssSelector("a[class='logout']"));
	}


	@Test //@Ignore
	public void bankwireCheckoutTest1() throws Exception{

			ProductPage page = new ProductPage(driver);
			page.open();
			page.addToCart("div#center_column ul li:nth-child(1) div.left-block a");
			Thread.sleep(5000); //THIS WORKS AND WEBDRIVERWAIT DOES NOT
			page.confirmUpdatedCartBtn.click();

			OrderPage page2 = new OrderPage(driver);
			page2.confirmSummaryBtn.click();
			LoginPage page3 = new LoginPage(driver);
			page3.login("foobar23@gmail.com", "maverick");
			page2.confirmAddressBtn.click();
			page2.clickTermsOfService();
			page2.confirmShippingBtn.click();
			page2.payByBankwireBtn.click();
			page2.confirmPaymentBtn.click();
			String order_no = page2.getOrderNumber();
			page2.orderHistoryLink.click();
			HistoryPage page4 = new HistoryPage(driver);
			
			Assert.assertTrue(page4.orderFound(order_no));

	}

}


import org.junit.*;
import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.support.ui.ExpectedConditions;
//import java.util.regex.Matcher;
//import java.util.regex.Pattern;
import java.util.Random;
import java.util.concurrent.TimeUnit;


//for the testBot framework
import org.openqa.selenium.remote.*;
import java.net.URL;
import java.io.BufferedReader;
import java.io.InputStreamReader;



public class OldCrowd {
	
	private WebDriver driver;
	
	private boolean error = false;
	private boolean success = true;
	private String errorMsg = "";
	private String testName = "";
	
	String register_url = "http://automationpractice.com/index.php?controller=authentication&back=my-account#account-creation";
	private String my_acct_url = "http://automationpractice.com/index.php?controller=my-account";
	private String shop_category_url = "http://automationpractice.com/index.php?id_category=8&controller=category";
	private String fufill_order_url = "http://automationpractice.com/index.php?controller=order";
	
	private String registered_email = "foobar23@gmail.com"; //persists in the DB btwn sessions
	private String unregistered_email = "";
	

	@Before
	public void setUp() throws Exception {
		/*
			DesiredCapabilities capabilities = DesiredCapabilities.firefox();
		capabilities.setCapability("version", "latest");
		capabilities.setCapability("platform", Platform.WINDOWS);
		capabilities.setCapability("name", "CrowdTwist tests");

		this.driver = new RemoteWebDriver(
			new URL("http://key:secret@hub.testingbot.com/wd/hub"),
		   	capabilities);
		driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);*/
		driver = new ChromeDriver();
		driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);

	}

	@After
	public void tearDown() throws Exception {
		//String cmd = String.format("curl \"https://api.testingbot.com/v1/tests/%s\" -X PUT -d \"test[name]=%s\" -d \"test[success]=%s\" -d \"test[status_message]=%s\" -u key:secret", ((RemoteWebDriver)driver).getSessionId(), testName, success, errorMsg);
		//this.executeBashCommand(cmd); //using this with class method
		driver.quit();
		//run script to remove DB records after registration 
	}

	/////////////////////////
	//REGISTER STEP 1 TESTS
	/////////////////////////

	@Test //@Ignore
	public void invalidEmailTest() throws Exception {
		try{
			driver.get(register_url);

			step1_submitEmail("fake_email");
			WebElement errorBox = driver.findElement(By.id("create_account_error"));
		}
		catch (Exception | AssertionError e ){
			error = true;
			errorMsg = e.toString();
			throw e;
		}
	}

	@Test //@Ignore
	public void blankEmailTest() throws Exception {
		try{
			driver.get(register_url);

			step1_submitEmail("");
			WebElement errorBox = driver.findElement(By.id("create_account_error"));
		}
		catch (Exception | AssertionError e ){
			error = true;
			errorMsg = e.toString();
			throw e;
		}
	}

	@Test //@Ignore
	public void duplicateEmailTest() throws Exception {
		try{
			driver.get(register_url);

			step1_submitEmail(registered_email); //assuming this record exists!!!
			WebElement errorBox = driver.findElement(By.id("create_account_error"));
		}
		catch (Exception | AssertionError e ){
			error = true;
			errorMsg = e.toString();
			throw e;
		}
	}

	////////////////////////
	//REGISTER STEP 2 Tests
	///////////////////////
	@Test //@Ignore
	public void blankFirstnameTest() throws Exception {
		try{
			driver.get(register_url);

			step1_submitEmail("foobar00@gmail.com");
			step2_submitCompleteForm(Gender.MRS,
									"", //blank firstname is invalid
									"bar",
									"",
									"maverick",
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
		catch (Exception | AssertionError e ){
			error = true;
			errorMsg = e.toString();
			throw e;
		}
	}

	@Test //@Ignore
	public void registerTest1() throws Exception {
		try {
			driver.get(register_url);

			Random r = new Random();
			unregistered_email = "foobar" + String.valueOf(r.nextInt(10000)) + "@gmail.com"; //hack
			//System.out.println(unregistered_email);

			step1_submitEmail(unregistered_email);
			step2_submitCompleteForm(Gender.MRS,
									"foo",
									"bar",
									"", //email from step 1
									"maverick",
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

			Assert.assertEquals(my_acct_url, driver.getCurrentUrl());
			WebElement e = driver.findElement(By.cssSelector("a[class='logout']"));
		}
		catch (Exception | AssertionError e ){
			error = true;
			errorMsg = e.toString();
			throw e;
		}
	}

	////////////////////////
	//CHECKOUT Tests
	///////////////////////
	@Test //@Ignore
	public void checkoutTest1() throws Exception{
		try {
			driver.get(shop_category_url);

			Actions action = new Actions(driver);
			action.moveToElement(driver.findElement(By.cssSelector("div#center_column ul li:nth-child(1) div.left-block a"))).moveToElement(driver.findElement(By.cssSelector("div#center_column ul li:nth-child(1) div.right-block a.ajax_add_to_cart_button"))).click().build().perform();
	
			//WebDriverWait wait = new WebDriverWait(driver, 5000);
			//WebElement e = wait.until(ExpectedConditions.presenceOfElementLocated(By.id("div#layer_cart a")));
			Thread.sleep(5000); //THIS WORKS AND WEBDRIVERWAIT DOES NOT
	        driver.findElement(By.cssSelector("div#layer_cart a")).click();
	        //((JavascriptExecutor)driver).executeScript("arguments[0].click();", e);

	        //Assert.assertEquals(fufill_order_url, driver.getCurrentUrl());
	      
	        driver.findElement(By.cssSelector("p.cart_navigation a")).click(); //1. summary
	        login(registered_email, "maverick");  //2. sign-in
	       	driver.findElement(By.cssSelector("div#center_column form p button")).click(); //3. address
	       	WebElement e = driver.findElement(By.id("cgv")); //4. shipping	 
	       	if (!e.isSelected())
	       		e.click();
	       	driver.findElement(By.cssSelector("form#form p button")).click(); 
	       	driver.findElement(By.cssSelector("div#HOOK_PAYMENT a.bankwire")).click(); //5. choose payment type
	       	driver.findElement(By.cssSelector("#cart_navigation button")).click(); //confirm payment

	       	String txt=driver.findElement(By.cssSelector("div.box")).getText();
	       	String[] arr = txt.split(" ");

	       	String order_no = "";
	       	boolean b = false;
	       	for (String s : arr){
	       		//System.out.println(s);
	       		if (b) {
	       			order_no = s;
	       			break;
	       		}
	       		else if (s.equals("reference"))
	       			b = true;
	       	}
	       	//System.out.println(order_no);
	       	driver.findElement(By.cssSelector("#center_column p a")).click(); //back_to_orders btn
	       	
	       	//driver.findElement(By.xpath("//*[text()[contains(.,order_no)]]"))
	       	String pg_src = driver.getPageSource(); //THIS WORKS, BUT NOT PREFERRED...
	       	Assert.assertTrue(pg_src.contains(order_no));
		}
		catch (Exception | AssertionError e ){
			error = true;
			errorMsg = e.toString();
			throw e;
		}
	}

	//------------------------------------------------------------------------------------
	//private helpers
	//------------------------------------------------------------------------------------
	/**
	 * Execute a bash command. We can handle complex bash commands including
	 * multiple executions (; | && ||), quotes, expansions ($), escapes (\), e.g.:
	 *     "cd /abc/def; mv ghi 'older ghi '$(whoami)"
	 * @param command
	 * @return true if bash got started, but your command may have failed.
	 */
	private boolean executeBashCommand(String command) {
	    boolean success = false;
	    System.out.println("Executing BASH command:\n   " + command);
	    Runtime r = Runtime.getRuntime();
	    // Use bash -c so we can handle things like multi commands separated by ; and
	    // things like quotes, $, |, and \. My tests show that command comes as
	    // one argument to bash, so we do not need to quote it to make it one thing.
	    // Also, exec may object if it does not have an executable file as the first thing,
	    // so having bash here makes it happy provided bash is installed and in path.
	    String[] commands = {"bash", "-c", command};
	    try {
	        Process p = r.exec(commands);

	        p.waitFor();
	        BufferedReader b = new BufferedReader(new InputStreamReader(p.getInputStream()));
	        String line = "";

	        while ((line = b.readLine()) != null) {
	            System.out.println(line);
	        }

	        b.close();
	        success = true;
	    } catch (Exception e) {
	        System.err.println("Failed to execute bash with command: " + command);
	        e.printStackTrace();
	    }
	    return success;
	}

	private void step1_submitEmail(String email_address){
		driver.findElement(By.id("email_create")).sendKeys(email_address);
		driver.findElement(By.id("SubmitCreate")).click();
	}

	private enum Gender {NONE, MR, MRS};
	private void step2_submitCompleteForm(Gender g,
										 String customer_firstname,
										 String customer_lastname,
										 String email,
										 String passwd,
										 String days,
										 String months,
										 String years,
										 boolean newsletter,
										 boolean optin,
										 String firstname,
										 String lastname,
										 String company,
										 String address1,
										 String address2,
										 String city,
										 String id_state,
										 String postcode,
										 String id_country,
										 String other,
										 String phone,
										 String phone_mobile,
										 String alias){

			if (g == Gender.MR)
				driver.findElement(By.id("id_gender1")).click();
			else if (g == Gender.MRS)
				driver.findElement(By.id("id_gender2")).click();

	 		driver.findElement(By.id("customer_firstname")).sendKeys(customer_firstname);
			driver.findElement(By.id("customer_lastname")).sendKeys(customer_lastname);
			driver.findElement(By.id("email")).sendKeys(email);
			driver.findElement(By.id("passwd")).sendKeys(passwd);

			driver.findElement(By.id("days")).sendKeys(days);
			driver.findElement(By.id("months")).sendKeys(months);
			driver.findElement(By.id("years")).sendKeys(years);
	 		
	 		
	 		WebElement e1 = driver.findElement(By.id("newsletter"));
	 		if ((newsletter & !e1.isSelected()) || (!newsletter & e1.isSelected()))
	 			e1.click();
	 		WebElement e2 = driver.findElement(By.id("optin"));
			if ((optin & !e2.isSelected()) || (!optin & e2.isSelected()))
	 			e2.click();


	 		driver.findElement(By.id("firstname")).sendKeys(firstname);
	 		driver.findElement(By.id("lastname")).sendKeys(lastname);
	 		driver.findElement(By.id("company")).sendKeys(company);
	 		driver.findElement(By.id("address1")).sendKeys(address1);
	 		driver.findElement(By.id("address2")).sendKeys(address2);
	 		driver.findElement(By.id("city")).sendKeys(city);
	 		driver.findElement(By.id("id_state")).sendKeys(id_state);
	 		driver.findElement(By.id("postcode")).sendKeys(postcode);
	 		driver.findElement(By.id("id_country")).sendKeys(id_country);
	 		driver.findElement(By.id("other")).sendKeys(other);
	 		driver.findElement(By.id("phone")).sendKeys(phone);
	 		driver.findElement(By.id("phone_mobile")).sendKeys(phone_mobile);
	 		driver.findElement(By.id("alias")).sendKeys(alias);
	 		driver.findElement(By.id("submitAccount")).click();
	}

	private void login(String email, String password){
		driver.findElement(By.id("email")).sendKeys(email);
		driver.findElement(By.id("passwd")).sendKeys(password);
		driver.findElement(By.id("SubmitLogin")).click();
	}

}
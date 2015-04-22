import org.openqa.selenium.WebDriver;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.openqa.selenium.support.*;
import org.openqa.selenium.support.ui.Select;

//import org.testng.annotations.*;
//import org.testng.Assert;

//class variables & @BeforeClass and @AfterClass 
//need to be static for junit, but not for TestNG
import org.junit.Test;
import org.junit.Assert;
import org.junit.*;
import java.util.concurrent.TimeUnit;
import java.util.*;



public class LibertyTests{

	private static WebDriver driver;
	public static LibertyActions actions;
	public static String url;

	@BeforeClass
	public static void setUp(){}

	@AfterClass
	public static void tearDown(){}

	@Before
	public void b4_test(){
		//String chrome_path = "C:\\Documents and Settings\\chuck\\Desktop\\shri\\Development\\test_tools\\selenium\\chromedriver.exe";
		//System.setProperty("webdriver.chrome.driver", chrome_path);
		//driver = new ChromeDriver();
		
		driver = new FirefoxDriver();
		actions = PageFactory.initElements(driver, LibertyActions.class);
		driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
		driver.manage().deleteAllCookies();
		Set cookies = driver.manage().getCookies(); 
		Assert.assertEquals(cookies.size(), 0);
		url = "https://us.battle.net/account/creation/tos.html";
		driver.get(url);

	}

	@After
	public void after_test() throws Exception{
		//driver.quit();
	}


	@Test 
	public void invoke_happy_path()throws Exception{
		//need to refactor this into a fill_form method
		actions.selectCountry("USA"); 		
		actions.selectDay("31");
		actions.selectMonth("3");
		actions.selectYear("1976"); //must be 18 yrs old to register?
		actions.firstname.sendKeys("tom");
		actions.lastname.sendKeys("cramps");
		actions.email.sendKeys("tom.cramps@gmail.com");
		actions.confirm_email.sendKeys("tom.cramps@gmail.com");
		actions.password.sendKeys("flower45");
		actions.confirm_password.sendKeys("flower45");
		actions.selectQuestion("What was the first car you owned?");
		actions.answer.sendKeys("geo");
		if (!actions.isTermsOfServiceChecked())
			actions.terms_checkbox.click();
		if (!actions.isSignupChecked())
			actions.signup_checkbox.click();
		actions.submit_btn.click();
		Assert.assertTrue(driver.getPageSource().contains("Account Creation Successful!"));
	}

	@Ignore
	@Test
	public void invoke_email_as_username_tip() throws Exception {
		Assert.assertFalse(actions.email_as_username_tip.isDisplayed());
		actions.email.click();
		Assert.assertTrue(actions.email_as_username_tip.isDisplayed());
	}

	@Ignore
	@Test 
	public void invoke_invalid_email_tip()throws Exception{
		Assert.assertFalse(actions.email_invalid_tip.isDisplayed());
		actions.email.sendKeys("fasdfsd\t");
		Assert.assertTrue(actions.email_invalid_tip.isDisplayed());
	}

	@Ignore
	@Test 
	public void invoke_email_mismatch_tip()throws Exception{
		Assert.assertFalse(actions.email_mismatch_tip.isDisplayed());
		actions.email.sendKeys("shri.amin@gmail.com");
		actions.confirm_email.sendKeys("shri.amin@gmail.cm\t");
		Assert.assertTrue(actions.email_mismatch_tip.isDisplayed());
	}
	
	@Ignore
	@Test
	public void invoke_password_strength_dialog() throws Exception {
		Assert.assertFalse(actions.password_assist_dialog.isDisplayed());
		actions.password.click();
		Assert.assertTrue(actions.password_assist_dialog.isDisplayed());
	}

	@Ignore
	@Test
	public void invoke_answer_tip() throws Exception {
		Assert.assertFalse(actions.acct_security_tip.isDisplayed());
		actions.answer.click();
		Assert.assertTrue(actions.acct_security_tip.isDisplayed());
	}

	@Ignore
	@Test
	public void invoke_change_country_dialog() throws Exception {
		Assert.assertFalse(actions.change_country_btn.isDisplayed());
		Assert.assertFalse(actions.cancel_country_btn.isDisplayed());
		actions.selectCountry("FRA"); //france
		Assert.assertTrue(actions.change_country_btn.isDisplayed());
		Assert.assertTrue(actions.cancel_country_btn.isDisplayed());
	}

	@Ignore
	@Test 
	public void invoke_form_submission_error()throws Exception{
		Assert.assertFalse(actions.form_submission_error.isDisplayed());
		actions.submit_btn.click();
		Assert.assertTrue(actions.form_submission_error.isDisplayed());
	}

	@Ignore
	@Test
	public void invoke_terms_of_use_page() throws Exception{
		//state of terms checkbox prior to click
		Assert.assertFalse(actions.isTermsOfServiceChecked());
		actions.terms_link.click();
		String mainWindow = driver.getWindowHandle();
		//Switch to new window opened
		for(String winHandle : driver.getWindowHandles()){
    		driver.switchTo().window(winHandle);
		}	
		url = "http://us.blizzard.com/en-us/company/about/termsofuse.html"; //default country
		Assert.assertEquals(driver.getCurrentUrl(), url);
		//Switch back to the main window
		driver.switchTo().window(mainWindow);
		//state of terms checkbox post click
		Assert.assertTrue(actions.isTermsOfServiceChecked());
	}
}
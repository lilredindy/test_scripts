import org.openqa.selenium.WebDriver;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.openqa.selenium.support.*;
import org.openqa.selenium.Dimension;
import org.openqa.selenium.support.ui.*;
//import org.testng.annotations.*;
//import org.testng.Assert;

import org.junit.Test;
import org.junit.Assert;
import org.junit.*;
import java.util.*;


public class ForthEstateAcceptanceTests {
	 
	private static WebDriver driver;
	private static ForthEstateActions actions;
 	private static String contact_page_url = "http://forthestate.com/contact";
      

	@BeforeClass
	public static void setUp(){  //class method setUp must be declared static for junit
		driver = new FirefoxDriver();
		actions = PageFactory.initElements(driver, ForthEstateActions.class);
		//driver.get(contact_page_url);

	}
	 
	@AfterClass
	public static void tearDown(){ //class method tearDown must be declared static for junit
		//driver.quit();
	}
	 
	@Before
	public void DeleteCookiesAndOpenWindow(){
		driver.manage().deleteAllCookies();
		Set cookies  = driver.manage().getCookies(); 
		Assert.assertEquals(cookies.size(), 0);

		driver.get(contact_page_url);
		Assert.assertEquals(driver.getCurrentUrl(), contact_page_url);
	}


	////////////////////////
	//  Tests 
	/////////////////////////

/*
	@Test
	public void CheckIfCookiesExist() throws Exception{
		Set cookies  = driver.manage().getCookies(); 
		Assert.assertEquals(cookies.size(), 0);
	}*/

	

	@Test @Ignore
	public void CheckWebpageResponseCode()throws Exception{

	 }

	@Test 
	public void CheckForPageHeaderText()throws Exception{

		Assert.assertEquals(actions.newsletter_heading.getText(), "Forth Estate Newsletter");

	 }

	@Test 
	public void CheckForEmailInputLabel()throws Exception{

		Assert.assertEquals(actions.email_input_label.getText(), "Email Address");

	 }

	@Test 
	public void CheckForEmailInputBox()throws Exception{

		Assert.assertTrue(actions.email_input_field.isDisplayed());

	 }

	@Test @Ignore
	public void CheckForEmailInputBoxSizeRequirement()throws Exception{

		Dimension d = actions.email_input_field.getSize();
		System.out.println("width: " +  d.width);

	 }

	@Test 
	public void CheckForFormSubmitButton()throws Exception{

		Assert.assertTrue(actions.email_input_field.isDisplayed());

	 }

	@Test @Ignore
	public void SubscribeWithUnverifiedEmail()throws Exception{

		Assert.assertFalse (actions.subscribe_msg_success.isDisplayed());
		actions.email_input_field.sendKeys("foo@foo.com"); //need to generate a fake email address
		actions.email_subscribe_btn.click();
		Assert.assertTrue (actions.subscribe_msg_success.isDisplayed());
	 }

	@Test 
	public void SubscribeWithVerifiedEmail()throws Exception{

		//NOTE:  REGISTERed implies user clicked on verification link sent via email

		Assert.assertFalse (actions.subscribe_msg_error.isDisplayed());
		actions.email_input_field.sendKeys("shri.amin@gmail.com"); 
		actions.email_subscribe_btn.click();
		Assert.assertTrue (actions.subscribe_msg_error.isDisplayed());
	 }

	@Test 
	public void SubscribeWithInvalidEmail1()throws Exception{

		//Assert.assertFalse (actions.invalid_email_err_msg.isDisplayed());
		actions.email_input_field.sendKeys("shri.amin@gmail,com"); 
		actions.email_subscribe_btn.click();
		Assert.assertTrue (actions.invalid_email_err_msg.isDisplayed());
	 }

	@Test 
	public void SubscribeWithInvalidEmail2()throws Exception{

		//Assert.assertFalse (actions.invalid_email_err_msg.isDisplayed());
		actions.email_input_field.sendKeys("shri.amin"); 
		actions.email_subscribe_btn.click();
		Assert.assertTrue (actions.invalid_email_err_msg.isDisplayed());
	 }

	 @Test 
	public void SubscribeWithInvalidEmail3()throws Exception{
		
		//Assert.assertFalse (actions.invalid_email_err_msg.isDisplayed());
		actions.email_input_field.sendKeys(""); 
		actions.email_subscribe_btn.click();
		Assert.assertTrue (actions.invalid_email_err_msg.isDisplayed());
	 }



	 //Contact Tests
	@Test 
	public void CheckForPageHeaderText2()throws Exception{

		Assert.assertEquals(actions.newsletter_heading.getText(), "Contact");

	 }
}

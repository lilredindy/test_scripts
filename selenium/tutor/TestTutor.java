import org.openqa.selenium.WebDriver;

import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.*;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.testng.annotations.*;
import org.testng.Assert;
import java.util.concurrent.TimeUnit;


public class TestTutor
{
WebDriver driver;
AboutUsPage aboutus_page;
LoginPage login_page;

@BeforeClass
public void setUp(){
	System.out.println("before class - setup");

	driver = new FirefoxDriver();

	aboutus_page = PageFactory.initElements(driver, AboutUsPage.class);
	login_page = PageFactory.initElements(driver, LoginPage.class);

}
 
@AfterClass
public void tearDown(){
	System.out.println("after class - tear down");
	driver.quit();
}


@Test 
public void clickAwards(){
	System.out.println("test - click awards");

	driver.get("http://www.tutor.com/our-company");
	aboutus_page.a.click();

}

@Test 
public void testSuccessfulLogin(){
	System.out.println("test - success login");

	driver.get("https://www.tutor.com/account/login.aspx");
	login_page.login("shri.amin@gmail.com","flower45");
	//test is something displayed? or get the next page and check for title?
}

@Test 
public void testBadLogin(){
	System.out.println("test - bad login");

	driver.get("https://www.tutor.com/account/login.aspx");
	login_page.login("shri.amin@gmail.com","flower");
	Assert.assertTrue(login_page.error_msg.isDisplayed());
}

@Test
public void testEmptyFields(){
	System.out.println("test - empty fields");

	driver.get("https://www.tutor.com/account/login.aspx");
	Assert.assertEquals(login_page.textField1.getText(), "");
	Assert.assertEquals(login_page.textField2.getText(), "");
}

}

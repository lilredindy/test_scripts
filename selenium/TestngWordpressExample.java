import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.testng.Assert;
import org.testng.annotations.*;

//import org.openqa.selenium.remote.DesiredCapabilities;
//import org.openqa.selenium.remote.RemoteWebDriver;
//import java.net.*;
 
public class TestngWordpressExample {
 
// create a WebDriver
WebDriver driver;
 
// use the Firefox browser and go to the wikipedia site
@BeforeClass
public void setUp() throws Exception{
driver = new FirefoxDriver();
//driver = new RemoteWebDriver(new URL("http://127.0.0.1:4444/wd/hub"), DesiredCapabilities.firefox());

}
 
// quit from WebDriver
@AfterClass
public void tearDown(){
driver.quit();
}


@Test(description="Launches the WordPress site")
public void launchSite(){
driver.get("http://demo.opensourcecms.com/wordpress/wp-admin");
Assert.assertEquals(driver.getTitle(), "WordPress Demo Install › Log In");
}
 
@Test(description="Enters valid login data")
public void loginAsAdmin() {
  
WebElement userid = driver.findElement(By.id("user_login"));
userid.sendKeys("admin");

WebElement password = driver.findElement(By.id("user_pass"));
password.sendKeys("demo123");

WebElement submit = driver.findElement(By.id("wp-submit"));
submit.click();
Assert.assertEquals(driver.getTitle(), "Edit Post ‹ WordPress Demo Install — WordPress");

}

/*
@Test(description="Navigates to the New Post screen")
public void navigateNewPost() {
  selenium.click("//a[contains(text(),'Posts')]/following::a[contains(text(),'Add New')][1]");
  selenium.waitForPageToLoad("30000");
  assertTrue(selenium.isTextPresent("Add New Post"));
}
  
@Test(description="Writes the new post")
public void writeBlogPost() {
  selenium.type("title", "New Blog Post");
  selenium.click("edButtonHTML");
  selenium.type("content", "This is a new post");
  //TODO:Assert
}
  
@Test(description="Publishes the post")
public void publishBlogPost() {
  selenium.click("submitdiv");
  selenium.click("publish");
  selenium.waitForPageToLoad("30000");
  assertTrue(selenium.isTextPresent("Post published."));
}
  
@Test(description="Verifies the post")
public void verifyBlogPost() {
  selenium.click("//a[contains(text(),'Posts') and contains(@class,'wp-first-item')]");
  selenium.waitForPageToLoad("30000");
  assertTrue(selenium.isElementPresent("//a[text()='New Blog Post']"));
}
  
@Test(description="Logs out")
public void logout() {
  selenium.click("//a[text()='Log Out']");
  //TODO:Assert
}
*/

}
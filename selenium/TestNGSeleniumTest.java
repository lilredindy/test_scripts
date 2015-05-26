import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.testng.annotations.*;
import org.testng.Assert;
 
public class testNGSeleniumTest {
 
// create a WebDriver
WebDriver driver;
 
// use the Firefox browser and go to the wikipedia site
@BeforeClass
public void setUp(){
driver = new FirefoxDriver();
driver.get("http://en.wikipedia.org/wiki/Main_Page");
}
 
// quit from WebDriver
@AfterClass
public void tearDown(){
driver.quit();
}
 
@Test
public void testFindElements()throws Exception{
 
//find the About link
WebElement about= driver.findElement(By.xpath("//*[@id='n-aboutsite']/a"));
 
// click to the link
about.click();
 
// wait for 5 seconds
Thread.sleep(5000);
 
// write out the title of the page in console
System.out.println(driver.getTitle());
}

}
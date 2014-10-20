import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
//import org.testng.annotations.*;
//import org.testng.Assert;
import org.junit.Test;
import org.junit.Assert;
import org.junit.*;
import org.openqa.selenium.support.ui.*;
import java.util.*;

public class JunitDropdownTest {
 
// create a WebDriver
private static WebDriver driver;
 
// use the Firefox browser and go to the wikipedia site
@BeforeClass
public static void setUp(){
driver = new FirefoxDriver();
driver.get("http://localhost:7272/person.html");
}
 
// quit from WebDriver
@AfterClass
public static void tearDown(){
//driver.quit();
}
 
@Test
public void findPersonPeterGriffin()throws Exception{
 
	String bodyText = driver.findElement(By.tagName("body")).getText();
	Assert.assertTrue(bodyText.contains("Peter Griffin"));
}

@Test
public void selectThirdPersonFromList() throws Exception{

	WebElement opt3 = driver.findElement(By.cssSelector("body > form:nth-child(1) > select:nth-child(1) > option:nth-child(4)"));
	opt3.click();

	Assert.assertTrue(opt3.isSelected());

}

@Test
public void verifyAllPersonsInList() throws Exception{
	Select s = new Select(driver.findElement(By.name("users")));
	List<WebElement> persons = s.getOptions();
	Assert.assertEquals(persons.size(), 5);

}

@Test
public void verifyUserIsShown() throws Exception{
	Select s = new Select(driver.findElement(By.name("users")));
	s.selectByValue("4");

	WebDriverWait wait = new WebDriverWait(driver, 0000);
	WebElement eTable = wait.until(ExpectedConditions.presenceOfElementLocated(By.tagName("table")));
	// wait for 5 seconds
	//Thread.sleep(5000);
	
	//WebElement eTable = driver.findElement(By.id("txtHint"));
	String tableText = eTable.getText();
	System.out.println(tableText);
	Assert.assertTrue(tableText.contains("Joseph"));
}

}
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
driver.get("http://localhost:7272/person_dropdown/person.html");
}
 
// quit from WebDriver
@AfterClass
public static void tearDown(){
driver.quit();
}
 
@Test @Ignore
public void verifyTitleText() throws Exception{
	WebElement title = driver.findElement(By.tagName("title"));
	Assert.assertEquals(title, "this_title");
}

@Test
public void findPersonPeterGriffin()throws Exception{
 
	String bodyText = driver.findElement(By.tagName("body")).getText();
	Assert.assertTrue(bodyText.contains("Peter Griffin"));
}

@Test
public void selectThirdPersonFromList() throws Exception{

	WebElement opt3 = driver.findElement(By.cssSelector("option[value='3']"));
	opt3.click();
	Assert.assertEquals(opt3.getText(), "Lois Griffin");
}

@Test
public void verifyNumOfPersonsInList() throws Exception{
	Select s = new Select(driver.findElement(By.name("users")));
	List<WebElement> persons = s.getOptions();
	Assert.assertEquals(persons.size(), 5);
}

@Test
public void verifyNumOfPersonsInList2() throws Exception{
	WebElement u = (driver.findElement(By.name("users")));
	List<WebElement> persons = u.findElements(By.tagName("option"));
	Assert.assertEquals(persons.size(), 5);
}

@Test
public void verifyUserOutputIsShown() throws Exception{
	Select s = new Select(driver.findElement(By.name("users")));
	s.selectByValue("4");

	WebDriverWait wait = new WebDriverWait(driver, 5000);
	WebElement eTable = wait.until(ExpectedConditions.presenceOfElementLocated(By.tagName("table")));
	// wait for 5 seconds
	//Thread.sleep(5000);
	
	//WebElement eTable = driver.findElement(By.id("txtHint"));
	String tableText = eTable.getText();
	System.out.println(tableText);
	Assert.assertTrue(tableText.contains("joseph"));
}

}
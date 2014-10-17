import org.openqa.selenium.WebDriver;
import org.openqa.selenium.By;

import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.*;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.testng.annotations.*;
import org.testng.Assert;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.support.ui.ExpectedConditions;



public class GrubHubTests
{

WebDriver driver;
GrubHubActions actions;
WebDriverWait wait;

@BeforeClass
public void setUp(){
	System.out.println("before class - setup");

	driver = new FirefoxDriver();
	actions = PageFactory.initElements(driver, GrubHubActions.class);
	wait = new WebDriverWait(driver, 10);
}
 

@AfterClass
public void tearDown(){
	System.out.println("after class - tear down");
	//driver.quit();
}


@Test 
public void registration(){
	System.out.println("test - registration");

	driver.get("https://www.grubhub.com/");	
	actions.create_account("crap1111@mailinator.com","flower45");
	
	//wait for the registration to process
	wait.until(ExpectedConditions.elementToBeClickable(actions.logged_in_link)); 

	Assert.assertEquals(actions.logged_in_link.isDisplayed(),true);
}


@Test
public void login(){
	System.out.println("test - login");

	driver.get("https://www.grubhub.com/");	
	actions.login("crap1111@mailinator.com","flower45");

	//wait for the login to process
	wait.until(ExpectedConditions.elementToBeClickable(actions.logged_in_link)); 

	Assert.assertEquals(actions.logged_in_link.isDisplayed(),true);	
}

@Test
public void search_exact_location_found(){
	System.out.println("test - single address match");

	driver.get("https://www.grubhub.com/");	
	actions.search("South Orange, NJ", "pizza");
	
	Assert.assertEquals(driver.getCurrentUrl(),"https://www.grubhub.com/search/South_Orange,_NJ/?searchTerm=pizza&filters=openNow");	

}

@Test
public void search_multiple_location_found(){
	System.out.println("test - multiple address match");

	driver.get("https://www.grubhub.com/");	
	actions.search("10 Ford Ave", "pizza");
	
	Assert.assertEquals(driver.getCurrentUrl(),"https://www.grubhub.com/search/10%20Ford%20Ave/?searchTerm=pizza&filters=openNow");
	Assert.assertEquals(driver.getPageSource().contains("We found more than one match for"), true);	
}

@Test
public void search_with_zipcode(){
	System.out.println("test - search with zipcode");

	driver.get("https://www.grubhub.com/");	
	actions.search("08857", "pizza");
	
	Assert.assertEquals(driver.getCurrentUrl(),"https://www.grubhub.com/?errMsg=search.cannot_geocode&searchAddressStr=08857");	
}

@Test
public void logged_in_links(){
	System.out.println("test - logged in links");

	driver.get("https://www.grubhub.com/");	
	actions.login("crap1111@mailinator.com","flower45");
	//wait for the registration to process
	wait.until(ExpectedConditions.elementToBeClickable(actions.logged_in_link)); 
	actions.logged_in_link.click();
	actions.your_grubhub_link.click();
	wait.until(ExpectedConditions.elementToBeClickable(actions.orders_btn)); 
	actions.orders_btn.click();
	Assert.assertEquals(driver.getCurrentUrl(),"https://www.grubhub.com/yourGrubHub/pastOrders.action");	

	//this test is incomplete due to timing problems (prob cuz ajax) and some css id issues
}

@Test
public void place_order(){
	System.out.println("test - place an order");

	driver.get("https://www.grubhub.com/");	
	actions.search("Jersey City, NJ", "");
	WebElement thai_food = wait.until(ExpectedConditions.elementToBeClickable(driver.findElement(By.xpath("/html/body/div[3]/div[2]/div[6]/div[1]/ol/li[3]/img")))); 
	thai_food.click();
	WebElement nanking = wait.until(ExpectedConditions.elementToBeClickable(driver.findElement(By.linkText("Nanking")))); 
	nanking.click();
	WebElement butter_nan = wait.until(ExpectedConditions.elementToBeClickable(driver.findElement(By.linkText("Butter Nan")))); 
	butter_nan.click();
	WebElement add_item_btn = wait.until(ExpectedConditions.elementToBeClickable(driver.findElement(By.linkText("Add Item")))); 
	add_item_btn.click();
}

}

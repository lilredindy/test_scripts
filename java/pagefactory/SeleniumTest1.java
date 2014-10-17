package test.selenium.pagefactory;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.*;

public class SeleniumTest1 {
	WebDriver driver;
	
	@FindBy(how = How.ID, using = "id-012")
	WebElement verifybutton;

	public SeleniumTest1(WebDriver driver) {
		this.driver = driver;
		
		// you may Check title of the page and assert if page title is incorrect
        System.out.println("Page title is: " + driver.getTitle());
	}
	
	public void clickButtonPresentByID_id012() {
		verifybutton.click();
	}

	// Find and click selenium-test2
	public SeleniumTest2 clickSeleniumTest2() {
		// Find the text link by its name
		WebElement someElement = driver.findElement(By.linkText("selenium-test2"));
		
		// Click the link text
		someElement.click();
		
		return PageFactory.initElements(driver, SeleniumTest2.class);
	}
	
	// Find and click selenium-test3

}
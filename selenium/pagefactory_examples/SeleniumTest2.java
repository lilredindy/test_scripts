package test.selenium.pagefactory;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.*;

public class SeleniumTest2 {
	WebDriver driver;
	
	@FindBy(how = How.ID, using = "q2")
	WebElement textBox;

	public SeleniumTest2(WebDriver driver) {
		this.driver = driver;
		
		// you may Check title of the page and assert if page title is incorrect
        System.out.println("Page title is: " + driver.getTitle());
	}
	
	// Find the text box by ID
	public void inputTextBox(String txt) {
		textBox.clear();
		textBox.sendKeys(txt);
	}
	
	// Find and click selenium-test1
	public SeleniumTest1 clickSeleniumTest1() {
		// Find the text link by its name
		WebElement someElement = driver.findElement(By.linkText("selenium-test1"));
		
		// Click the link text
		someElement.click();
		
		return new SeleniumTest1(driver);
	}
	
	// Find and click selenium-test3
}
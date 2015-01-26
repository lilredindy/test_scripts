import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import java.util.concurrent.TimeUnit;



public class moneyMediaTest {

	public static void main(String [] args) {

		WebDriver driver;

		driver = new FirefoxDriver();
		driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
		driver.get("http://www.financialadvisoriq.com/?login=1");
		driver.findElement(By.cssSelector("input#email.required.email")).sendKeys("hell");
		driver.quit();

	}


}
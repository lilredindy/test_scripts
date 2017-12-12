import org.openqa.selenium.*;
import org.openqa.selenium.support.*;

public class HistoryPage extends BasePage {
	
	HistoryPage (WebDriver driver) {
		super(driver);
		PageFactory.initElements(driver, this);
	}

	public void open(){
		driver.get("http://automationpractice.com/index.php?controller=history");
	}

	boolean orderFound(String order_no){  //quick and easy, but should parse table 
	    String pg_src = driver.getPageSource(); 
	   	return pg_src.contains(order_no);
	}

}
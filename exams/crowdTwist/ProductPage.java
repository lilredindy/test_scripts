import org.openqa.selenium.*;
import org.openqa.selenium.support.*;
import org.openqa.selenium.interactions.Actions;


public class ProductPage extends BasePage {
	
	@FindBy(css ="div#layer_cart a")WebElement confirmUpdatedCartBtn;

	ProductPage (WebDriver driver) {
		super(driver);
		PageFactory.initElements(driver, this);
	}

	public void open(){
		driver.get("http://automationpractice.com/index.php?id_category=5&controller=category");
	}

	public void addToCart (String productSelector){
		Actions action = new Actions(driver);
		action.moveToElement(driver.findElement(By.cssSelector(productSelector))).moveToElement(driver.findElement(By.cssSelector("a.ajax_add_to_cart_button"))).click().build().perform();
	}




}
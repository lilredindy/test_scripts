import org.openqa.selenium.*;
import org.openqa.selenium.support.*;

public class LoginPage extends BasePage {
	
	@FindBy(id = "email" )  WebElement emailTxtField;
	@FindBy(id = "passwd")  WebElement pwdTxtField;
	@FindBy(id = "SubmitLogin")  WebElement submitLoginBtn;


	LoginPage (WebDriver driver) {
		super(driver);
		PageFactory.initElements(driver, this);
	}

	public void open(){
		driver.get("http://automationpractice.com/index.php?controller=authentication");
	}


	public void login (String email, String password){
		emailTxtField.sendKeys(email);
		pwdTxtField.sendKeys(password);
		submitLoginBtn.click();
	}


}
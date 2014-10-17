import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.*;


public class LoginPage
{

//a list of elements

	@FindBy(how = How.ID, using = "ctl00_content_lg_txtEmail") WebElement textField1;
	@FindBy(how = How.ID, using = "ctl00_content_lg_txtPassword") WebElement textField2;
	@FindBy(how = How.ID, using = "ctl00_content_lg_btnSignIn") WebElement button;
	@FindBy(how = How.ID, using = "ctl00_content_lg_ErrorMsg") WebElement error_msg;


//procedures
public void login(String username, String password){
	textField1.sendKeys(username);
	textField2.sendKeys(password);
	button.click();
}

}
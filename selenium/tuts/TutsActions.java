//Actions
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.*;


public class TutsActions {

	//create account
	@FindBy(how = How.ID, using ="user_login") WebElement text_field;
	@FindBy(how = How.CLASS_NAME, using ="user-form__button") WebElement submit_btn;


	public void SendPasswordResetVerficationLink() {
		this.text_field.sendKeys("shri.amin@gmail.com");
		this.submit_btn.click();
	}


}


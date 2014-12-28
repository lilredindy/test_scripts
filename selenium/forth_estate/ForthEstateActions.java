//Actions
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.*;



public class ForthEstateActions {
/*
CLASS_NAME 
CSS 
ID 
ID_OR_NAME 
LINK_TEXT 
NAME 
PARTIAL_LINK_TEXT 
TAG_NAME 
XPATH 
*/


	//Newsletter
	@FindBy(how = How.CSS, using ="div.mc-field-group label") WebElement email_input_label;
	@FindBy(how = How.CSS, using ="div#newsletter div.h1") WebElement newsletter_heading;
	@FindBy(how = How.ID, using ="mce-EMAIL") WebElement email_input_field;
	@FindBy(how = How.ID, using ="mc-embedded-subscribe") WebElement email_subscribe_btn;
	@FindBy(how = How.ID, using ="mce-success-response") WebElement subscribe_msg_success;
	@FindBy(how = How.ID, using ="mce-error-response") WebElement subscribe_msg_error;
	@FindBy(how = How.CSS, using="div.mce_inline_error") WebElement invalid_email_err_msg;

	//Contact Us
	@FindBy(how = How.ID, using ="div#contact div.h1") WebElement contact_heading;




	public void generateNewEmailAddress(){}

	/*
	private boolean isElementPresent(String using){
		boolean present;
		try {
		   driver.findElement(By.id(""));
		   present = true;
		} catch (NoSuchElementException e) {
		   present = false;
		}
	}
	*/

}




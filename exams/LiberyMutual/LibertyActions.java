import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.*;
import org.openqa.selenium.support.ui.Select;

import java.util.*;


public class LibertyActions
{
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

	@FindBy(how = How.ID, using ="country") WebElement country;
	@FindBy(how = How.ID, using ="dobMonth") WebElement month;
	@FindBy(how = How.ID, using ="dobDay") WebElement day;
	@FindBy(how = How.ID, using ="dobYear") WebElement year;
	@FindBy(how = How.ID, using ="firstname") WebElement firstname;
	@FindBy(how = How.ID, using ="lastname") WebElement lastname;
	@FindBy(how = How.ID, using ="emailAddress") WebElement email;
	@FindBy(how = How.ID, using ="emailAddressConfirmation") WebElement confirm_email;
	@FindBy(how = How.ID, using ="password") WebElement password;
	@FindBy(how = How.ID, using ="rePassword") WebElement confirm_password;
	@FindBy(how = How.ID, using ="question1") WebElement question;
	@FindBy(how = How.ID, using ="answer1") WebElement answer;
	@FindBy(how = How.ID, using ="captcha") WebElement captcha;
	@FindBy(how = How.ID, using ="agreedToToU-link") WebElement terms_checkbox;
	@FindBy(how = How.LINK_TEXT, using = "Terms of Use") WebElement terms_link;
	@FindBy(how = How.ID, using ="blizzardNewsletter-link") WebElement signup_checkbox;
	@FindBy(how = How.ID, using ="creation-submit") WebElement submit_btn;
	@FindBy(how = How.CLASS_NAME, using ="ui-cancel") WebElement cancel_btn;

	//ajax elements
	@FindBy(how = How.CSS, using ="#countryGlobal span.button-right") WebElement change_country_btn;
	@FindBy(how = How.CSS, using ="#countryGlobal a.ui-cancel") WebElement cancel_country_btn;
	@FindBy(how = How.CSS, using ="div#password-strength p.caption") WebElement password_assist_dialog;
	@FindBy(how = How.CSS, using ="div.alert.error div.alert-message") WebElement form_submission_error;	
	@FindBy(how = How.CSS, using ="span#emailAddress-message span.tip-information") WebElement email_as_username_tip;	
	@FindBy(how = How.CSS, using ="span#emailAddress-message span.tip-warning") WebElement email_invalid_tip;	
	@FindBy(how = How.CSS, using ="span#emailAddressConfirmation-message span.tip-warning") WebElement email_mismatch_tip;	
	@FindBy(how = How.CSS, using ="div#question-info span.tip-information") WebElement acct_security_tip;	


	/*///////////
	//procedures
	*////////////

	public void selectCountry(int index){
		Select s = new Select(this.country);
		s.selectByIndex(index);
	}

	public void selectCountry(String value){
		Select s = new Select(this.country);
		selectUsingOptionValue(s, value);
		//s.selectByValue(value);
	}

	public void selectDay(int index){
		Select s = new Select(this.day);
		s.selectByIndex(index);
	}

	public void selectDay(String value){
		Select s = new Select(this.day);
		selectUsingOptionValue(s, value);
	}

	public void selectMonth(int index){
		Select s = new Select(this.month);
		s.selectByIndex(index);
	}

	public void selectMonth(String value){
		Select s = new Select(this.month);
		selectUsingOptionValue(s, value);
	}
	
	public void selectYear(int index){
		Select s = new Select(this.year);
		s.selectByIndex(index);
	}

	public void selectYear(String value){
		Select s = new Select(this.year);
		selectUsingOptionValue(s, value);
	}

	public void selectQuestion(int index){
		Select s = new Select(this.question);
		s.selectByIndex(index);
	}

	public void selectQuestion(String text){
		Select s = new Select(this.question);
		selectUsingOptionText(s, text);
	}

	public boolean isTermsOfServiceChecked(){
		String s = this.terms_checkbox.getAttribute("class");
		return s.contains("input-checkbox-checked");
	}

	public boolean isSignupChecked(){
		String s = this.signup_checkbox.getAttribute("class");
		return s.contains("input-checkbox-checked");
	}

	private void selectUsingOptionValue(Select s, String value){
		List<WebElement> options = s.getOptions();
		for (WebElement option: options)
			if (option.getAttribute("value").equals(value))
				option.click();
	}

	private void selectUsingOptionText(Select s, String text){
		List<WebElement> options = s.getOptions();
		for (WebElement option: options)
			if (option.getText().equals(text))
				option.click();
	}

}
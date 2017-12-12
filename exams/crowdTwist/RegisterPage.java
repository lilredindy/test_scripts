

import org.openqa.selenium.*;
import org.openqa.selenium.support.*;

public class RegisterPage extends BasePage {
	
	@FindBy(id = "email_create")  WebElement registerEmailTxtField;
	@FindBy(id = "SubmitCreate")  WebElement submitRegisterEmailBtn;

	@FindBy(id = "id_gender1")  WebElement MR_RadioBtn;
	@FindBy(id = "id_gender2")  WebElement MRS_RadioBtn;
	@FindBy(id = "customer_firstname")  WebElement customerFirstNameTxtField;
	@FindBy(id = "customer_lastname")  WebElement customerLastNameTxtField;
	@FindBy(id = "email")  WebElement emailTxtField;
	@FindBy(id = "passwd")  WebElement passwordTxtField;
	@FindBy(id = "days")  WebElement daysDropdown;
	@FindBy(id = "months")  WebElement monthsDropdown;
	@FindBy(id = "years")  WebElement yearsDropdown;
	@FindBy(id = "newsletter")  WebElement newsletterCheckbox;
	@FindBy(id = "optin")  WebElement optinCheckbox;
	@FindBy(id = "firstname")  WebElement firstnameTxtField;
	@FindBy(id = "lastname")  WebElement lastnameTxtField;
	@FindBy(id = "company")  WebElement companyTxtField;
	@FindBy(id = "address1")  WebElement address1TxtField;
	@FindBy(id = "address2")  WebElement address2TxtField;
	@FindBy(id = "city")  WebElement cityTxtField;
	@FindBy(id = "id_state")  WebElement stateDropdown;
	@FindBy(id = "postcode")  WebElement postcodeTxtField;
	@FindBy(id = "id_country")  WebElement countryDropdown;
	@FindBy(id = "other")  WebElement otherTxtField;
	@FindBy(id = "phone")  WebElement phoneTxtField;
	@FindBy(id = "phone_mobile")  WebElement phoneMobileTxtField;
	@FindBy(id = "alias")  WebElement aliasTxtField;
	@FindBy(id = "submitAccount")  WebElement submitAccountBtn;


	RegisterPage (WebDriver driver) {
		super(driver);
		PageFactory.initElements(driver, this);
	}

	public void open(){
		driver.get("http://automationpractice.com/index.php?controller=authentication");
	}

	public void registerEmail(String email){
		registerEmailTxtField.sendKeys(email);
		submitRegisterEmailBtn.click();
	}

	public enum Gender {NONE, MR, MRS};

	public void registerFullForm(Gender g,
								 String customer_firstname,
								 String customer_lastname,
								 String email,
								 String passwd,
								 String days,
								 String months,
								 String years,
								 boolean newsletter,
								 boolean optin,
								 String firstname,
								 String lastname,
								 String company,
								 String address1,
								 String address2,
								 String city,
								 String id_state,
								 String postcode,
								 String id_country,
								 String other,
								 String phone,
								 String phone_mobile,
								 String alias){
				
				if (g == Gender.MR)
					MR_RadioBtn.click();
				else if (g == Gender.MRS)
					MRS_RadioBtn.click();

		 		customerFirstNameTxtField.sendKeys(customer_firstname);
				customerLastNameTxtField.sendKeys(customer_lastname);
				emailTxtField.sendKeys(email);
				passwordTxtField.sendKeys(passwd);

				daysDropdown.sendKeys(days);
				monthsDropdown.sendKeys(months);
				yearsDropdown.sendKeys(years);
		 		
		 		
		 		if ((newsletter & !newsletterCheckbox.isSelected()) || (!newsletter & newsletterCheckbox.isSelected()))
		 			newsletterCheckbox.click();
				if ((optin & !optinCheckbox.isSelected()) || (!optin & optinCheckbox.isSelected()))
		 			optinCheckbox.click();

		 		firstnameTxtField.sendKeys(firstname);
		 		lastnameTxtField.sendKeys(lastname);
		 		companyTxtField.sendKeys(company);
		 		address1TxtField.sendKeys(address1);
		 		address2TxtField.sendKeys(address2);
		 		cityTxtField.sendKeys(city);
		 		stateDropdown.sendKeys(id_state);
		 		postcodeTxtField.sendKeys(postcode);
		 		countryDropdown.sendKeys(id_country);
		 		otherTxtField.sendKeys(other);
		 		phoneTxtField.sendKeys(phone);
		 		phoneMobileTxtField.sendKeys(phone_mobile);
		 		aliasTxtField.sendKeys(alias);
		 		submitAccountBtn.click();
	}
}
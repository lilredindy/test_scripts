import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.*;


public class GrubHubActions
{

	//create account
	@FindBy(how = How.CLASS_NAME, using ="create-account-link") WebElement signup_link;
	@FindBy(how = How.CLASS_NAME, using ="email") WebElement signup_email_address;
	@FindBy(how = How.CLASS_NAME, using ="password") WebElement signup_password;
	@FindBy(how = How.CLASS_NAME, using ="primaryActionButton") WebElement signup_btn;

	//sign in
	@FindBy(how = How.CLASS_NAME, using = "login-link") WebElement login_link;
	@FindBy(how = How.ID, using = "login-email") WebElement login_email_address;
	@FindBy(how = How.ID, using = "login-password") WebElement login_password;
	@FindBy(how = How.CLASS_NAME, using = "primaryActionButton") WebElement login_btn;
	@FindBy(how = How.CLASS_NAME, using = "") WebElement forgot_link;

	//logged in menu (only available post- login/registration)
	@FindBy(how = How.CLASS_NAME, using = "status-loggedin") WebElement logged_in_link;
	@FindBy(how = How.LINK_TEXT, using = "Your GrubHub") WebElement your_grubhub_link;
	@FindBy(how = How.LINK_TEXT, using = "Account Info") WebElement acct_info_link;
	@FindBy(how = How.LINK_TEXT, using = "Yummy Rummy") WebElement yummy_rummy_link;
	@FindBy(how = How.CLASS_NAME, using = "logoutlink") WebElement logout_link;

	//search
	@FindBy(how = How.ID, using = "addressTop") WebElement address_txtField;
	@FindBy(how = How.ID, using = "itemTop") WebElement item_txtField;
	@FindBy(how = How.ID, using = "search") WebElement search_btn;

	//your GrubHub
	@FindBy(how = How.ID, using = "pastOrdersSeeAll") WebElement orders_btn;
	@FindBy(how = How.ID, using = "favoritesOrdersSeeAll") WebElement favs_btn;
	@FindBy(how = How.ID, using = "reviewsSeeAll") WebElement reviews_btn;



	//procedures
	public void create_account(String email, String password){
		this.signup_link.click();
		this.signup_email_address.sendKeys(email);
		this.signup_password.sendKeys(password);
		this.signup_btn.click();
	}

	public void login(String email, String password){
		this.login_link.click();
		this.login_email_address.sendKeys(email);
		this.login_password.sendKeys(password);
		this.login_btn.click();
	}

	public void logout(){
		this.logged_in_link.click();
		this.logout_link.click();
	}

	public void search(String address, String item){
		this.address_txtField.sendKeys(address);
		this.item_txtField.sendKeys(item);
		this.search_btn.click();
	}

}
import org.openqa.selenium.*;
import org.openqa.selenium.support.*;



class AccountPage extends BasePage {
	
	@FindBy(css = "a[title=\"Orders\"]") WebElement orderHistoryDetailBtn;
	@FindBy(css = "a[title=\"Credit slips\"]") WebElement myCreditSlipsBtn;
	@FindBy(css = "a[title=\"Addresses\"]") WebElement myAddressesBtn;
	@FindBy(css = "a[title=\"Information\"]") WebElement myPersonalInfoBtn;
	@FindBy(css = "a[title=\"My wishlists\"]") WebElement myWishListBtn ;


	AccountPage (WebDriver driver) {
		super(driver);
		PageFactory.initElements(driver, this);
	}

}
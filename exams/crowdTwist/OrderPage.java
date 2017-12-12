import org.openqa.selenium.*;
import org.openqa.selenium.support.*;

public class OrderPage extends BasePage {
	
	@FindBy(css ="p.cart_navigation a")  WebElement confirmSummaryBtn;
	@FindBy(css ="div#center_column form p button") WebElement confirmAddressBtn;

	@FindBy(id ="cgv") WebElement termsOfServiceCheckbox;
	@FindBy(css ="form#form p button") WebElement confirmShippingBtn;

	@FindBy(css ="div#HOOK_PAYMENT a.bankwire") WebElement payByBankwireBtn;
	@FindBy(css ="div#HOOK_PAYMENT a.cheque") WebElement payByChequeBtn;
	@FindBy(css ="#cart_navigation button") WebElement confirmPaymentBtn;

	@FindBy(css ="div.box") WebElement orderDetailTextbox;
	@FindBy(css ="#center_column p a") WebElement orderHistoryLink;


	OrderPage (WebDriver driver) {
		super(driver);
		PageFactory.initElements(driver, this);
	}

	public void open(){
		driver.get("http://automationpractice.com/index.php?controller=OrderPage");
	}

	public void clickTermsOfService(){
		if (!termsOfServiceCheckbox.isSelected())
			termsOfServiceCheckbox.click();
	}

	public String getOrderNumber(){
	 	String txt = orderDetailTextbox.getText();
       	String[] arr = txt.split(" ");

       	String order_no = "";
       	boolean b = false;
       	for (String s : arr){
       		//System.out.println(s);
       		if (b) {
       			order_no = s;
       			break;
       		}
       		else if (s.equals("reference"))
       			b = true;
       	}

		return order_no;	      	
	}

}
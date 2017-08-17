import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.openqa.selenium.WebDriver;

import io.appium.java_client.remote.MobileCapabilityType;
import io.appium.java_client.remote.MobilePlatform;

import io.appium.java_client.remote.IOSMobileCapabilityType;
import io.appium.java_client.ios.IOSDriver;

import java.net.URL;
import java.net.MalformedURLException;

import org.openqa.selenium.html5.Location;

class mobile1 {

	public static void main(String[] args) throws Exception{

		DesiredCapabilities cap = new DesiredCapabilities();
		cap.setCapability(MobileCapabilityType.PLATFORM_NAME, MobilePlatform.IOS);
		//cap.setCapability(MobileCapabilityType.PLATFORM_VERSION, "9.3");
        //cap.setCapability(MobileCapabilityType.DEVICE_NAME, "iPhone 5s (9.3) [B47D5711-547D-40EE-BC36-7CB7C7BD192C] (Simulator)");
        cap.setCapability(MobileCapabilityType.DEVICE_NAME, "iPhone 5s Simulator"); //works
        //cap.setCapability(MobileCapabilityType.UDID, "F3DD0093-DEF4-4694-AECF-CB7BBB67D566");
        //cap.setCapability(MobileCapabilityType.UDID, "iPhone 5s (9.3) [B47D5711-547D-40EE-BC36-7CB7C7BD192C] (Simulator)");
        //cap.setCapability(MobileCapabilityType.BROWSER_NAME, "Safari");         
        //cap.setCapability(MobileCapabilityType.APP, "");
        cap.setCapability(IOSMobileCapabilityType.BUNDLE_ID, "com.apple.Maps");
		cap.setCapability("locationServicesEnabled", true);
		cap.setCapability("locationServicesAuthorized", true);


        IOSDriver driver; 
        try{
        	//AppiumDriver driver = new AppiumDriver(new URL("http://127.0.0.1:4723/wd/hub"),cap);
        	//WebDriver driver = new RemoteWebDriver(new URL("http://127.0.0.1:4723/wd/hub"), cap);
        	driver = new IOSDriver(new URL("http://127.0.0.1:4723/wd/hub"), cap);
        }
        catch (MalformedURLException e){
        	//e.printStackTrace();
        	throw e;
        }
		Location location = new Location(30.267, -97.7430, 0.0);
		driver.setLocation(location);

		driver.findElementByAccessibilityId("Tracking").click();
		driver.findElementByAccessibilityId("Search for place or address").click();
		driver.findElementByAccessibilityId("Food").click();

	
	}
}
 package com.test.helloworld;
import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.remote.DesiredCapabilities;
import java.io.File;
import java.net.MalformedURLException;
import java.net.URL;
import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.remote.MobileCapabilityType;
import io.appium.java_client.remote.MobilePlatform;
public class AppiumTest {
   AndroidDriver driver;
   @Before
   public void testCaseSetUp() throws MalformedURLException {
       File appDir = new File("src");
       File app = new File(appDir, "app-debug.apk");
       DesiredCapabilities cap = new DesiredCapabilities();
       cap.setCapability(MobileCapabilityType.PLATFORM_NAME, MobilePlatform.ANDROID);
       cap.setCapability(MobileCapabilityType.DEVICE_NAME, "Android device");
       cap.setCapability(MobileCapabilityType.NEW_COMMAND_TIMEOUT, "100");
       cap.setCapability(MobileCapabilityType.APP, app.getAbsolutePath());
       driver = new AndroidDriver(new URL("http://127.0.0.1:4723/wd/hub"), cap);
       cap.setCapability("fullReset", true);
   }
   @Test
   public void testHelloWorld() throws Exception {
       //find text HelloWorld and assert
       WebElement text1 = driver.findElement(By.xpath("//android.widget.TextView[@index='0']"));
       Assert.assertEquals("HelloWorld", text1.getText());
       //Click Menu and asset settings
       driver.findElementByName("More options").click();
       Assert.assertEquals("Settings", driver.findElementById("title").getText());
   }
   @After
   public void testCaseTearDown()
   {
       if (driver != null)
           driver.quit();
   }
}
//package simulator.selenium;


import com.google.common.base.Function;
import com.thoughtworks.selenium.SeleneseTestBase;
import org.apache.commons.lang.RandomStringUtils;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.openqa.selenium.*;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.openqa.selenium.support.ui.FluentWait;
import org.openqa.selenium.support.ui.Wait;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.beans.factory.config.PropertyPlaceholderConfigurer;
import org.springframework.core.io.support.PropertiesLoaderUtils;

import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.Properties;
import java.util.concurrent.TimeUnit;




public class stack_overflow_code extends SeleneseTestBase {
    static WebDriver driver;

    private static Logger log = LoggerFactory.getLogger(BaseSeleniumTest.class);
    private String loginBaseUrl;


    @BeforeClass
    public static void firefoxSetUp() throws MalformedURLException {

          DesiredCapabilities capability = DesiredCapabilities.firefox();

        driver = new FirefoxDriver();  

        driver.manage().timeouts().implicitlyWait(20, TimeUnit.SECONDS);
        driver.manage().timeouts().pageLoadTimeout(30, TimeUnit.SECONDS);
        driver.manage().window().setSize(new Dimension(1920, 1080));
    }
    @Before
    public void homePageRefresh() throws IOException {
        driver.manage().deleteAllCookies();
        driver.get(propertyKeysLoader("login.base.url"));
    }


    @AfterClass
    public static void closeFirefox(){
        driver.quit();

    }

    public WebElement findElementByXpath(String key) throws IOException {

        int i=0;
        while(!isElementPresent(By.xpath(propertyKeysLoader(key))) && i<5){
            driver.manage().timeouts().implicitlyWait(1, TimeUnit.SECONDS);
            i++;
        }
        return fluentWait(By.xpath(propertyKeysLoader(key)));
    }
    public WebElement findElementByCssSelector(String key) throws IOException {

        int i=0;

        while(!isElementPresent(By.cssSelector(propertyKeysLoader(key))) && i<5){
            driver.manage().timeouts().implicitlyWait(1, TimeUnit.SECONDS);
            i++;
        }

    }


    public void locatorFindingHandling(String key) throws IOException /*throws IOException*/ {

        fluentWait(By.cssSelector(propertyKeysLoader(key))).click();

    }
    public void locatorFindingHandling(String key, String key1) throws IOException {

        driver.findElement(By.xpath(propertyKeysLoader(key))).sendKeys(propertyKeysLoader(key1));

    }



    public String propertyKeysLoader(String key) throws IOException {
        Properties props = PropertiesLoaderUtils.loadAllProperties("selenium-config.properties");
        PropertyPlaceholderConfigurer props2 = new PropertyPlaceholderConfigurer();
        props2.setProperties(props);
        return (String)props.get(key)          ;
    }

    public WebElement fluentWait(final By locator){
        Wait<WebDriver> wait = new FluentWait<WebDriver>(driver)
                .withTimeout(30, TimeUnit.SECONDS)
                .pollingEvery(5, TimeUnit.SECONDS)
        .ignoring(org.openqa.selenium.NoSuchElementException.class);
        WebElement foo = wait.until(
                new Function<WebDriver, WebElement>() {
                    public WebElement apply(WebDriver driver) {
                        return driver.findElement(locator);
                    }
                }
        );
        return  foo;              }     ;


   public boolean isElementPresent(By selector)
   {
       return driver.findElements(selector).size()>0;
   }

    public boolean isElementVisible(By selector){
        return driver.findElement(selector).isDisplayed();
    }

    public void jsDirectClickUsingDOM_GEBi(String key) throws IOException {
        JavascriptExecutor js = (JavascriptExecutor) driver;
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append("document.getElementById(\'"+propertyKeysLoader(key) +"\').click();");
        js.executeScript(stringBuilder.toString());

    }

    public void jsCodeExecution(String jsCode){
        JavascriptExecutor js = (JavascriptExecutor)driver;
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append(jsCode);
        js.executeScript(stringBuilder.toString());
    }

    public void jsDirectClickUsingDOM_GEBTagName(String tagName,int argNum) throws IOException {
        JavascriptExecutor js = (JavascriptExecutor) driver;
        StringBuilder stringBuilder = new StringBuilder();
//        stringBuilder.append("document.getElementsByClassName(\'"+propertyKeysLoader(key) +"\')["+argArrNum+"].click();");
//        stringBuilder.append("document.getElementsByTagName(\'"+tagName+"\')[document.getElementsByTagName('div').length-"+argNum+"].click()");
        stringBuilder.append("document.getElementsByTagName(\'"+tagName+"\')[document.getElementsByTagName(\'"+tagName+"\').length-"+argNum+"].click()");
        js.executeScript(stringBuilder.toString());

    }


    public String jsGetColor(String css){

        JavascriptExecutor js = (JavascriptExecutor) driver;
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append("var x=$(\'"+css+"\');");
        stringBuilder.append("return x.css('color')");
        String res= (String) js.executeScript(stringBuilder.toString());
        return res;

    }


    public String randomStringGenerator(){
        return  RandomStringUtils.randomAlphabetic(8);
    }

    public String randomIntSequenceGenerator(){
        return RandomStringUtils.randomNumeric(6);
    }
}
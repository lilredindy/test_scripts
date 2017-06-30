import java.util.*;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.WebDriver; 
import org.openqa.selenium.htmlunit.HtmlUnitDriver; 
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;



class Solution {

    public static void main( String[] args ) {
        //WebDriver driver = new FirefoxDriver();
        WebDriver driver = new HtmlUnitDriver();
        //String uri = System.getProperty("user.dir") + "/index.html";        
        driver.get("file://" + System.getProperty("user.dir") + "/index.html");

        //List<WebElement> list = driver.findElements(By.className("title"));
        //List<WebElement> list = driver.findElements(By.cssSelector("*[class^='title']"));
        
        //WebElement e = driver.findElement(By.cssSelector("span.title:nth-child(1)"));
        WebElement e = driver.findElement(By.xpath("//span[@class='title'])[0]"));
        //WebElement e = driver.findElement(By.cssSelector(".title>span:nth-child(1)"));


        driver.quit();

/*
    driver.get("http://www.google.com/");
    WebElement element = driver.findElement(By.name("q"));

    element.sendKeys("TestingBot");
    element.submit();

    System.out.println(driver.getTitle());
    driver.quit();
*/
    }

    
}
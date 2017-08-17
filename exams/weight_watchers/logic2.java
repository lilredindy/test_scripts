import java.util.*;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.WebDriver; 
import org.openqa.selenium.htmlunit.HtmlUnitDriver; 
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;

class logic2 {

    public static void main( String[] args ) {
        //WebDriver driver = new ChromeDriver();
        WebDriver driver = new HtmlUnitDriver();
        String uri = "file://" + System.getProperty("user.dir") + "/index.html";
        System.out.println(uri);
        driver.get(uri);

        //WebElement e3 = driver.findElement(By.xpath("//span[@class='title ng-binding'][3]")); //works
        WebElement e3 = driver.findElement(By.xpath("//span[@ng-bind='food.name'][3]")); 
        System.out.println(e3.getText());
        //WebElement e5 = driver.findElement(By.xpath("//span[@class='title ng-binding'][5]")); //works
        WebElement e5 = driver.findElement(By.xpath("//span[@ng-bind='food.name'][5]")); 
        System.out.println(e5.getText());

        //List<WebElement> elements = driver.findElements(By.className("title")); //works
        //List<WebElement> elements = driver.findElements(By.cssSelector("*[class^='title']")); //works
        //List<WebElement> elements = driver.findElements(By.cssSelector("div.itemContent > span.title")); //works
        //List<WebElement> elements = driver.findElements(By.xpath("//span[@class='title ng-binding']")); //works
        //List<WebElement> elements = driver.findElements(By.cssSelector("div.itemContent > span")); //works
        //for (WebElement e : elements)
         //   System.out.println(e.getText());


        List<WebElement> foods = driver.findElements(By.cssSelector("div.itemContent > span")); //works

        /*
        Map m = new HashMap();
        for (int i = 0; i < foods.size(); i += 2)
            m.put(foods.get(i).getText(), foods.get(i+1).getText());
        System.out.println(m);
        */

        
        HashMap<String, String> hm = new HashMap<String, String>();
        for (int i = 0; i < foods.size(); i += 2)
            hm.put(foods.get(i).getText(), foods.get(i+1).getText());
        
        System.out.println("Food diary:");
        for (Map.Entry<String, String> entry: hm.entrySet()){
            System.out.println("Food name: " + entry.getKey());
            System.out.println("Serving size: " + entry.getValue());
        }

        driver.quit();

    }

    
}
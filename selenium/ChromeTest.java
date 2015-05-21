 import static org.junit.Assert.assertEquals;
 import org.junit.Test;

 
 import org.junit.After;
 import org.junit.AfterClass;
 import org.junit.Before;
 import org.junit.BeforeClass;
 import org.junit.runner.RunWith;
 import org.junit.runners.BlockJUnit4ClassRunner;
 import org.openqa.selenium.chrome.ChromeDriverService;
 import org.openqa.selenium.remote.service.DriverService;
 import org.openqa.selenium.remote.DesiredCapabilities;
 import org.openqa.selenium.remote.RemoteWebDriver;
 import org.openqa.selenium.WebDriver;

 import java.io.File;

//This is apparently for a WINDOWS SERVICE or the like...
//not really what I am needing
 
 @RunWith(BlockJUnit4ClassRunner.class)
 public class ChromeTest {
 
   private static ChromeDriverService service;
   private WebDriver driver;
 
   @BeforeClass
   public static void createAndStartService() {
     ChromeDriverService.Builder service = new ChromeDriverService.Builder();
         service.usingDriverExecutable(new File("path/to/my/chromedriver.exe"));
         service.usingAnyFreePort();
         service.build();
     service.start();
   }
 
   @AfterClass
   public static void createAndStopService() {
     service.stop();
   }
 
   @Before
   public void createDriver() {
     driver = new RemoteWebDriver(service.getUrl(),
         DesiredCapabilities.chrome());
   }
 
   @After
   public void quitDriver() {
     driver.quit();
   }
 
   @Test
   public void testGoogleSearch() {
     driver.get("http://www.google.com");
     WebElement searchBox = driver.findElement(By.name("q"));
     searchBox.sendKeys("webdriver");
     searchBox.quit();
     assertEquals("webdriver - Google Search", driver.getTitle());
   }
 }
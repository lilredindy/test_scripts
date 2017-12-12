import org.openqa.selenium.*;
import org.openqa.selenium.remote.*;
import java.net.URL;
import java.util.concurrent.TimeUnit;
import org.openqa.selenium.remote.SessionId;


import org.junit.Test;
import org.junit.Assert;
import org.junit.*;

//import com.testingbot.testingbotrest.TestingbotREST;
import java.util.*;


import java.io.BufferedReader;
import java.io.InputStreamReader;


public class TestingBot {

	private WebDriver driver;
	private boolean error = false;
	private boolean success = true;
	private String errorMsg = "";
	private String testName = "";


	@Before
	public void setUp() throws Exception {
		DesiredCapabilities capabilities = DesiredCapabilities.firefox();
		capabilities.setCapability("version", "latest");
		capabilities.setCapability("platform", Platform.WINDOWS);
		capabilities.setCapability("name", "Pilot tests");

		this.driver = new RemoteWebDriver(
		   new URL("http://e9119262abca817b6e89829a3f3b39ed:10b7b3f28b761a8190a08d262506b227@hub.testingbot.com/wd/hub"),
		   capabilities);
		driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
	}


	@Test
	public void getESPN() throws Exception {
		try {
			testName = Thread.currentThread().getStackTrace()[1].getMethodName();
			driver.get("http://www.espn.com");
			Assert.assertEquals("ESPN: The Worldwide Leader in Sports", this.driver.getTitle());	
		}
		catch ( | AssertionError e ){
			error = true;
			errorMsg = e.toString();
			throw e;
		}
	}


	@Test
	public void getGoogle() throws Exception {
		try {
			testName = Thread.currentThread().getStackTrace()[1].getMethodName();
			driver.get("http://www.google.com");
			Assert.assertEquals("Gooooogle", this.driver.getTitle());
		}
		catch (Exception | AssertionError e ){
			error = true;
			success = false;
			errorMsg = e.toString();
			throw e;
		}
		
	}


	@After
	public void tearDown() throws Exception {
		System.out.println("Session ID:" + ((RemoteWebDriver)this.driver).getSessionId());
		System.out.println("Error: " + error);
		
		/*
		TestingbotREST r = new TestingbotREST("e9119262abca817b6e89829a3f3b39ed", "10b7b3f28b761a8190a08d262506b227");
		Map<String,Object> data = new HashMap<String,Object>();
		data.put("test[success]", error);
		//data.put("name", "My Test");
		r.updateTest(((RemoteWebDriver)driver).getSessionId().toString(), data);
		*/

		//executeBashCommand("curl \"https://api.testingbot.com/v1/user\" -u e9119262abca817b6e89829a3f3b39ed:10b7b3f28b761a8190a08d262506b227");
		String cmd = String.format("curl \"https://api.testingbot.com/v1/tests/%s\" -X PUT -d \"test[name]=%s\" -d \"test[success]=%s\" -d \"test[status_message]=%s\" -u e9119262abca817b6e89829a3f3b39ed:10b7b3f28b761a8190a08d262506b227", ((RemoteWebDriver)driver).getSessionId(), testName, success, errorMsg);
		this.executeBashCommand(cmd); //using this with class method
		driver.quit();
	}

		/**
	 * Execute a bash command. We can handle complex bash commands including
	 * multiple executions (; | && ||), quotes, expansions ($), escapes (\), e.g.:
	 *     "cd /abc/def; mv ghi 'older ghi '$(whoami)"
	 * @param command
	 * @return true if bash got started, but your command may have failed.
	 */
	public static boolean executeBashCommand(String command) {
	    boolean success = false;
	    System.out.println("Executing BASH command:\n   " + command);
	    Runtime r = Runtime.getRuntime();
	    // Use bash -c so we can handle things like multi commands separated by ; and
	    // things like quotes, $, |, and \. My tests show that command comes as
	    // one argument to bash, so we do not need to quote it to make it one thing.
	    // Also, exec may object if it does not have an executable file as the first thing,
	    // so having bash here makes it happy provided bash is installed and in path.
	    String[] commands = {"bash", "-c", command};
	    try {
	        Process p = r.exec(commands);

	        p.waitFor();
	        BufferedReader b = new BufferedReader(new InputStreamReader(p.getInputStream()));
	        String line = "";

	        while ((line = b.readLine()) != null) {
	            System.out.println(line);
	        }

	        b.close();
	        success = true;
	    } catch (Exception e) {
	        System.err.println("Failed to execute bash with command: " + command);
	        e.printStackTrace();
	    }
	    return success;
	}

}
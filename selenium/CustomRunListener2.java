//import org.openqa.selenium.*;
import org.openqa.selenium.remote.SessionId;
import org.openqa.selenium.remote.RemoteWebDriver;


import org.junit.runner.Description;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;
import org.junit.runner.notification.RunListener;

public class CustomRunListener extends RunListener {


	private SessionId id;

	public void CustomRunListener(RemoteWebDriver driver){
		id = driver.getSessionId();
	}

	public void testFailure(Failure failure){
		System.out.println("Failed: " + failure.getDescription().getMethodName());
	}
}
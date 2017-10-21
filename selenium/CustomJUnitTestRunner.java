import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;
import org.junit.runner.notification.RunListener;


public class CustomJUnitTestRunner {


	  public static void main(String[] args) throws Exception {
	  	
	  	//Result result = JUnitCore.runClasses(TestingBot1.class);

	  	JUnitCore core = new JUnitCore();
	  	//core.addListener(new TestingBot1());
	  	Result result = core.run(TestingBot1.class);


	  	System.out.println("The number of tests: " + result.getRunCount());
	  	System.out.println("The test was success: " + result.wasSuccessful());

	  	
	  	if (!result.wasSuccessful()){

		  	for (Failure f : result.getFailures()){
		  		//System.out.println(f.getTestHeader());
		  		//System.out.println(f.getDescription());
		  		//System.out.println(f.getMessage());
		  		System.out.println(f.getException());
		  	}	
	  	}
	  }

}

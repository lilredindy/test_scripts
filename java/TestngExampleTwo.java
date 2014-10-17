
import org.testng.annotations.*;
import org.testng.Assert;


public class TestngExampleTwo {
	
	@Test
	public void testAssert(){
 
	String test = "test";
	Assert.assertEquals(test, "test");
	}

}
package foo;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import org.junit.runner.JUnitCore;


public class TestJunit {


   String message = "Hello World";	

   @Test
   public void testPrintMessage() {
      assertEquals(message,"Hello Worlds");
   }
}
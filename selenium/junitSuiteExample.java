import org.junit.runner.RunWith;
import org.junit.runners.Suite;
import org.junit.runners.Suite.SuiteClasses;


@RunWith(Suite.class)
@SuiteClasses({
    googleTest.class,
    gmailTest.class
})

public class jUnitSuiteExample
{
 /* empty class */
}


/*
//Junit 3 style

import junit.framework.Test;
import junit.framework.TestSuite;
import junit.textui.TestRunner;
 
public class TestSuiteExample{
    public static Test suite() {  
        TestSuite suite = new TestSuite(googleTest.class);
        suite.addTestSuite(gmailTest.class);
        return suite;  
    } 
    public static void main(String[] args) {
        TestRunner.run(suite());
    }
}

*/
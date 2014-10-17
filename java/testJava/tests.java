import junit.framework.TestCase;
import org.junit.*;
import static org.junit.Assert.*;
 
public class tests extends TestCase
{
 
 //public tests(String s)
 //{
  //super(s);
  //System.out.println("constructor");

 //}


  @BeforeClass
  public void testBeforeClass(){

  	System.out.println("Before Class");
  }

  @AfterClass
  public void testAfterClass(){

  	System.out.println("After Class");
  }

 
 @Test
 public void testA()
 {
  assertTrue(true);
 }

 @Test
 public void testB()
 {
  assertTrue(false);
 }
 
 @Test
 public void testC()
 {
 	Foo foo1 = new Foo();
 	assertEquals(true, foo1.isBroken());
 }

@Test
 public void testBike()
 {
 	Bicycle bike1 = new Bicycle();
 	
 }

@Before
 public void setUpFunc()
 {
 	System.out.println("before");
 }
 
 @After
 public void tearDown()
 {
 	System.out.println("after");
 }
 
}

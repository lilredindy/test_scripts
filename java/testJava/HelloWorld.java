
public class HelloWorld {

  public static void main(String args[]) {
    System.out.println("Hello, World!");
    Bicycle myBike = new Bicycle();
    myBike.printStates();
    Foo myfoo = new Foo();
    if (myfoo.isBroken())
    	System.out.println("yes, it is broken");
  }
}

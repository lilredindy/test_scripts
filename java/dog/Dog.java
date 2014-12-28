
public class Dog {



	public static void woof(){

		System.out.println("woof");
	}
   
   	private static void woof2 (){

		System.out.println("woof");

	}

   	private int count;

	

  	public static void main(String args[]) {
    System.out.println("Main inside dog");



    woof();
    woof2();

    //woof3();

	}
}

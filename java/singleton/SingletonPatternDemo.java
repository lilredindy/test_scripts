public class SingletonPatternDemo {
   public static void main(String[] args) {

      //illegal construct
      //Compile Time Error: The constructor SingleObject() is not visible
      //SingleObject object = new SingleObject();

      //Get the only object available
      SingleObject object = SingleObject.getInstance();
	SingleObject object2 = SingleObject.getInstance();

      //show the message
      object.showMessage();
	object2.showMessage();
	System.out.println(object.equals(object2));

	NonSingleton non1 = new NonSingleton();
	NonSingleton non2 = new NonSingleton();
	System.out.println(non1.equals(non2));	

   }
}

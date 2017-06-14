
public class pass_by_value {


    public static void main( String[] args ) {
        Dog aDog = new Dog("Max");
        // we pass the object to foo
        foo(aDog);
        // aDog variable is still pointing to the "Max" dog when foo(...) returns
        if (aDog.getName().equals("Max")) { System.out.println("Max is my dog!"); } // true, java passes by value
        if (aDog.getName().equals("Fifi")) { System.out.println("Fifi is my dog!"); } // false 
    }

    public static void foo(Dog d) {
        d.getName().equals("Max"); // true
        // change d inside of foo() to point to a new Dog instance "Fifi"
        d = new Dog("Fifi");
        if (d.getName().equals("Fifi")) { System.out.println("Local to foo() Fifi is my dog!"); } // true
    }
}



class Dog {

    private String name = "Bar";
        
    public Dog(String name){
        System.out.println(this.name);
        this.name = name;
    }

    String getName(){
        return name;
    }   
}





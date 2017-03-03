


import java.util.*;



class TestFood{
	
		/*
		OUTPUT:
		My name is: FastFood
		My name is: Fruit
		Our superclass is: Food
		I'm serving FastFood
		I'm serving Fruit
		*/

	public static void main(String [] arg){


		FoodFactory myFoods = new FoodFactory();
		//System.out.println(myFoods.getClass().getName());
		Food f1 = myFoods.getFood("FastFood");
		Food f2 = myFoods.getFood("Fruit");

		System.out.println("My name is: " + f1.getClass().getName());
		System.out.println("My name is: " + f2.getClass().getName());

		System.out.println("Our superclass is: " + f1.getClass().getSuperclass().getName());
		f1.serveFood();
		f2.serveFood();
	}



	public static class Food {

		protected String name;


		public void serveFood(){
			System.out.println("Im serving: " + name);
		}
	}

	public static class FastFood extends Food{}
	public static class Fruit extends Food{}

	public static class FoodFactory extends Food {

		public Food getFood(String s){
			if (s == "FastFood"){
				Food f = new FastFood();
				f.name = s;
				return f;
			}
			
			if (s == "Fruit"){
				Food f = new Fruit();
				f.name = s;
				return f;
			}

			return this;
		
		}

	}

}
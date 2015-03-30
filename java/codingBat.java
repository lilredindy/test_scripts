

public class codingBat {



public static void main(String [ ] args)

{
    //int[] x = {2, 1, 1, 2, 1};
    //System.out.println(canBalance(x));

    int[] nums = {5};
    System.out.println(splitOdd10(nums));
}


public static boolean splitOdd10(int[] nums) {

  if (nums.length == 0)
    return false;
  if (nums.length == 1 && ((nums[0] % 2) != 0))
    return true;

  
  int[] grp1 = new int[nums.length];
  int[] grp2 = new int[nums.length];

  
  System.out.println("grp1: " + java.util.Arrays.toString(grp1));
  System.out.println("grp2: " + java.util.Arrays.toString(grp2));
  System.out.println("======================================"); 
  

  int small_counter = 0;
  int big_counter = 0;
 
  
  while (big_counter != nums.length){
    
    while (small_counter != nums.length){
      
      for (int i = 0; i < nums.length; ++ i) {

        if (i >= big_counter && i <= small_counter)
          grp1[i] = nums[i];
        else 
          grp2[i] = nums[i]; 
      
      }
        
      
      System.out.println("big counter is at: " + big_counter);      
      System.out.println("small counter is at: " + small_counter);
      System.out.println("grp1: " + java.util.Arrays.toString(grp1));
      System.out.println("grp2: " + java.util.Arrays.toString(grp2));
      System.out.println("======================================"); 
      

      if (checkGroups(grp1, grp2))
        return true;
      
      ++small_counter;

      java.util.Arrays.fill(grp1, 0);
      java.util.Arrays.fill(grp2, 0);
    }
    
    
    ++big_counter;
    small_counter = big_counter;
  } 
   
  return false;
}


public static boolean checkGroups(int[] group1, int[] group2){
  int sum_grp1 = 0;
  int sum_grp2 = 0;

  for (int i = 0; i < group1.length; ++ i)
    sum_grp1 += group1[i];
    
  for (int j = 0; j < group2.length; ++j)  
    sum_grp2 += group2[j];
  
  if ((sum_grp1 % 10 == 0) && (sum_grp2 % 2 != 0))
    return true;
  else
    return false; 
}







public static int maxSpan(int[] nums) {
	int span =0;
	if (nums.length == 0) return 0;
	if (nums.length == 1) return 1;
 
  	for (int i = 0; i < nums.length; ++ i) 
  		for ( int j = 1 ; j < nums.length; ++ j)
  			if (nums[i] == nums[j]) {
  				if ((j - i + 1) > span) 
  					span = j - i + 1;
  			}

  	return span;
}

public boolean linearIn(int[] outer, int[] inner) {
  boolean match = false;
  int count = 0;
  for (int i = 0; i < inner.length; ++ i)
    for (int j =0; j < outer.length; ++ j)
      if (outer[j] == inner[i]) {
        ++ count;
        break; }      
     
  if (count == inner.length) match = true;
  return match;    
}

public static boolean canBalance(int[] nums) {
  // {2, 1, 1}
  //forwards 2,3,4 
  //backwards 1,2,4 
  //{2,5,1,1,1,1,1,2}
  //forwards 2,7,8,9,10,11,12,14
  //backwards 2,3,4,5,6,7,12,14 

  int len = nums.length;
  
  if (len == 1) return false; 
  if (len == 2 && (nums[0] == nums[1])) return true;
  
  int [] forwards = new int [len];
  int [] backwards = new int [len];
  
  for (int i = 0; i < len; ++ i) {
    if (i == 0){
      forwards[i] = nums[i];
      backwards[i] = nums[len - 1];
    }
    else {
      forwards[i] = nums[i] + forwards[i - 1]; 
      backwards[i] = nums[(len - 1) - i] + backwards[i - 1]; 
    } 
  }

  for (int j = 0; j < len; ++ j)
    for (int k = 0; k < len; ++ k)  
      if ((forwards[j] == backwards[k]) && (j + k + 2 == len))
        return true;
  

  return false;
}



}

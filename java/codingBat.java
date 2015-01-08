

public class codingBat {



public static void main(String [ ] args)

{
    int[] x = {2, 1, 1, 2, 1};
    System.out.println(canBalance(x));
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

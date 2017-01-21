import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Thief {


    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
       //Scanner in = new Scanner(System.in);
       Scanner in = new Scanner(System.in);
		
		
        int N = in.nextInt();
        int X = in.nextInt();
        //System.out.println(N + " " + X);
        int[] v = new int[N];
        int[] a = new int[N];
        for (int i = 0; i < N; ++i){
            v[i] = in.nextInt();
            a[i] = in.nextInt();
            //System.out.println(v[i] + " " + a[i]);
        }
        
        List<Integer> totals = new ArrayList<Integer>();
        List<Integer> subtotal_indices = new ArrayList<Integer>();


		int j_counter =0;

        for (int j = 0; j < N; ++j){
            subtotal_indices.clear();
			int A = a[j];  //add first amt to sum
            subtotal_indices.add(j);

			if (X == A){
                totals.add(v[j]);  	
                continue; //already done!  back to top of j loop
            }
            
            if (A > X)
                continue;
            
            for (int k = j + 1; k < N; ++k){   
				
			    A += a[k]; //amt is tallied     
                subtotal_indices.add(k);

                if (A >= X) { 
					if (A == X){
						
						
						for(Integer s: subtotal_indices)
                        	System.out.print(s + " ");
                    	System.out.println();
						
 						
                    	int total = 0;
                    	for (Integer s : subtotal_indices)
                        	total += v[s]; //the price at stored index
                    	totals.add(total);
					}
					
					A -= a[k]; 
                    subtotal_indices.remove(subtotal_indices.size() - 1);
  					
					if (N - k == 1){ //edge case
                    	if (subtotal_indices.size() == 1)
                        	continue; //the k is complete and returns to j
                    	A -= a[subtotal_indices.get(subtotal_indices.size() -1)];
						k = subtotal_indices.get(subtotal_indices.size() - 1); //reset k
                    	subtotal_indices.remove(subtotal_indices.size() - 1); 
                	}
                }   
				else { // A < X
                    
					if (N - k == 1){ //edge case
					    A -= a[k]; 
                    	subtotal_indices.remove(subtotal_indices.size() - 1);
                    	if (subtotal_indices.size() == 1)
                        	continue;
                        A -= a[subtotal_indices.get(subtotal_indices.size() -1)];
						k = subtotal_indices.get(subtotal_indices.size() - 1); //reset k
                    	subtotal_indices.remove(subtotal_indices.size() - 1); 
                	}
				}

				
            } //k loop
			++j_counter;
			System.out.println("Number of j loops done: " +  j_counter);
        } //j loop
        
      	System.out.println("hello");
   
		int W = 0;
        for (Integer t : totals){
			//System.out.print(t + " ");
         	if (t > W)
				W = t;    
         }

         if (W == 0)
             System.out.print("Got caught!");
         else
            System.out.print(W + " ");   
        
    }
}


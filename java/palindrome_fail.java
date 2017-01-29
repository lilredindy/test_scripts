import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class palindrome {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */

        Scanner sc = new Scanner(System.in);


        int N = sc.nextInt();
        String S = new String("");
        S = sc.next();

        //System.out.println(N);        	
        //System.out.println(S);  


        for (int i = 0; i < N; ++i){
        	int max = do_palin(S);
        	//System.out.println(S);	
        	System.out.println(max);	
        	String S2 = S.substring(1);
        	S2 = S2.concat(String.valueOf(S.charAt(0)));
        	S = S2;

        	
        }
    }

    public static int do_palin(String s){

    	//System.out.println(s);
    	int N = s.length();

    	List<Integer> maxs = new ArrayList<Integer>();

    	for (int i = 1; i < (N-1); ++i){
    		System.out.println("i: " + i);
    		int left = i-1;
    		int right = i+1;
    		int max = 1;
    		//System.out.println("left: " + left + ",right: " + right);
    		while((left >= 0) && (right < N)){
				if (s.charAt(left) == s.charAt(right) ){
    				max += 2;
    				--left;
    				++right;
    			}
    			else 
    				break;
    		}
    		
    		if ((max == 1) && ((s.charAt(left) == s.charAt(i)) || (s.charAt(right) == s.charAt(i)))) 
    			++max;
    	


    		maxs.add(max);
    		System.out.println(Arrays.toString(maxs.toArray()));

    	}
    	int best_max = Collections.max(maxs);
    	return best_max;
    }
}
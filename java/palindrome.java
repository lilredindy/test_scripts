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

    	int N = s.length();

    	List<Integer> maxs = new ArrayList<Integer>();

    	String p = new String("");
        for (int i = 0; i <= N; ++i){
            for (int j = i+1; j <= N; ++j){
                p = s.substring(i,j);
                //System.out.println(p);
                if (isPalindrome(p)){
                    maxs.add(p.length());
                }
                    
            }
        }
        System.out.println(Arrays.toString(maxs.toArray()));
        int best_max = Collections.max(maxs);
        return best_max;
    }


    private static Boolean isPalindrome(String p){
        Boolean result = true;
        for (int i = 0; i < p.length(); ++i){
            if (p.charAt(i) != p.charAt(p.length()-1-i)){
                result = false;
                break;
            }
                
        }
        return result;
    }
}
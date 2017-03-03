import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class crush {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();
        int M = sc.nextInt();
        
        List<Long> ab = new ArrayList<Long>();

        for (int i = 0; i < N; ++i)
            ab.add((Long)(long)0);
        
        while (M-- > 0){
            int a = sc.nextInt();
            int b = sc.nextInt();
            int k = sc.nextInt();
        
            for (int i = a; i <= b; ++i){
                long sum = ab.get(i - 1) + k;
                ab.set(i-1, sum);  
                //System.out.println(ab);
            }
         }
        
        long max = Collections.max(ab);
        System.out.println(max);
      
    }
}
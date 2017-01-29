import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class flip {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */

        Scanner sc = new Scanner(System.in);

        int q = sc.nextInt();

        while (q-- > 0){

        	int n = sc.nextInt();

        	int[][] M = new int[2*n][2*n];

        	for (int i = 0; i < (2*n); ++i){ //row
        		for (int j = 0; j < (2*n); ++j){ //col
        			M[i][j] = sc.nextInt();
        		}
        	}

        	System.out.println(Arrays.deepToString(M));

        	//int[] find_max = new int[4];
        	List<Integer> find_max = new ArrayList<Integer>();
        	//int[] sum_max = new int[n*n];
        	List<Integer> sum_max = new ArrayList<Integer>();

        	for (int i = 0; i < n; ++i){ //row
        		for (int j = 0; j < n; ++j){ //col

        			find_max.add(M[i][j]);
        			find_max.add(M[i][(2*n - 1) - j]);
        			find_max.add(M[(2*n - 1) -i][j]);
        			find_max.add(M[(2*n - 1) -i][(2*n - 1) - j]);
        			//int max = (int) Collections.max(Arrays.asList(find_max));
        			//System.out.println(Arrays.toString(find_max.toArray()));
        			Integer max  = Collections.max(find_max);
        			sum_max.add(max);
        			find_max.clear();
        		}
        	}

        	int sum = 0;
        	for(Integer s : sum_max)
        		sum += (int)s;

        	System.out.println(sum);


        }
    } //main


}
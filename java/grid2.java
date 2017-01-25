
//import java.io.*;
import java.util.*;
//import java.text.*;
//import java.math.*;
//import java.util.regex.*;
//import java.util.Collections;


class grid2 {


	public static void main(String []argh){

		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt(); //num of rows
		int m = sc.nextInt(); //num of cols
		int k = sc.nextInt(); //num of tracks


		int[][] aa = new int[n][m];


		for (int i = 0; i < k; ++i){
			
			int r = sc.nextInt();
			int c1 = sc.nextInt();
			int c2 = sc.nextInt();

			aa = layTracks(aa,m,r,c1,c2);

		}

		//System.out.println(Arrays.deepToString(aa));
		
		int counter = 0;
		for (int i = 0; i < n; ++i){
			for (int j = 0; j < m; ++j){
				if (aa[i][j] == 0)
					++counter;
			}
		}

		System.out.println(counter);
			
	} //main
			




	public static int[][] layTracks(int[][] matrix, int m, int row_no, int start, int end){

		//int[][] M = new int[n][m];
		for (int i = 0; i < m; ++i)
			if (i >= (start -1) && i <= (end -1))
				matrix[row_no - 1][i] = 1;

		return matrix;
	} 
}

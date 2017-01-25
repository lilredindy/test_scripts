
//import java.io.*;
import java.util.*;
//import java.text.*;
//import java.math.*;
//import java.util.regex.*;
//import java.util.Collections;


class grid {


	public static void main(String []argh){

		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt(); //num of rows
		int m = sc.nextInt(); //num of cols
		int k = sc.nextInt(); //num of tracks


		int[] freeForRow = new int[n];

		for (int x = 0; x < n; ++x)
			freeForRow[x] = m; //init with all free


		for (int i = 1; i <= k; ++i){
			int r = sc.nextInt();
			int c1 = sc.nextInt();
			int c2 = sc.nextInt();


			int y = calcFree(m, c1, c2);

			freeForRow[r-1] = y;
		}

			int sum =0;
			for (int j = 0; j < freeForRow.length; ++ j){
				System.out.println("Index " + (j+1)+ ": " + freeForRow[j] );
				sum += freeForRow[j];

			}
			

			System.out.println(sum);

	} //main

	public static int calcFree(int m, int start, int end){

		int counter = 0;
		for (int i = 1; i <=m; ++i){
			if (i < start || i > end)
				++counter;
		}

		return counter;
	} //calcFree
}

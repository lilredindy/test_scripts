
//import java.io.*;
import java.util.*;
//import java.text.*;
//import java.math.*;
//import java.util.regex.*;
//import java.util.Collections;


class grid3 {


	public static void main(String []argh){

		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt(); //num of rows
		int m = sc.nextInt(); //num of cols
		int k = sc.nextInt(); //num of tracks


		//int[][] aa = new int[n][m]; //heap extended
		//int[] M = new int[m]; //heap extended
		HashMap<Integer, Integer[]> h = new HashMap<Integer, Integer[]>();

		for (int i = 0; i < k; ++i){
			
			int r = sc.nextInt();
			int c1 = sc.nextInt();
			int c2 = sc.nextInt();

			h = updateMap(h, r, c1, c2);
		}

		for (Map.Entry<Integer, Integer[]> entry : h.entrySet()) {
			System.out.println("key: " + entry.getKey());
			Integer[] v = entry.getValue();
			System.out.println("start: " + v[0] + ", end: " + v[1]);
		}
			
	} //main
			


	public static HashMap<Integer, Integer[]> updateMap(HashMap<Integer,Integer[]> h, int key, int start, int end){

		Integer[] value = {start, end};
		Integer[] v = new Integer[2];


		if (!h.containsKey(key))
			h.put(key, value);
		else {
			v = (Integer[])h.get(key);  //returns Object
			if (v[0] > value[0])
				value[0] = v[0];
			if (v[1] > value[1])
				value[1] = v[1];
			h.put(key,value);
		}

		return h;
	}

	public static int[][] layTracks(int[][] matrix, int m, int row_no, int start, int end){

		//int[][] M = new int[n][m];
		for (int i = 0; i < m; ++i)
			if (i >= (start -1) && i <= (end -1))
				matrix[row_no - 1][i] = 1;

		return matrix;
	} 
}

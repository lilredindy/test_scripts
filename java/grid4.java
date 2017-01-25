
//import java.io.*;
import java.util.*;
//import java.text.*;
//import java.math.*;
//import java.util.regex.*;
//import java.util.Collections;


class grid4 {


	public static void main(String []argh){

		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt(); //num of rows
		int m = sc.nextInt(); //num of cols
		int k = sc.nextInt(); //num of tracks


		//int[][] aa = new int[n][m]; //heap extended
		//int[] M = new int[m]; //heap extended
		//HashMap<Integer, Integer[]> h = new HashMap<Integer, Integer[]>();
		HashMap<Integer, HashSet<Integer>> h = new HashMap<Integer, HashSet<Integer>>();

		for (int i = 0; i < k; ++i){ //runtime is O(k)
			
			int r = sc.nextInt();
			int c1 = sc.nextInt();
			int c2 = sc.nextInt();

			h = updateMap(h, r, c1, c2);
		}

		int track_nodes = 0;
		for (Map.Entry<Integer, HashSet<Integer>> entry : h.entrySet()) { //runtime of k
			//System.out.println("key: " + entry.getKey());
			HashSet<Integer> v = entry.getValue();
			//System.out.println(v);
			track_nodes += v.size();
		}

		int grid_size = m * n;
		int free_space = grid_size - track_nodes; 
		System.out.println(free_space);	
	} //main
			


	public static HashMap<Integer, HashSet<Integer>> updateMap(HashMap<Integer,HashSet<Integer>> h, int key, int start, int end){

		HashSet<Integer> s = new HashSet<Integer>();

		if (h.containsKey(key))
			s = h.get(key);
		
		for (int i = start; i <= end; ++i) //runtime is O(m)
			if (!s.contains(i)) //Integer class wraps int
				s.add(i); //add to set
		
		h.put(key, s); //re-write key-value if key exists
		return h;
	}
}

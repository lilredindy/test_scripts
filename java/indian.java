//import java.io.*;
import java.util.*;
//import java.text.*;
//import java.math.*;
//import java.util.regex.*;
//import java.util.Collections;


class indian {


	public static void main(String []argh){

		Scanner sc = new Scanner(System.in);

		int T = sc.nextInt();

		for (int t = 0; t < T; ++t){

			int N = sc.nextInt();
			int G = sc.nextInt();

			/*
			//still has the 0s 
			Integer[] A = new Integer[N];
			for (int n = 0; n < N; ++n)
				A[n] = sc.nextInt();
			Arrays.sort(A,  Collections.reverseOrder());
			System.out.println(Arrays.toString(A));
			*/



			List<Integer> L = new ArrayList<Integer>();
			int next = 0;
			for (int n = 0; n < N; ++n){
				next = sc.nextInt();
				if (next != 0) //remove any 0 from the list
					L.add(next);	
			}
				
			//System.out.println("L: " + Arrays.toString(L.toArray()));
			Integer[] A = L.toArray(new Integer[0]); //this is weird, but works
			Arrays.sort(A,  Collections.reverseOrder()); //misleading...not reverse, descending
			//System.out.println(Arrays.toString(A));


			
			if (isSyncable(G,A))
				System.out.println("YES");
			else 
				System.out.println("NO");

		}
	}

	public static Boolean isSyncable(int duration, Integer[] thieves){
		
		//duration = 4
				  //0,1,2,3
		//thieves = 4,2,2,1


		int slot1 = -1;
		int timer1 = -1;
		int slot2 = -1;
		int timer2 = -1;
		int thief_index = 0;

		for (int d = duration; d > 0; --d){


			if (timer1 <= 0 && (thief_index != thieves.length)){
				slot1 = thief_index;
				timer1 = thieves[slot1];
				++thief_index;
			}
			
			if (timer2 <= 0 && (thief_index != thieves.length)){
				slot2 = thief_index;
				timer2 = thieves[slot2];
				++thief_index;
			}

			--timer1;
			--timer2;
	
			//System.out.println("Countdown: " + d);
			//System.out.println("Thief: " + thief_index);
			//System.out.println("slot1: " + slot1 + ", timer1: " + timer1);
			//System.out.println("slot2: " + slot2 + ", timer2: " + timer2);

			if ((thief_index == thieves.length)  && timer1 <= 0 && timer2 <= 0)
				return true;

		} //duration
		
		return false;
		
	} //asSync

}

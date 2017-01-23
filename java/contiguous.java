import java.util.*;


class contiguous {


	public static void main(String []argh){

		Scanner sc = new Scanner(System.in);

		int T = sc.nextInt();

		for (int t = 0; t < T; ++t){

			int N = sc.nextInt();

			int[] arr = new int[N];
			for (int n = 0; n < N; ++n)
				arr[n] = sc.nextInt();

			System.out.println();
			System.out.println(contig(arr) + " " + noncontig(arr));

		}
	}

	public static int contig(int[] r){


		List<Integer> sums = new ArrayList<Integer>();
		int max = -10000;
		for (int i = 0; i < r.length; ++i){
			
			int sum = r[i];
			int best_sum = sum;

			if (r[i] > max)
				max = r[i];


			//System.out.println(i + ": " + best_sum);

			for (int j = i+1; j < r.length; ++j){

				sum += r[j];

				if (sum > best_sum)
					best_sum = sum;
				

				//System.out.println(j + ": " + best_sum);

			}

			sums.add(best_sum);

		}

        //System.out.println("sums: " + Arrays.toString(sums.toArray()));

		Integer s = Collections.max(sums);
		
		if (max > s)
			return max;
		else 
			return s;
	}



	public static int noncontig(int[] r){

		int sum = 0;
		int max = -10000;
		for (int i = 0;i < r.length ; ++i ) {
			
			if (r[i] > max)
				max = r[i];

			if (r[i] > 0)
				sum += r[i];

		}
			
		if (sum == 0){ 
			sum = max;
		}


		return sum;
	}
}

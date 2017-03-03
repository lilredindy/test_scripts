import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class prison {

/*
 * Complete the function below.
 */

 static long prison(int n, int m, int[] h, int[] v) {

        List<Integer> hList = new ArrayList<Integer>();
        List<Integer> vList = new ArrayList<Integer>();

        for (int i = 0; i <= (n+1); ++i)
        	hList.add(i);

        for (int j = 0; j <= (m+1); ++j)
        	vList.add(j);

		//System.out.println("hList: " + Arrays.toString(hList.toArray()));
		//System.out.println("vList: " + Arrays.toString(vList.toArray()));

        //System.out.println("h[]: " + Arrays.toString(h));

        for (int i = 0; i < h.length; ++i)
        	if (hList.contains(h[i]))
        		hList.remove((Integer)h[i]); 

        //System.out.println("v[]: " + Arrays.toString(v));

        for (int j = 0; j < v.length; ++j)
        	if (vList.contains(v[j]))
        		vList.remove((Integer)v[j]);



		//System.out.println("hList: " + Arrays.toString(hList.toArray()));
		//System.out.println("vList: " + Arrays.toString(vList.toArray()));

        
        long h_max = 0;
        long v_max = 0;
        
        for (int i = 0; i < (hList.size() -1); ++i){
            long diff = hList.get(i+1) - hList.get(i);
            if (diff > h_max)
                h_max = diff;
        }
        
        for (int j = 0; j < (vList.size() -1); ++j){
            long diff = vList.get(j+1) - vList.get(j);
            if (diff > v_max)
                v_max = diff;
        }
        
		return h_max * v_max;
    
    
    }


  	public static void main(String[] args) throws IOException{
        Scanner in = new Scanner(System.in);
        final String fileName = System.getenv("OUTPUT_PATH");
        BufferedWriter bw = new BufferedWriter(new FileWriter(fileName));
        long res;
        int _n;
        _n = Integer.parseInt(in.nextLine().trim());
        
        int _m;
        _m = Integer.parseInt(in.nextLine().trim());
        
        
        int _h_size = 0;
        _h_size = Integer.parseInt(in.nextLine().trim());
        int[] _h = new int[_h_size];
        int _h_item;
        for(int _h_i = 0; _h_i < _h_size; _h_i++) {
            _h_item = Integer.parseInt(in.nextLine().trim());
            _h[_h_i] = _h_item;
        }
        
        
        int _v_size = 0;
        _v_size = Integer.parseInt(in.nextLine().trim());
        int[] _v = new int[_v_size];
        int _v_item;
        for(int _v_i = 0; _v_i < _v_size; _v_i++) {
            _v_item = Integer.parseInt(in.nextLine().trim());
            _v[_v_i] = _v_item;
        }
        
        res = prison(_n, _m, _h, _v);
        bw.write(String.valueOf(res));
        bw.newLine();
        
        bw.close();
    }
}
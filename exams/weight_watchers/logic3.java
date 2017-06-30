import java.io.*;
import java.util.*;

public class logic3 {

   public static void main(String args[]) {

      try{
         System.out.print("Enter full path to file or enter for default: ");
         Scanner sc = new Scanner(System.in);
         String filePath = sc.nextLine(); 

         if (filePath.isEmpty())
            filePath = System.getProperty("user.dir") + "/dictionary.txt"; //get full path

         if (!doesFileExist(filePath))
            throw new Exception("File does not exist at specified path!"); 

         BufferedReader bufferedReader = new BufferedReader(new FileReader(filePath));

         String line = "";
         List<String> wordLines = new ArrayList<String>();
         HashMap<String, List<String>> hm = new HashMap<String, List<String>>(); //create map

         while ((line = bufferedReader.readLine()) != null) {
            //System.out.println(line);
            if (!line.contains("-"))       
               throw new Exception("invalid line, check file for errors...");
            wordLines.add(line);
         }

         for (String wordLine: wordLines){
            String[] parts = wordLine.split("\\s*-\\s*");
            //System.out.println(Arrays.toString(parts));  
            hm.put(parts[0], Arrays.asList(parts[1].split("\\s*,\\s*", -1)));
         }

         for (Map.Entry<String, List<String>> entry: hm.entrySet()){
            System.out.println("Word: " + entry.getKey());
            List<String> meanings = entry.getValue();
            for (String meaning: meanings)
               System.out.println("Meaning: " + meaning);
        }

        bufferedReader.close();

      }
      catch (Exception e){
         e.printStackTrace();
      }
      
         

  


   }

   private static boolean doesFileExist(String path){
      boolean result = true;
      File f = new File(path);
      if (!f.isFile())
         result = false;
      return result;
   }
}
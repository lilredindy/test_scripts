import java.awt.Point;
import java.util.Random;
import java.io.*;
import java.util.*;

public class Cluster{

	public LinkedList <Person> persons;
	public Point center;
	//public int center_weight;
	//public int center_height;

	public Cluster(){
		center = new Point();
		Random r = new Random();

		center.x =  r.nextInt(101) + 50;
		//System.out.println(center.x);
		center.y =  r.nextInt(53) + 38;
		//System.out.println(center.y);

		persons = new LinkedList <Person>();
	}

	public int getWeight(){
		return (int)center.getX();
	}

	public int getHeight(){
		return (int)center.getY();
	}

	public double averageWeight(){
		double total = 0.0;
		int count = 0;
		ListIterator <Person> p_iter = persons.listIterator(0);
		while (p_iter.hasNext()){
			Person p = p_iter.next();
			count += 1;
			total += p.weight;
		} 
		return total/count;
	}

	public double averageHeight(){
		double total = 0.0;
		int count = 0;
		ListIterator <Person> p_iter = persons.listIterator(0);
		while (p_iter.hasNext()){
			Person p = p_iter.next();
			count += 1;
			total += p.height;
		} 
		return total/count;
	}

	public static void main(String args[]){ 
		
		try {
			BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

			System.out.print("Enter number of clusters: ");
			String line = in.readLine();
			int num_of_clusters = Integer.parseInt(line);
			System.out.println("the num of clusters:" + num_of_clusters);
		
			LinkedList <Cluster> clusters = new LinkedList <Cluster>();
			for (int i = 0; i < num_of_clusters; ++i){
				clusters.add(new Cluster());
			}

			//print the cluster list before adding persons
			ListIterator <Cluster> c_iter = clusters.listIterator(0); 
			while (c_iter.hasNext()){
				Cluster c = c_iter.next();
				System.out.println("Cluster address: " + c);
				System.out.println("Cluster weight: " + c.getWeight());
				System.out.println("Cluster height: " + c.getHeight());  
				System.out.println("Cluster persons: " + c.persons);
			}

			//read person list from file 
			LinkedList <Person> persons = new LinkedList <Person>();
			BufferedReader reader = new BufferedReader(new InputStreamReader(new BufferedInputStream(new FileInputStream(new File("person_data.csv")))));
			String fl;
         	while ((fl = reader.readLine()) != null) {
				//System.out.println(fl);
         		if (fl.contains("kg"))
         			continue;
         		String[] person_attr = fl.split(",");
         		Person p = new Person(person_attr[0], Integer.parseInt(person_attr[1]), Integer.parseInt(person_attr[2]));
         		persons.add(p); 	
         	}

			//now for every person get distance to each cluster
			ListIterator <Person> p_iter = persons.listIterator(0); 
			double distance;
			while (p_iter.hasNext()){
				Person p  = p_iter.next();
				//System.out.println("Person name: " + p.name);
				//System.out.println("Person weight: " + p.weight);
				//System.out.println("Person height: " + p.height);

				c_iter = clusters.listIterator(0);
				while (c_iter.hasNext()){
					distance = 0.0;
					Cluster c = c_iter.next();
					distance = Math.sqrt(Math.pow((p.weight - c.center.x),2) + Math.pow((p.height - c.center.y),2));
					//System.out.println(distance);
					p.dist_2_cluster_map.put(c, distance);  //create distance map
				}

				
				System.out.println("Distance map: " + p.dist_2_cluster_map);

				
				Cluster minKey = null;
				Double minValue = Double.MAX_VALUE;
				for (Map.Entry<Cluster, Double> entry : p.dist_2_cluster_map.entrySet()) {
    				Double value = entry.getValue();
   					if (value < minValue) {
        				minKey = entry.getKey();
        				minValue = value;
    				}
				} //ends c_iter	

				System.out.println("nearest cluster: " + minKey);
				System.out.println("Distance to nearest cluster: " + minValue);	
				int index = clusters.indexOf(minKey);
				System.out.println("Index of nearest cluster: " + index);	
				Cluster target_cluster = (Cluster)clusters.get(index);
				target_cluster.persons.add(p); //add the person to the nearest cluster
			} //ends p_iter

			//print out the cluster list again 
			//and see which persons have been added to
			ListIterator <Cluster> c_iter2 = clusters.listIterator(0); 
			while (c_iter2.hasNext()){
				Cluster c2 = c_iter2.next();
				System.out.println("Cluster address: " + c2);
				System.out.println("Cluster weight: " + c2.getWeight());
				System.out.println("Cluster height: " + c2.getHeight());  
				System.out.println("Cluster persons: " + c2.persons);
				System.out.println("Cluster average weight: " + c2.averageWeight());
				System.out.println("Cluster average height: " + c2.averageHeight());
			}

		}
		catch (IOException io){
			io.printStackTrace();
		}
		catch (Exception e){
			e.printStackTrace();
		}
	}
}

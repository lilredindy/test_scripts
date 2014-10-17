import java.awt.Point;
import java.util.*;


public class Person{

	public String name;
	public int weight;
	public int height;

	public HashMap <Cluster, Double> dist_2_cluster_map; 

	public Person(String name, int weight, int height){
		this.name = name;
		this.weight = weight;
		this.height = height;

		dist_2_cluster_map = new HashMap <Cluster, Double>();
	}

	public void setWeight(int weight){
		this.weight = weight;
	}
	public void setHeight(int height){
		this.height = height;
	}

	public int getWeight(){
		return this.weight;
	}
	public int getHeight(){
		return this.height;
	}

}
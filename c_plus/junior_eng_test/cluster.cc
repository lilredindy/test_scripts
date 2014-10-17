//for c
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
//and for c++
#include <cstdlib>
#include <vector>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>

using namespace std;

//////////////////////////////
/* Person class decl and def*/
//////////////////////////////
class Person {
	string name;
	double weight;
	double height;
public:
	Person(string name, double myWeight, double myHeight);
	~Person(){};
	string getName();
	double getWeight();
	double getHeight();
};

Person::Person(string myName, double myWeight, double myHeight) {
	name = myName;
	weight = myWeight;
	height = myHeight;
}

string Person::getName(){
	return name;
}

double Person::getWeight(){
	return weight;
}

double Person::getHeight(){
	return height;
}


///////////////////////////////
/* Cluster class decl and def*/
///////////////////////////////
class Cluster {
	double cWeight;
	double cHeight;
	vector <Person> ppl;
public:
	Cluster(double x, double y, vector <Person> persons);
	~Cluster(){};
	double getCenterWeight();
	double getCenterHeight();
	void setCenterWeight(double w);
	void setCenterHeight(double h);
	void addPerson(Person p);
	vector<Person> getPersons();
	void clearPersons();
};

Cluster::Cluster(double x, double y, vector <Person> persons) {
	cWeight = x;
	cHeight = y;
	ppl = persons;
}

double Cluster::getCenterWeight(){
	return cWeight;
}

double Cluster::getCenterHeight(){
	return cHeight;
}

void Cluster::setCenterWeight(double w){
	cWeight = w;
}

void Cluster::setCenterHeight(double h){
	cHeight = h;
}

void Cluster::addPerson(Person p){
	ppl.push_back(p);
}

vector<Person> Cluster::getPersons(){
	return ppl;
}

void Cluster::clearPersons(){
	ppl.clear();
}


////////////////////////
/* global random func */
////////////////////////
int random(int min, int max)
{
	int r;
	r = rand () % (max - min + 1) + min;
	return r;
}

//////////
/* main */
//////////
int main (int argc, char *argv[])
{
	
	////////////////
	/* read csv file */
	////////////////
	vector <Person> ppl;
	vector <string> v;
	
	string datafile;
	cout << "Please enter the full path to the data file: ";
	cin >> datafile;
	//ifstream in("/Users/shrikant/Development/person_data.csv"); 
	ifstream in(datafile.c_str()); 

	if(!in) { 
		cout << "Cannot open file.\n"; 
		return 0; 
	} 
	
	string line;
	string line_item;
	
	getline (in, line); //first line is label
	while(getline (in, line)) {
		istringstream linestream(line);
		while (getline (linestream, line_item, ','))
			v.push_back(line_item.c_str());
	}

	for(int i=0; i< v.size(); ){
		Person p(v[i], atoi((v[i+1]).c_str()),atoi((v[i+2]).c_str()));
		ppl.push_back(p);
		i = i + 3;
	}
/*
	for(int i=0; i< ppl.size(); ++i){
		cout << ppl[i].getName() << " \n";
		cout << ppl[i].getWeight() << " \n";
		cout << ppl[i].getHeight() << " \n";
	}
*/
	
	
	////////////////
	/* clusterize */
	////////////////
	int k = 0;
	vector <Cluster> clusters;
	
	cout << "Please enter the number of clusters: ";
	cin >> k;
	
	srand((unsigned)time(0)); 
	for (int i = 0; i < k; ++i)
	{		
		int cWeight = random (50, 150);
		int cHeight = random (38, 90);
		vector <Person> p; //placeholder
		Cluster c(cWeight,cHeight, p);
		clusters.push_back(c);
	}
	 
	
	/////////////////////////////////////////////////////////////////
	//do it 1000 times IN ORDER TO REFINE THE CENTER OF EACH CLUSTER
	/////////////////////////////////////////////////////////////////
	for (int iter = 0; iter <= 1000; ++iter)
	{
	
		double distance = 0;
		int index = 0;
		for(int i=0; i < ppl.size(); ++i){
			for (int j=0; j < clusters.size(); ++j){
				double d = sqrt(double(pow((ppl[i].getWeight() - clusters[j].getCenterWeight()),2) + pow((ppl[i].getHeight() - clusters[j].getCenterHeight()),2)));				
				if (j == 0)
					distance = d;
				if (d <= distance){
					distance = d;
					index = j;
				}	
			}
		
			//cout << distance << " is the distance\n";
			//cout << index << " is the index\n";
			clusters[index].addPerson(ppl[i]); //use shortest distance's index to add to correct cluster 
		}
	

		for (int i=0; i < clusters.size(); ++i){
			int w=0, h=0;
			double wAvg=0, hAvg=0;
			vector<Person> p = clusters[i].getPersons();
			//cout << "Cluster " << i + 1 << ":\n";
			//if (p.size() == 0) cout << "This cluster has no persons\n";
			for (int j=0; j < p.size(); ++j){
				w = w + p[j].getWeight();
				h = h + p[j].getHeight();
				//cout << "Name:" << p[j].getName() << ", Weight:"<< p[j].getWeight() << ", Height:"<< p[j].getHeight() << " \n";
			}
			
			if (p.size() != 0){
				wAvg = (double)w / p.size();
				//cout << wAvg << " is avg weight\n";
				clusters[i].setCenterWeight(wAvg);
				//cout << clusters[i].getCenterWeight() << " is center's new weight\n";
				
				hAvg = (double)h / p.size();
				//cout << hAvg << " is avg height\n";
				clusters[i].setCenterHeight(hAvg);
				//cout << clusters[i].getCenterHeight() << " is center's new height\n";
			}
			
			//clear the persons from each cluster until the last iteratiion
			if (iter != 1000)
				clusters[i].clearPersons();
		}
	} //closes 1000 iter
	
	for (int i=0; i < clusters.size(); ++i){
		cout << "Cluster " << i + 1 << ":\n";
		cout << "The center's weight is: " << clusters[i].getCenterWeight() << "\n";
		cout << "The center's height is: " << clusters[i].getCenterHeight() << "\n";
		vector<Person> p = clusters[i].getPersons();
		if (p.size() == 0)
			cout << "This cluster has no persons\n";
		for (int j=0; j < p.size(); ++j){
			cout << "Name:" << p[j].getName() << ", Weight:"<< p[j].getWeight() << ", Height:"<< p[j].getHeight() << " \n";
		}
		cout << "\n";
	}


	return (0);
}

from operator import itemgetter, attrgetter


def doctor_sort (csv_string):
	doctor_records = csv_string.split()
	for index in range(len(doctor_records)):
		doctor_records[index] = doctor_records[index].split(",")
	

	'''
	There's also a suggestion in the Python wiki under the heading 
	Sort Stability and Complex Sorts to do the sort in multiple passes, 
	from least significant key to most significant. 
	This works because Python's sort is guaranteed to be stable, 
	so the previous order is maintained when equivalent keys are encountered.
	
	#sorted(doctor_records, key=lambda records: records[3])   # sorted makes copy, needs assignment
	#key function is called exactly once for each input record
	#doctor_records.sort(key=lambda record: (float(record[3]), float(record[4]))) 
	#doctor_records.sort(key=itemgetter(3)) #sort is in place

	id,name,zip,scripts_per_week_avg,scripts_val_avg
	sort by scripts_per_week_avg,ascending
	secondary sort scripts_val_avg, descending
	return the same csv format
	'''
	
	print (doctor_records)
	doctor_records.sort(key=lambda record: float(record[4]), reverse=True)
	doctor_records.sort(key=lambda record: float(record[3]))
	print(doctor_records)

	for index in range(len(doctor_records)):
		doctor_records[index] = ",".join(doctor_records[index])

	sorted_csv = '\n'.join(doctor_records)
	

	return sorted_csv

csv = """1,alex,80405,13,5
3,bob,94123,320,1.5
2,jane,94032,35,2.8
4,will,94110,31.6,6.1
5,jess,94117,48,4
6,sam,94032,31.4,9
7,jim,94036,35,19"""


'''
expected_output:
1,alex,80405,13,5
6,sam,94032,31.4,9
4,will,94110,31.6,6.1
7,jim,94036,35,19
2,jane,94032,35,2.8
5,jess,94117,48,4
3,bob,94123,320,1.5
'''

print (doctor_sort(csv))



#print(sorted("This is a test string from Andrew".split() ))
#print(sorted("This is a test string from Andrew".split(), key=str.lower))

#dict = {'title': "this title", 'isbn': "234gdgg"}
#print(sorted (dict))



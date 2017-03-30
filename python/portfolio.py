import math

def day0_shares_bought(path):
	f = open(path + 'portfolio.csv', 'r')
	f.readline() #col labels for file
	l = []
	for line in f:
		l.append(int(line.split(",")[1] ))
	f.close()
	return l

def get_index(path):
	f = open(path + 'index_closing_prices.csv', 'r')
	f.readline() #col labels for file
	d= {}
	d['index_day0'] = float(f.readline().split(',')[1])
	d['index_day1'] = float(f.readline().split(',')[1])
	d['index_day2'] = float(f.readline().split(',')[1])
	f.close()
	return d


def create_dataset(path):
	f1 = open(path + 'stocks_info.csv', 'r')
	f2 = open(path + 'stocks_closing_prices.csv', 'r')
	f1.readline() #col labels for file
	f2.readline() #col labels for file
	my_list = []
	d1 = {}
	for index, line in enumerate(f2):
		d1['stock_name'] =  line.split(",")[0]
		d1['price_day0'] = float( line.split(",")[1])
		d1['price_day1'] = float( line.split(",")[2])
		d1['price_day2'] = float( line.split(",")[3])
		my_list.append(d1.copy()) 
	d2 = {}
	for index, line in enumerate(f1):
		d2['float'] = float( line.split(",")[3])
		my_list[index].update(d2.copy())
	d3 = {}
	for index,entry in enumerate(my_list):
		d3['cap_day0'] = entry['float'] * entry['price_day0']
		d3['cap_day1'] = entry['float'] * entry['price_day1']
		d3['cap_day2'] = entry['float'] * entry['price_day2']
		my_list[index].update(d3.copy())
	sum_cap_day0 = 0
	sum_cap_day1 = 0
	sum_cap_day2 = 0
	for entry in my_list:
		sum_cap_day0 += entry['cap_day0']
		sum_cap_day1 += entry['cap_day1']
		sum_cap_day2 += entry['cap_day2']
	d4 = {}
	for index,entry in enumerate(my_list):
		d4['w_day0'] =  entry['cap_day0'] / sum_cap_day0
		d4['w_day1'] =  entry['cap_day1'] / sum_cap_day1
		d4['w_day2'] =  entry['cap_day2'] / sum_cap_day2
 		my_list[index].update(d4.copy()) 
	d5 = {}
	l = day0_shares_bought(path)
	for index, entry in enumerate(my_list):
		d5['shares_day0'] = l[index]
		d5['shares_day1'] = int(round((entry['w_day1'] * (2500000 + 832704)) / entry['price_day1']))
		d5['shares_day2'] = int(round((entry['w_day2'] * (2500000)) / entry['price_day2']))
		my_list[index].update(d5.copy())
 	
 	f1.close()
 	f2.close()
	return my_list




path = raw_input('Enter path to index_rebalance_dataset: ')
list1 = create_dataset(path)
print(list1)

'''
sum = 0
for index, entry in enumerate(list1):
	sum += entry['price_day0'] * shares[index]
print (sum) #should equal 4167296
'''

sum = 0
for entry in list1:
	sum += entry['price_day1'] * entry['shares_day1']
	sum += entry['price_day2'] * entry['shares_day2']
print ("Leftover is: {}".format(5832704 - sum))




file = open(path + 'index_constituents.csv', 'w+')
file.write("Symbol,Quantity_Day_1,Quantity_Day_2\n")
for entry in list1:
	file.write("{},{},{}\n".format(entry['stock_name'],entry['shares_day1'],entry['shares_day2']))
file.close()






# Enter your code here. Read input from STDIN. Print output to STDOUT

#example:
# Enter the number of elements: 5
# Enter the elements: 5 10 20 25 30
# Output: 15

#example:
# Enter the number of elements: 3
# Enter the elements: 2 4 8
# Output: 6


print "Enter the number of elements: " 
n = int(raw_input())
l = list()
print "enter the elements: "
l = raw_input().split()
l = [int(i) for i in l]


d = list()
for i in range(len(l)-1):
    d.append((l[i+1] - l[i]))


for i in range(len(d)):
    for j in range(len(d)):
        if i != j:
            if d[i] == d[j]:
                diff = d[i] 


for i in range(len(l) -1):
	if (l[i] + diff != l[i+1]):
		result = l[i] + diff

print result


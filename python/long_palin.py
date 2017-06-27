#!/bin/python3

import sys


def transform(pairs, str, front_index, back_index):
    next = -1
    while (next):
        print ("transform()")
        if next != -1:
            str[back_index] = next 
            next = -1
        for pair in pairs[:]:
            print (pair,str[back_index], next)
            if pair[0] == str[back_index]:
                if pair[1] == str[front_index]:
                    str[back_index] = str[front_index]
                    return
                else:
                    next = pair[1]
                    pairs.remove((pair[0],pair[1])) #from original pairs
            elif pair[1] == str[back_index]:
                if pair[0] == str[front_index]:
                    str[back_index] = str[front_index]
                    return
                else:
                    next = pair[0]
                    pairs.remove((pair[0],pair[1])) #from original pairs
            
        
        if next == -1:
            next = 0
       
         
    
def long_palindrome(pairs, str):
        front_index = 0
        back_index = len(str) -1
        while (front_index < back_index):
            print("long_palindrome()")
            print(str)
            print("front: %s" % str[front_index])
            print("back: %s" % str[back_index])
            if str[front_index] != str[back_index]:
                transform(pairs[:], str, front_index, back_index)
                if (str[front_index] != str[back_index]):
                    str[back_index] = '-'
                    back_index = back_index - 1 
                    
                else:
                    front_index = front_index + 1
                    back_index = back_index - 1
            else:
                front_index = front_index + 1
                back_index = back_index - 1

        count = 0
        for char in str:
            if char != '-':
                count = count + 1
        
        print (count)
        return count


def make_dictionary(n,pairs):
    my_dict = {}
    for i in range(1, n+1):
        my_dict[i] = list()
    print (my_dict)

    for pair in pairs:
        if pair[1] not in my_dict[pair[0]]:
            my_dict[pair[0]].append(pair[1])
        if pair[0] not in my_dict[pair[1]]:
            my_dict[pair[1]].append(pair[0])
    print (my_dict)

    for key,value in my_dict.items():
        for i in list(value):
            my_dict[key].extend(x for x in my_dict[i] if x not in my_dict[key] and x is not key)
            #my_dict[key].update(my_dict[i])
    print (my_dict)
    return my_dict


n,k,m = raw_input().strip().split(' ')
n,k,m = [int(n),int(k),int(m)]
pairs = []
for a0 in range(k):
    x,y = raw_input().strip().split(' ')
    x,y = [int(x),int(y)]
    pairs.append((x,y))
A = list(map(int, raw_input().strip().split(' ')))
print (n,k,m)
print(pairs)
print (A)
D = make_dictionary(n,pairs)
long_palindrome(pairs, A)
 



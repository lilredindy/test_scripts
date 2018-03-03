#!/bin/python3

import sys
from random import randint
from collections import defaultdict

def raceAgainstTime(n, mason_height, heights, prices):
    # Complete this function
    d = defaultdict(int)
    print (n,mason_height, heights,prices)
    price = 0
    price2 = None
    current_height = mason_height

    for i in range(n-1):
        exch_time = heights[i] - current_height
        if (exch_time > 0): #make exchange
            print ("*")
            price+=exch_time
            price+=prices[i]
            current_height = heights[i]
        elif (prices[i]<0 and exch_time == 0):
            print ("**")
            price+=prices[i]
        elif ( abs(exch_time)+prices[i] < 0): #alt universe
            print ("***")
            tmp = None
            if (price2):
                tmp = price2  
            price2 = price
            price2+=abs(exch_time)
            price2+=prices[i]
            r = randint(1000,5000)
            print("prerace_{}: curh_{} nexth_{} tmp_{} price_{} prce2_{}".format(r,current_height,heights[i],tmp,price,price2))
            p = raceAgainstTime(n-(i+1),heights[i], heights[i+1:],prices[i+1:])
            p -= n-(i+1)
            price2+=p   
            if (tmp):
                if (price2 < price):
                    price = price2
                price2 = tmp
        
       
            print("postrace_{}: curh_{} nexth_{} tmp_{} price_{} prce2_{}".format(r,current_height,heights[i],tmp,price,price2))

    print ("n:{} price:{} price2:{}".format(n,price,price2))
    if price2 != None and price2 < price:
        return price2+n
    else: 
        return price+n

if __name__ == "__main__":
    #n = int(input().strip())
    #mason_height = int(input().strip())
    #heights = list(map(int, input().strip().split(' ')))
    #prices = list(map(int, input().strip().split(' ')))
    
    n = 10
    mason_height = 5 
    heights = [6,1,2,7,3,6,1,2,7]
    prices = [-2,-7,7,-2,-13,-2,-7,7,-2]
    result = raceAgainstTime(n, mason_height, heights, prices)
    print(result)

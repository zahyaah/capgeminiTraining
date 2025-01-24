import math

def sieveOfErasthosthenes(l, r):
    primesList = [True] * (r+1)
    primesList[0] = False 
    primesList[1] = False 

    for i in range(2, (int)(math.sqrt(r))+1):
        if primesList[i]:
            for j in range(i*i, r+1, i):
                primesList[j] = False

    
    for i in range(l, r+1):
        if primesList[i]:
            print(i)

def main():
    sieveOfErasthosthenes(0, 1)
    print("\n")
    sieveOfErasthosthenes(45, 10000)

main()
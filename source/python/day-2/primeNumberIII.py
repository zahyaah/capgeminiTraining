import math

def sieveOfErasthosthenes(l, r):
    primesList = [True] * (r+1)
    primesList[0] = False 
    primesList[1] = False 
    limit = (int)(math.sqrt(r))+1 
    i = 2
    while i < limit: 
        if (primesList[i]):
            j = i*i 
            while j <= r:
                primesList[j] = False 
                j += i
        i += 1

    
    i = l 
    while i <= r: 
        if primesList[i]:
            print(i)
        i += 1

def main():
    sieveOfErasthosthenes(0, 11)
    print("\n")
    # sieveOfErasthosthenes(45, 10000)

main()
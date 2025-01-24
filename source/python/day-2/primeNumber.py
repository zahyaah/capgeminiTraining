import math

def isPrimeNumber(n):
    if n < 2: 
        return False 
    if n <= 3:
        return True 
    if (n%2 == 0 or n%3 == 0):
        return False

    for i in range(5, (int)(math.sqrt(n))+1, 6):
        if (n%i == 0 or n%(i+1) == 0):
            return False 
    
    return True

print(isPrimeNumber(10)) 
print(isPrimeNumber(11)) 
print(isPrimeNumber(13)) 
print(isPrimeNumber(17)) 
print(isPrimeNumber(1)) 
print(isPrimeNumber(97)) 
print(isPrimeNumber(29)) 
print(isPrimeNumber(11)) 

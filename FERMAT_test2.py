#code to input a no and check for fermat primality test
from random import randint
import time
"""def modpow(x,n,m):
    if n==0:
        return 1
    elif n==1:
        return x
    elif n%2==0:
        return modpow(x*(x%m),n//2,m)%m
    elif n%2==1:
        return (x*modpow(x*(x%m),(n-1)// 2,m)%m)%m"""
        
def isprime(n):
    # the function returns true if n is prime else it returns false
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

def find_d(n):
    #this function returns value of d and r
    #n is odd so n-1 is even. we have to find d such that n-1=d.2^r
    count=0; #count stores the power of r
    m=n-1;
    while(m%2==0):
        m=m//2;
        count=count+1;
    d=m;
    s=count;
    return d,s
#Code to tabulate first nos pseudoprimes, nos is given by the user
num=3 # the starting number is set as 3
a=2
nos=0 # a counter to count number of prime numbers
t=time.time()
#we have specified a as 2 because we are checking only for strong base 2 pseudoprime
while(nos<20):
    if(not isprime(num)): # we are eliminating prime numbers as pseudoprimes are composite nos
        d,s=find_d(num)
        for r in range(0,s): 
            p=d*(2**r)
            if((pow(a,p,num)==num-1)):
                print(num)
                nos=nos+1
                

    num=num+2
b=time.time() #stores the current time
t2=b-t # stores the time to find nos numbers
print("The time taken to print ",nos," Strong base 2 pseudoprime numbers is : ",t2, "seconds")

    
    


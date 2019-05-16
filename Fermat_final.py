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
def isprime(n): # The function returns true if n is prime else false
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

num=2047
def find_d(n):
    
    #this function returns value of d and r
    #n is odd so n-1 is even. we have to find d such that n-1=d.2^r
    count=0;
    m=n-1;
    while(m%2==0):
        m=m//2;
        count=count+1; #count stores d power of 2
    d=m;
    r=count;
    return d,r
#Code to tabulate first nos pseudoprimes where nos is given by the user
def fermat_1(num):
    a=2#we have specified a as 2 because we are checking only for strong base 2 pseudoprime
    if(not isprime(num)):
        d1,r1=find_d(num)
        if (pow(a,d1,num)==1):#if (a^d)%num equals 0 then it is a fermat pseudoprime number
            return True
    return False
def fermat_2(num):
    a=2
    if(not isprime(num)): # we are eliminating prime numbers as pseudoprimes are composite nos
        d,s=find_d(num)
        for r in range(0,s): 
            p=d*(2**r)
            if((pow(a,p,num)==num-1)):
                return True
    return False
nos=0
t=time.time()
while(nos<20):
    if(fermat_1(num) or fermat_2(num)):
        print(num)
        nos=nos+1
    num=num+2
b=time.time()
print("The time required to print ",nos, "Fermat Pseudoprime numbers is : ",(b-t))
    
    


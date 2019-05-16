#code to input a no and check for fermat primality test
from random import randint
import time
from fractions import gcd
from math import sqrt
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
    """if(n%2==0):
        print("Number must be odd")
        return 0,0"""
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
d=5 # d is the discriminant i.e. p^2-4q
p=1 
q=-1
al= (p+(d**0.5))*0.5  # roots of the equation
be= (p-(d**0.5))*0.5  #x^2-px+q
def js(a,p):   # to find the jacobian symbol
    if(a%p==0):
        return 0
    elif (isSquare(a%p)==1):
        return 1
    else:
        return -1
def u(n):   #to find Un using iteration
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':    v1, v2, v3 = v1+v2, v1, v2
    return v2
def U(n):   # to find Un using recursion
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
      return p*U(n-1)-q*U(n-2)


def isSquare(x):  # to check whether a number is a perfect square
    if x == 1:
        return 1
    low = 0
    high = x // 2
    root = high
    while root * root != x:
       root = (low + high) // 2
       if low + 1 >= high:
          return 0
       if root * root > x:
          high = root
       else:
          low = root
    return 1
def lucas(n): # returns true if the number is Lucas else eturns False
    if(not isprime(n)):
        if(gcd(n,5)==1):
            delta=n+1
            a=u(delta)%n
            if(a==0):
                return True
    return False
nos=0
no=3
t=time.time()
while(nos<10): #main function to tabulate lucas pseudoprime numbers
    #if(fermat_1(num) or fermat_2(num)):
    if(fermat_1(num) or fermat_2(num)):
        if(lucas(num)):
            print(num)
            nos=nos+1
    no=no+2
b=time.time()
print("The time required to print ",nos, " Pseudoprime numbers is : ",(b-t))
    
    


from fractions import gcd
from math import sqrt
import time

d=5 # d is the discriminant i.e. p^2-4q
p=1 
q=-1
al= (p+(d**0.5))*0.5  # roots of the equation
be= (p-(d**0.5))*0.5  #x^2-px+q

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

def js(a,p):   # to find the jacobian symbol
    if(a%p==0):
        return 0
    elif (isSquare(a%p)==1):
        return 1
    else:
        return -1

def U(n):   # to find Un using recursion
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
      return p*U(n-1)-q*U(n-2)


def u(n):   #to find Un using iteration
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':    v1, v2, v3 = v1+v2, v1, v2
    return v2

def prime(num): # returns true if the number is prime else returns false
    if n==2:
        return True
    if n==3:
        return True
    if n%2==0:
        return False
    if n%3==0:
        return False
    i=5
    w=2
    while(i*i<=n):
        if(n%i==0):
            return False
        i+=w
        w=6-w
    return True
nos=0
n=3
t=time.time() #stores the current time

while(nos<20):
    if(not prime(n)):
        t1=(time.time())*60
        if(gcd(n,5)==1):
            delta=n+1
            a=u(delta)%n
            if(a==0):
                print(n)
                nos=nos+1
    n=n+2
t2=time.time()  #stores the current time
T=t2-t
print("The time taken to print ",nos," Lucas pseudoprime numbers is : ",T, "seconds") 

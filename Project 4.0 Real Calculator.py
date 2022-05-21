from ast import Mult
from math import remainder
from statistics import multimode



def add(a,b):
    sum=a+b
    print(f"the sum of {a} and {b} is {sum}") #formatted strings
def minus(a,b):
    if a>b:
        subtract=a-b
    else:
        subtract=b-a
    print(f"the difference between {a} and {b} is {subtract}")
def into(a,b):
    mult=a*b
    print(f"the product of {a} and {b} is {mult}")        
def by(a,b):
    quotient=a/b
    print(f"the result of {a}/{b} is {int(quotient)}")    
def modulus(a,b):
    remainder=a%b
    print(f"the result of {a}%{b} is {int(remainder)}")    


n1, op, n2= map(str, input("Enter equation").split()) #multiple inputs in a single line
n1=int(n1)
n2=int(n2)
if op=='+':
    add(n1,n2)
elif op=='-':
    minus(n1,n2)
elif op=='x':
    into(n1,n2)
elif op=='/':
    by(n1,n2)
elif op=='%':
    modulus(n1,n2)
else:
    print("Enter a valid operator") 
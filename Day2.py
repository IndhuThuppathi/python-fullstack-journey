#arithmetic & math
f=10
#f=f+1
f+=1
print(f)

f=10
#f=f-1
f-=1
print(f)

f=10
#f=f*1
f*=1
print(f)

f=10
#f=f/1
f/=1
print(f)

f=10
#f=f%1
f%=1
print(f)

#math functions

x=-3.6
y=-8
z=10
#result=round(x)
#result=max(x,y,z)
#result=min(x,y,z)
#result=pow(2,2)
#result=abs(x)

import math
x=3.6
#x=math.sqrt(x)
#x=math.ceil(x)
x=math.floor(x)
print(x)

#circumfarance of circle

#radius=int(input("enter radii:"))
#=round(2*math.pi*radius)
#print(f"the circumference of circle is {c}")

#area of circle

#radius=int(input("enter radii:"))
#a=math.pi *pow(radius,2)
#print(f"the area of circle is {a}")

#hypotenus of right angle triangle
#a=int(input("enter a: "))
#b=int(input("enter b: "))
#c=math.sqrt(pow(a,2)+pow(b,2))
#print(f"side c is {c}")

#if=do only if condition is true
#else= do something if not is correct

#age=int(input("enter age:"))
#if(age>=18):
 # print("you signed in")
#else:
 # print("you signed in")

#calculater program

#operator=input("enter +,-,*,/: ")
#num1=float(input("enter number 1: "))
#num2=float(input("enter number 2: "))
#if(operator=='+'):
 # r=num1+num2
  #print(r)
#elif(operator=='-'):
 # r=num1-num2
  #print(r)
#elif(operator=='*'):
 # r=num1*num2
  #print(r)

#else:
 # r=num1/num2
  #print(r)

#temperature conversion program 


temp = float(input("Enter temperature: "))
unit = input("Enter unit (C/F): ")

if unit == "C":
    fahrenheit = (temp * 9/5) + 32
    print("Temperature in Fahrenheit:", fahrenheit)

elif unit == "F":
    celsius = (temp - 32) * 5/9
    print("Temperature in Celsius:", celsius)

else:
    print("Invalid unit")






#print()
print("hello world")

#variable

#1.string
first_name="Indhu"
print(f" hello {first_name}")
#2.integer
age = 15
print(f"you are {age} years old")
discount=20
print(f"you got rs {discount} ")
#3.float
price=10.99
print(f"price of a product is ${price}")
#4.boolean
is_student=True
print(f"are you a student?{is_student}")


#typecasting

name="indhu"
print(type(name))

gpa=3.2
gpa=int(gpa)
print(gpa)

age=25
age=float(age)
print(age)
age=25
age=str(age)
print(age)
print(type(age))
age+='1'

print(age)

name="b"
name=bool(name)
print(name)

name=""
name=bool(name)
print(name)

#use input
name=input("what is your name?")
age=input("what is your age?")
age=23
age=int(age)
age+=1


print(f"my name is {name}")
print("happy birthday")
print(f"my age is {age}")

#ex-1->area of rectangle
l=float(input("enter the length"))
w=float(input("enter the width"))
a=l*w
print(f"the area of rectangle is{a}")

#madlibs game
#creating a story

animal=input("enter animal")
adj1=input("how it is")
verb=input("what it is doing")
noun=input("enter suitable noun")
print(f"i went to {animal} park")
print(f"i saw {adj1} monkey")
print(f"it is {verb} ")
print(f" {noun} was happy")




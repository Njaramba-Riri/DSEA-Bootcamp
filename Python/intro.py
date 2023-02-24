#Variables and Datatypes
name ="James"
last="Riri"
f_name=(name+last)
print(f_name)
type(f_name)

"""Variable names"""

#mathematical operators
a=5
b=6
c=a**b #Exponential
d=c+a #addition
e=d//3 #floor division
f=e%a #modulus

print(c,d,e,f)  

#control structure and conditional statements:
#for loop
for i in range(2,-2,11):
    print(i)

#while loop
i=0
while i<5:
    print(i)
    i+=2

#if
age=int(input('Enter your age: '))

if age>=18:
    print('Congrats, you can vote')

#if...else
age=18

if age>=18:
    print('Congrats, you can vote')

else:
    print("Too young to vote")

#if...else for a traffic light
color=str(input("Enter traffic light color: "))

"""
Red=Stop
yellow=wait
green=go
"""
#elif allows for control system to take a number of #inputs as arguments
if color=='Red':
    print("Stop! ")
elif color=='Yellow':
    print('Wait')
elif color=='Green':
    print('Go')
else:
    print('Color not recognised')


num=int(input('Enter first number: '))
num2=int(input('Enter second number: '))

if num>num2:
    print(num2,num)
else:
    print(num,num2)

#funtions in python
def get_name():
    user_name=input("What's your name?: ")
    return user_name
get_name()

#funtion to print a user defined message
def print_msg(user_name):
    print("Hello", user_name)
print_msg("Riri")

def main():
    user_name=get_name()
    print_msg(user_name)
main()

"""A funtion that asks a user to enter a number and saves it to avariable num, then another funtion counts from 1 to that number"""

def ask_value():
    num=int(input("Enter a number: "))
    return num
def count(num):
    n=1
    while n<=num:
        n=n+1
def main():
    num=ask_value()
    count(num)

main()

#lists, Tuples, Sets and dictionaries

#list-
name1='Leah'
name2='Wanjiru'

namelist=[name1, name2]
type(namelist)
print(namelist)

#Tuple- Similar to a list but can't be modified
nametuple=(name1,name2)
print(nametuple)
type(nametuple)

#Set- Doesn't  print repeated values
Employees={'Wangari','Oganda','Michael','Dennis', 'Oganda','Michael', 'John'}
print(Employees)
type(Employees)

#Dictionary
students={
    "name":['Kim','Mary','Joan','Melvin'],
    "age":[19,22,20,23],
    "grade":['A','C+','B','F'],
    "Score":[90,57,69,23]
}

print(students)
type(students)


"""Importing packages and classes"""
import math as m

m.factorial(5)

m.sqrt(4)

m.tan(120)

m.log(10)

class myclass:
    def add(self, a, b):
        return a+b

obj=myclass()
obj.add(5,6)
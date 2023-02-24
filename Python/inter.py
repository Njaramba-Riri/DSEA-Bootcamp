#Python Classes
#The __init__() funtion- executed whenever the class isbeing initiated, it is used to assign values to object properties, or other properties

class student:
    def __init__(self, name, age, school):
        self.name=name
        self.age=age
        self.school=school

student1=student("Ryan Breezy",12,"Wintwaters Elementary")

print(student1.name)
print(student1.age)
print(student1.school)

#The __str__() funtion-controls what should be returned when the class object is represented as a string.if it's not set, the string representation of the object is returned.

class car:
    def __init__(self, make,year):
        self.make=make
        self.year=year

    def __str__(self):
        return f"{self.make}({self.year})"

car1=car("Porsche",2021)
car2=car("Tesla",2022)

print(car1)
print(car2)


#Object methods
class person:
    def __init__(self, name,age):
        self.name=name
        self.age=age

    def newfunc(self):
        print("Hey there, I'm ",self.name,"and I am",self.age,"years old")

p1=person("Antony Odiwuor", 25)
p1.newfunc()
#Self parameter is just a reference to the current instance of the class and is used to acces variables used in the said class.matter of fact, you can change the "self" word into anyword you want and the code would still work.

#Class Inheritance
class animals:
    def __init__(self, type, legs):
        self.type=type
        self.no_of_legs=legs

    def printanimal(self):
        print(self.type, self.no_of_legs)

#create an object and execute using printanimal method:
x=animals("Carnivorous", 4)
x.printanimal()

#create a child class which inherits all properties and methods of the animals class.
#The pass keyword is used when you don't want to add any other properties or methods to the class.
class elephant(animals):
    pass

y=elephant("Herbivorous",4)
y.printanimal()

#Adding the __init__() funtion, this makes the child's init funtion override the parent's init function.
class elephant(animals):
    def __init__(self, weight, age):
        self.weight=weight
        self.age=age

#To keep tyhe parent's init funtion use:
class elephant(animals):
    def __init__(self, type, legs):
        animals.__init__(self, type, legs)

#Super()Function-this func makes the child class inherit all the methods and properties from its parent:
class elephant(animals):
    def __init__(self,type, legs):
        super().__init__(type, legs)
        self.game_park="Maasai Mara" #Anew property to the elephant classs.

#Writing smooth python program
name="Jane Waitherero Kimani"
first_name,middle_name,last_name=name.split()
print(last_name,first_name,middle_name, sep=',')


#Strings in Python
string="DSEA IS SO WASSUP"
print(string.lower())#lowercase
#joining strings
"Folks"+"it's February"
#repeating a string
3*"February"
#Membership operators in python- checks a value if it is present in a sequence.
"b" in "these people are so boring"
"x" not in "why are y'all so good? Xoxo :)"

#F-string formatting
name=str(input("What is your name?: "))
city=str(input("Where are you from?: "))
age=int(input("What is your age?: "))

f_literal=f"Hello there, I'm {name} from {city}, and I'm {age} years old."

print(f_literal)

#Zip funtion
names=['Martin','Ozark','Grace','Jane']
school=['RPM','Wintwaters','Riara','Alliance']
name_school=zip(names,school)
print(dict(name_school))

#enumerate function-assigns index values 
lst=['Name','Age','School','Reg_no']
out=dict(enumerate(lst))
print(out)

#Counter() function-Let's you count how many times a value occurs in a sequence

from collections import Counter
cou=['Free','Thugger','Not','Thugger','Camp','New','Free','Jersey']
print(Counter(cou))

#List Comprehension- offers a shorter syntax when you want to create a new list from an existing list in python

names=['John','Kimani','Jacob','Juliet','Leah','Wangechi','Lucy','James','Danice']
newnames=[]

for X in names:
    if "J" in X:
        newnames.append(x)

print(newnames)
#The above program is without list comprehension,but with list comprehension you can do all this in one line of code.
names=['John','Kimani','Jacob','Juliet','Leah','Wangechi','Lucy','James','Danice']
newnames=[X for X in names if "J" in X]

print(newnames)

#Just a recap
#if...else statements
values=[1,3,5,7,6,0]
i=3

for i in values:
    print(f"Yes 3 is present in the list.")
else:
    print(f"Nope,3 is not present in the list.")

#Range() function & if....else
for i in range(2,20):
    i=i+1
    print("Here are the values.")

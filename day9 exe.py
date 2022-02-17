"""y="Hello Live"
m=y.maketrans("e","w")
print(y.translate(m))"""

"""txt="500"
x=txt.zfill(10)
print(x)"""

"""items=[n for n in input().split('-')]
items.sort()
print('-'.join(items))"""


"""student_list = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
print("Original dictionary: ",student_list)
student_dict = {x.translate({32: None}): y for x, y in student_list.items()}
print("New dictionary: ",student_dict)"""

"""from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d = Counter(d1) + Counter(d2)
print(d)"""


"""import random 
nums = [1, 2, 3, 4, 5]
print("Original list:")
print(nums)
random.shuffle(nums)
print("Shuffle list:")
print(nums)
words = ['red', 'black', 'green', 'blue']
print("\nOriginal list:")
print(words)
random.shuffle(words)
print("Shuffle list:")
print(words)"""



"""class India():
	def capital(self):
		print("New Delhi is the capital of India.")

	def language(self):
		print("Hindi is the most widely spoken language of India.")

	def type(self):
		print("India is a developing country.")

class USA():
	def capital(self):
		print("Washington, D.C. is the capital of USA.")

	def language(self):
		print("English is the primary language of USA.")

	def type(self):
		print("USA is a developed country.")

obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
	country.capital()
	country.language()
	country.type()"""






"""class Bird:
        def intro(self):
                print("There are many types of birds.")
	
        def flight(self):
                print("Most of the birds can fly but some cannot.")

class sparrow(Bird):
        def flight(self):
                print("Sparrows can fly.")
class ostrich(Bird):
        def flight(self):
                print("Ostriches cannot fly.")
	
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()

"""

"""from abc import ABC, abstractmethod   
class Car(ABC):   
    def mileage(self):   
        pass  
  
class Tesla(Car):   
    def mileage(self):   
        print("The mileage is 30kmph")   
class Suzuki(Car):   
    def mileage(self):   
        print("The mileage is 25kmph ")   
class Duster(Car):   
     def mileage(self):   
          print("The mileage is 24kmph ")   
  
class Renault(Car):   
    def mileage(self):   
            print("The mileage is 27kmph ")   
          
# Driver code   
t= Tesla ()   
t.mileage()   
  
r = Renault()   
r.mileage()   
  
s = Suzuki()   
s.mileage()   
d = Duster()   
d.mileage()

"""





"""from abc import ABC  
  
class Polygon(ABC):   
  
   # abstract method   
   def sides(self):   
      pass  
  
class Triangle(Polygon):   
  
     
   def sides(self):   
      print("Triangle has 3 sides")   
  
class Pentagon(Polygon):   
  
     
   def sides(self):   
      print("Pentagon has 5 sides")   
  
class Hexagon(Polygon):   
  
   def sides(self):   
      print("Hexagon has 6 sides")   
  
class square(Polygon):   
  
   def sides(self):   
      print("I have 4 sides")   
  
# Driver code   
t = Triangle()   
t.sides()   
  
s = square()   
s.sides()   
  
p = Pentagon()   
p.sides()   
  
k = Hexagon()   
K.sides()   



"""
#Lambda
#lambda arguments: expression


# a is an argument and a+10 is an expression which got evaluated and returned.    
"""x = lambda a:a+10   
# Here we are printing the function object  
print(x)  
print("sum = ",x(20))





def x(a):  
    return a+10  
print(sum = x(10))


"""
# a and b are the arguments and a*b is the expression which gets evaluated and returned.    
"""x = lambda a,b: a*b  
print("mul = ", x(20,10))  

#the function table(n) prints the table of n    
def table(n):    
    return lambda a:a*n # a will contain the iteration variable i and a multiple of n is returned at each function call    
n = int(input("Enter the number:"))    
b = table(n) #the entered number is passed into the function table. b will contain a lambda function which is called again and again with the iteration variable i    
for i in range(1,11):    
    print(n,"X",i,"=",b(i)) #the lambda function b is called with the iteration variable i  



"""

#program to filter out the tuple which contains odd numbers    
"""lst = (10,22,37,41,100,123,29)  
oddlist = tuple(filter(lambda x:(x%3 == 0),lst)) # the tuple contains all the items of the tuple for which the lambda function evaluates to true    
print(oddlist)

"""
"""lst = (10,20,30,40,50,60)  
square_list = list(map(lambda x:x**2,lst)) # the tuple contains all the items of the list for which the lambda function evaluates to true    
print(square_list)    



"""
#EX
"""import datetime
now = datetime.datetime.now()
print(now)
year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
t = lambda x: x.time()
print(year(now))
print(month(now))
print(day(now))
print(t(now))

"""
# Python program to display calendar of
# given month of the year

# import module
"""import calendar

yy = 2017
mm = 11

# display the calendar
print(calendar.month(yy, mm))



"""
"""
# Python code to demonstrate the working of
# calendar() function to print calendar

# importing calendar module
# for calendar operations
import calendar

# using calendar to print calendar of year
# prints calendar of 2018
print ("The calendar of year 2018 is : ")
print (calendar.calendar(2018, 2, 1, 6))


"""

"""
# Python program to demonstrate working of formatmonth() method

# importing calendar module
import calendar

text_cal = calendar.TextCalendar()


# default value of width is 0

# printing formatmonth
print(text_cal.formatmonth(2018, 9, w = 5))


"""






"""

# Python program to demonstrate working of formatmonth() method

# importing calendar module
import calendar

text_cal = calendar.TextCalendar(firstweekday = 0)


# giving value of width = 6, line = 2

# printing formatmonth
print(text_cal.formatmonth(2018, 10, 6, 2))


"""


# Python program to demonstrate working of prmonth() method

# importing calendar module
"""import calendar

text_cal = calendar.TextCalendar(firstweekday = 0)


# giving value of width = 6, line = 2

# printing prmonth
print(text_cal.prmonth(2018, 10, 6, 2))

"""

"""
# Python program to demonstrate working of formatyear() method

# importing calendar module
import calendar

text_cal = calendar.TextCalendar(firstweekday = 0)


# default value of width is 0

# printing formatyear
print(text_cal.formatyear(2018, 5, c = 3, m = 2))





"""


import random
import math
# Taking Inputs
lower = int(input("Enter Lower bound:- "))

# Taking Inputs
upper = int(input("Enter Upper bound:- "))

# generating random number between
# the lower and upper
x = random.randint(lower, upper)
print("\n\tYou've only ",
	round(math.log(upper - lower + 1, 2)),
	" chances to guess the integer!\n")

# Initializing the number of guesses.
count = 0

# for calculation of minimum number of
# guesses depends upon range
while count < math.log(upper - lower + 1, 2):
	count += 1

	# taking guessing number as input
	guess = int(input("Guess a number:- "))

	# Condition testing
	if x == guess:
		print("Congratulations you did it in ",
			count, " try")
		# Once guessed, loop will break
		break
	elif x > guess:
		print("You guessed too small!")
	elif x < guess:
		print("You Guessed too high!")

# If Guessing is more than required guesses,
# shows this output.
if count >= math.log(upper - lower + 1, 2):
	print("\nThe number is %d" % x)
	print("\tBetter Luck Next time!")

# Better to use This source Code on pycharm!"""

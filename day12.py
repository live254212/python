"""a="no"
c=a[::-1]
if c==a:
    print("it is a palindrome")
else:
    print("it is not a palindrome")"""
    
"""
def num(x):
    def add(y):
        print(x+y)
    return add
r=num(7)
r(7)"""


"""#from collections import Counter
a="listen"
b="silent"
if(sorted(a)==sorted(b)):
    print("it is anagram")
else:
    print("it is panagram")"""

"""b=["malayalam"]
x=list(filter(lambda x:(x=="".join(reversed(x))),b))
print(x)"""


"""from Day11 import*


ans = isPalindrome("madam")

if (ans):
	print("Yes")
else:
	print("No")"""

"""try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")"""
"""try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")"""
"""try:
    x="f"
    print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")"""
"""try:
  f = open("demofile.txt")
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()"""

"""x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")

"""
"""x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")"""
"""amount = 10000

# check that You are eligible to
# purchase Dsa Self Paced or not
if(amount>2999)
	print("You are eligible to purchase Dsa Self Paced")"""

"""try:
	print("code start")
		
	# unsafe operation perform
	print(1 / 0)

# if error occur the it goes in except block
except:
	print("an error occurs")

# final code in finally block
finally:
	raise Exception("GeeksForGeeks")"""


"""try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
    print(num)
except:
    print("Not an even number!")
else:
    reciprocal = 1/num
    print(reciprocal)"""
# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass


class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass


class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass


# you need to guess this number
number = 10

# user guesses a number until he/she gets it right
while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("This value is too small, try again!")
        print()
    except ValueTooLargeError:
        print("This value is too large, try again!")
        print()

print("Congratulations! You guessed it correctly.")











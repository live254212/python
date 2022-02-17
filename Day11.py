"""def ab(m="n",**a):
    print(a,m)
ab(h=90,b="h")"""
#iterator
#iter()-create object for iterator
#next-Move to next value
"""class live:
    def __init__(a):
        a.num=1
    def __iter__(a):
        return a
    def __next__(a):
        if a.num<=10:
            val=a.num
            a.num+=1
            return val
        else:
            pass 
v=live()

for i in v:
    print(i)"""

#string
"""m=[4,7,8,9,10]
l=iter(m)
print(l.__next__())
print(l.__next__())"""

"""def sqrt():
    n=1
    while n<=10:
        sq=n*n
        yield sq
        n+=1
v=sqrt()
for i in v:
    print(i)"""

"""def my_gen():
    n = 1
    print(n)
    #print('This is printed first')
    # Generator function contains yield statements
    #yield n
   

    #n += 1
    #print('This is printed second')
    #yield n

    #n += 1
    #print('This is printed at last')
    #yield n
    print(n)

my_gen()
# Using for loop
#for item in my_gen():
   # print(item)"""

"""def num(x):
    def add(y):
        print(x+y)
    
    return add
r=num(7)
r(7)"""


def n():
    x=100
    def add():
        print(x)
    return add
r=n()
r()

# function to check string is
# palindrome or not
def isPalindrome(s):

	# Using predefined function to
	# reverse to string print(s)
	rev = ''.join(reversed(s))

	# Checking if both string are
	# equal or not
	if (s == rev):
		return True
	return False

# main function
#s = "malayalam"
#ans = isPalindrome(s)

#if (ans):
	#print("Yes")
#else:
	#print("No")








        

    
   

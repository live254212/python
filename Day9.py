"""class parent1:
    def first3(a):
        a=20+25
        print(a)
class parent1(parent1):
    def first3(a):
        super().first3()
        a=20+5
        print(a)

class child2(parent1):
    def first1(a):
        a=20+75
        print(a)
class child3(child2):
    def first(a):
        a=20+45
        print(a)
d=child3()
d.first()
d.first1()
d.first3()
#d.first3()"""

"""class parent1:
    def first4(a):
        a=20+25
        print(a)
class parent2:
    def first3(a):
        a=20+5
        print(a)

class child2(parent2,parent1):
    def first1(a):
        a=20+75
        print(a)
class child3(child2):
    def first(a):
        a=20+45
        print(a)
c=child3()
c.first()
c.first1()
c.first3()
c.first4()"""

"""def add(a,b):
    c=a+b
    print(c)"""
#print("Hello"+__name__)
"""def main():
    print("Hello")
if __name__=='__main__':
    main()
"""
"""class cmp:
    def __init__(a):
        print("I am __init__")

    def config(self):
        print("kk")
h=cmp()
h1=cmp()
h.config()
h1.config() """

class cmp:
    def __init__(a,cpu,k):
        print("I am __init__")
        a.cpu=cpu
        a.key=k

    def config(self):
        print("kk",self.cpu,self.key)
h=cmp("w10",8)
h1=cmp("w7",7)
h.config()
h1.config()        

#first python

from datetime import time
from datetime import date
from datetime import datetime

def main():
    today=datetime.now()
    wd = date.weekday(today)
    days =["Monday","Tuesday","Wedsday","Thursday","Friday","Satday","Sunday"]
    print "today is day number %d " % wd
    print "which is a " + days[wd]
    
    
if __name__ == "__main__":
    main()


    
'''

print "START"
    today = date.today()
    print "Today's date is: ", today
    print "Date components: ", today.day, today.month, today.year
    print "weekday: ", today.weekday()
    dayandtime = datetime.now()
    print "date and time is: ", dayandtime
    print "date and time is: ", datetime.now()
    t = datetime.time(datetime.now())
    print "current time is: ", t
    #print datetime.time()
    
class myClass():
    def method1(self):
        print "myClass method1"
    def method2(self, someString):
        print "myClass method2: " + someString

class anotherClass(myClass):
    def method2(self):
        print "another Class method2"
    def method1(self):
        myClass.method1(self);
        print "another Class method1"

  
print "HELLO"
def main():
  print "** START **"
  c = myClass()
  c.method1()
  c.method2("this is a string")
  c2 = anotherClass()
  c2.method1()
  c2.method2()

days =["Mon","Tues","Weds","Thurs","Fri","Sat","Sun"]
for x, y in enumerate(days):
    print x, y



x = 0
for x in range (5,10):
    #if (x==7):break
    if (x % 2 ==0):continue
    print x


days =["Mon","Tues","Weds","Thurs","Fri","Sat","Sun"]
for d in days:
    print d

x = 0
for x in range (5,10):
    print x



while x < 5:
    print x
    x +=  1


x, y = 100, 100

if x < y:
    st="x is less than y"
elif x == y:
    st="x is the same as y"
else:
    st="x is not less than y"

st = "x is greater than y" if (x>y) else "x is less than or equal to y"
print st


if __name__ == "__main__":
    main()

def func1():
    print "I am a function"


def func2 (arg1, arg2):
    print arg1, "  ", arg2

func2(10,20)
print func2(10,20)

def cube(x):
    return x*x*x

print cube(3)


def power(num, x=1):
    result = 1;
    for i in range (x):
        result = result * num
    return result

print power(x=3 , num=2)

def multi_add(*args):
    result = 0;
    for x in args:
        result += x
    return result

print multi_add(3,4,5,6,6,556,1000)

'''

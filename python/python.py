#first python

import calendar

c = calendar.TextCalendar(calendar.MONDAY)
#str = c.formatmonth(2015, 9 ,0, 0)
#print str

#ch = calendar.HTMLCalendar(calendar.MONDAY)
#str = ch.formatmonth(2015, 9)
#print str

#for i in c.itermonthdays(2015, 9):
#    print i

print "MONTHS"
for name in calendar.month_name:
    print name
print "DAYS"
for day in calendar.day_name:
    print day
'''


def main():
    #print timedelta(days=365, hours=5, minutes=1)
    print "today is: " + str(datetime.now())
    print "one year from now it will be " + str(datetime.now() + timedelta(days=365))

if __name__ == "__main__":
    main()

from datetime import time
from datetime import date
from datetime import datetime
from datetime import timedelta

#print timedelta(days=365, hours=5, minutes=1)
print "today is: " + str(datetime.now())
print "one year from now it will be " + str(datetime.now() + timedelta(days=365))


t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%Y, %A, %B, %d, %H:%M")
print "One week ago it was: ", s

    #formstting date and time
    now=datetime.now()
    print now.strftime("%Y")
    print now.strftime("%A")
    print now.strftime("%B")

    print now.strftime("%y")
    print now.strftime("%a")
    print now.strftime("%b")
    
    print now.strftime("%A, %d %B, %Y")

    print now.strftime("%c")

    print now.strftime("%I, %M %S, %p")
    print now.strftime("%H:%M")
    
today=datetime.now()
    print today
    wd = date.weekday(today)
    print wd
    days =["Monday","Tuesday","Wedsday","Thursday","Friday","Satday","Sunday"]
    print "today is day number %d " %wd
    print "which is a " + days[wd]

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

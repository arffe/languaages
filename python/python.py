#first python

def main():
    print "** START **"

days =["Mon","Tues","Weds","Thurs","Fri","Sat","Sun"]
print days[3], days[4]

'''
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

#wap to add first seven terms twice i.e 1/1!+2/2!+3/3!+...
import math
sum_numbers=0
for i in range(1,8):
    sum_numbers +=i/math.factorial(i)
    result=2*sum_numbers
    print("the sum of numebers added twice",result)
#wap to print all prime numbers from 900 to 1000
x=900
y=1000
print("prime numbers between",x,"and",y,"are:")
for num in range(x,y):
    if num > 1:
        for i in range(2,num):
            if(num%i)==0:
               break
        else:
            print(num)
#wap to print multiplication table
for a in range(1,6):
    print(a,"table")
    for b in range(1,11):
        c=a*b
        print(a,"x",b,"=",c)
    print()
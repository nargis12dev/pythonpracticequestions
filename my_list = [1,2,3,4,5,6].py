#my_list = [1,2,3,4,5,6]
#my_list[0],my_list[-1]=my_list[-1],my_list[0]
#print(my_list)

#swaping by temporary method
#def swaplist(newlist):
  #  size = len(newlist)
  #  temp = newlist[0]
  #  newlist[0]=newlist[size-1]
  #  newlist[size-1] = temp
  #  return newlist
#newlist = [1,2,4,5,6,8]
#print(swaplist(newlist))

#swaping of list by tuple variable
#def swaplist(list):
    #get=list[-1],list[0]
    #list[0],list[-1]=get
    #return list
#newlist=[2,3,4,5,6,8]
#print(swaplist(newlist))

#lsit swaping using operand
#list=[1,2,3,4,5,6]
#a,*b,c = list
#print(a)
#print(b)
#print(c)

#program to print first 10 natural numbers and their sum 
#sum=0
#for i in range(1,11):
 #print(i,end=" ")
 #sum=sum+i
 #print()
#print("the sum of first ten natural numbers is", sum)

#wap to print multiplication table of number entered by the user
#num=int(input("enter a number :"))
#for i in range(1,11):
    #print(num,"*",i,"=",num*i)

#wap to take vowels characters 
#vowels="aeiou"
#for i in vowels:
    #print(i)

#nested statements
#x=int(input("enter number:"))
#y=int(input("enter  a number:"))
#if x>2:
    #if y>2:
     #z=x+y
    #print("z is",z)
#else:
 #print("x is",x)

#nested loops
#height=int(input("enter a height:"))
#for row in range(1,height):
    #for col in range(1,height):
        #print(col, end=" ")
    #print()

#for i in range(2,11):
    #for j in range(1,11):
       # print(i,"*",j,"=",i*j)
#print()
#for i in range(1,6):
    #for j in range(1,i+1):
       # print(j,end=" ")   
    #print()

#wap to print pyramid shapes
#for i in range(6,0,-1):
    #for j in range(i):
       # print("*",end=" ")
    #print()

#def full_pyramid(n):
    #for i in range(1, n + 1):
        #for j in range(n - i):
           # print(" ", end="")
            #for k in range(1, 2*i):
               # print("*", end="")
           # print()
full_pyramid(5)


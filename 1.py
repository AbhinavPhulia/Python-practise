# practise questions after attending ython kss-1 and kss-2:


# #question-1
m=int(input("enter the value of m:"))
n=int(input("enter the value of n-:"))
for i in range (m,n):
    print(f"the nos between m and n are-:",{i})

# #question-2
x=int(input("enter the value of x-:"))
y=int(input("enter the value of y-:"))
if(x%y==0):
    print("x perfectly divisible by y")

#question-3
import math
d=int(input("enter the value for diameter-:"))   
r=d/2 
area_of_circle=3.14*r*r
perimeter_of_circle=2*3.14*r
print("area of circle-:",area_of_circle)
print("perimeter of circle-:",perimeter_of_circle)
    
#question-4
n=int(input("enter the value of n-:"))
fact=1
if n<0:
    print("factorial does not exist")
elif n==0:
 print("factorial",0)
else:
  for i in range(1,n+1):
        fact=fact*i
        print("factorial of n is-:",fact)


#question-5
for i in range(1,7):
    for j in range(1,i):
        print(j, end="")
    print()
    

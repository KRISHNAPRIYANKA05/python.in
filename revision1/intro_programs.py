"""in this session we will be practice the programs based on the introduction part
 that we have discussed. """

# printing the details
name = input("enter the name:")
age = int(input("enter the age:"))
college = input("enter the college name")
print(name,age,college)

# adding the numbers
k =int(input("enter the numbers 1:"))
l = int(input("enter the nhumber 2:"))
add = k+l
print(add)

# number swap
a = int(input("enter a:"))
b = int(input("enter b:"))
a,b=b,a
print(a,b)

# number swap by temp
f = int(input())
o = int(input())
temp = f
f=o
o=temp
print(f,o)

# fareniheit to celsius
c = int(input("enter the temperature:")) 
f= ((9/5)+c)
print(f)

#area of rectangle
l= int(input("enter the lenght:"))
b = int(input("enter the bredth:"))
a = 2*(l+b)
print("area of triangle:",a)

# simple interest
p = int(input("enter the principle:"))
t = int(input("enter the time :"))
r = int(input("enter the rate:"))
i = (p*t*r)/100
print("the simppl interst is:",i)

# total and average
t1 = int(input())
t2 = int(input())
t3 = int(input())
t4 = int(input())
t5 = int(input())
add =t2+t2+t3+t4+t5
average = (add)/5
print(add)
print(average)

# bill spilter
bill = int(input("enter the bill amount"))
spllit =int(input("enter the numbers"))
total_bill=bill/spllit
print(total_bill)

# salary calculator
#salary =hra+da+salary
salary=int(input("enter the salaray"))
hra = (salary/100)
da = (salary/10)
tatal_salary = salary+hra+da
print("the toatal salary is",tatal_salary)

#digit extraction
digit = int(input("enter the number"))
first = digit//100
second = (digit)//10
third = digit%10
print(first,second,third)

#minutes to hours
minutes = int(input("enter the minutes: "))
hours = round(minutes/60)
remaining_minutes = (minutes)%60
seconds = hours *60
print(hours ,'and', remaining_minutes)

# years and months 
days = int(input("enter the days:"))
year =days/365
months = days//12
print(year,months)
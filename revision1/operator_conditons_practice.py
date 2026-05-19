"""programs based on  operation and conditional statements that awe havw discussed before

# odd or even 
a = int(input("enter the nmber:"))
if a%2==0:
    print("even")
else:
    print("odd")

# positive,negative or zero
b= int(input("enter the number:"))
if b>0:
    print("positive")
elif b<0:
    print("negative")  
else:
    print("zero") 

#largest of 2 numbers:
c = int(input("enter the value:"))
d = int(input("enter the value:")) 
if c>d:
    print("c is larger")
else:
    print("d is larger") 

#voting elegibility
age= int(input("enter the age:"))
if age>=18:
    print("eleigible:")
else:
    print("not elegible")

# divisibe ny 5
t = int(input("enter the number:"))
if t%5==0:
    print("divisible by 5")
else:
    print("not divisible by 5")

# largest of 3 numbers
o =int(input("enter the number1:"))
p=int(input("entr the 2number:"))
q = int(input("enter the 3rd number:"))
if o>p and o>q:
    print("o")
elif p>o and p>q:
    print("p")
else:
    print("q")"""


#leap year
year=int(input("enter the year:"))
if year%4==0 or year%100==0 and year%400!=0:
    print("leap year")
else:
    print("not leap year")     

#simple calculator
w= int(input("enter the number:"))
x= int(input("enter th number:"))
add=(w+x)
sub= (w-x)
multi =(w*x)
div = (w/x)
print(add,sub,multi,div)



"""
# "login system"
user_name = "admin"
password = 123456789
login_name = input("enter the logon details:")
password_now = int(input("enter the password:"))
if user_name==login_name and password==password_now:
    print("login successful")
else:
    print("enter correct details")    

# ATM withdrwawal:
account_balance = 35000
balance = int(input("enter the amount:"))
if balance <= account_balance:
    print("enter the amount for withdrawalamount")
else:
    print("amount not sufficient")    

# find smallest number
a= int(input("enter the number:"))
b = int(input("enter the number:"))
c= int(input("enter the number:"))
if a<c and a<b:
    print("a")
elif b<c and b<a :
    print(b) 
else:
    print(c)   

# electricity bill
unit = int(input("enter no.of units consumed:"))
if unit<=100:
    print(unit*5)
else:
    print(unit*8)    

# bonus salary
experience = int(input("enter the experience of the  candidate:"))
salary = int(input("enter the salary of the employee:"))
if experience>=5:
    bonus = salary*0.2
    total_salary=(salary+bonus)
    print(total_salary)
else:
    print("no bonus")    """

# number type checker
number = int(input("enter the number:"))
if number>0 and number%2==0:
    print("number is positive even")
elif number>0 and number%2!=0:
    print("number is  positive odd")
elif number<0 and number%2==0:
    print("negative even")
elif number<0 and number%2!=0:
    print("negative odd")
else:    
    print("neither negative nor positive")
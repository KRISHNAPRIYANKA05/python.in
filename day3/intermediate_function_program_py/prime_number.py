""" in this program er are going to write
the code for  finding  whether the given nuber is prime number 
or not in both local and global variables."""

#global variable
number = int(input("enter the number:"))
 #defning the function 
def is_prime(number):
    if number <=1:
        print("not prime")
    else:
        for i in range(2, number):
            if number % i == 0:
                print("not prime")
                return
        print("prime")
        #calling the function
        # 
is_prime(number)
                 
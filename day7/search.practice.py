"""to find the missing number and print them.
l = list(map(int,input("enter the elements:").split()))
missing=()
for i in (0,len(l)):
    if i not in l:
        missing+=1
        
    else:
        print("no number")
# print(missing)    
# create a  matrix
matrix=[]
rows =int(input("enter the no.of rows:"))
columns = int(input("enter the no.of columns:"))
for i in range(rows):
    l = list(map(int,input("rows").split()))
    matrix.append(l)
print(matrix)
target =int(input("enter the target"))
for row in matrix:
    for values in row:
        if values==target:
            print("found")
        else:
            print("not found")    
            
# leaders in array
def findLeaders(arr):
    n = len(arr)
    leaders = []
    max_from_right = float('-inf')

    # Traverse from right to left    
    for i in range(n - 1, -1, -1):
        if arr[i] >= max_from_right:
            leaders.append(arr[i])
            max_from_right = arr[i]
            
    # Reverse to return the leaders in original left-to-right order
    return leaders[::-1]
"""
# to find the day of highest stock that can be selled out 
a=list(map(int,input("enter the stock price:").split()))
max_profit=float("-inf")
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[j]-a[i]>max_profit:
            max_profit=a[j]-a[i]
print(max_profit)            
            















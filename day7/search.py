"""searching techniques:
linera search: searchin a  arranged order
binary search:searching in two possible ways mostly in arranged order
some times in jumbled order.

# finding the element in linear way and non linear
h = list(map(int,input("enter the elements in the list:").split()))
target = int(input())
for i in h:
    if i==target:
        print("found")
        break
    else:
        print("target not found")
        
# without linera search
h = list(map(int,input("enter the elements in the list:").split()))
target = int(input())

if target in h:
        print("found")
        
else:
        print("target not found")
        
# user input to findthe target  index without linear sesarcg
s= list(map(int,input("enter the elements:").split()))
target =int(input())
for i in s:
    if i==target:
        print(s.index(target))
    else:
        print("not found")    
       
        
# another form of solveing with linear search
k= list(map(int,input("enter the elements:").split()))
target =int(input())
for i in range(len(k)):
    if k[i]==target:
        print(i)
        break
        
        
# frequency of the number
a=[1,2,6,2,3,2,2]
target =2
print(a.count(target))


s = list(map(int,input("enter:").split()))
k = int(input())
count=0
for i in s:
    if i==k:
        count+=1
print(count)        

# find the first and last occurence of the value
s = list(map(int,input("enter:").split()))
target = int(input())
last =-1
for i in range(len(s)):
    if s[i]==target:
        last=i
print(last)        

# find out the duplicate of the numbers in the given list 
my_list = [1, 2, 3, 2, 4, 5, 1, 6, 4]

seen = set()
duplicates = set()

for x in my_list:
    if x in seen:
        duplicates.add(x)
    else:
        seen.add(x)

print(f"Duplicate values: {list(duplicates)}")   

"""
a = list(map(int,input("enter:").split()))
dup=[]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j] and a[i] not in dup:
            dup.append(a[i])
print(dup)            
"""numbers = input("Enter the numbers: ").split()
a = set(map(int, numbers))

for i in a:
    print(i)

a.add(4)
print(a)

a = set(input("enter the set vallues:").split())
k =(input())
a.pop()
print(a)
a.discard(k)
print(a)

s = set(input().split())
print(max(s))
print(min(s))
"""
"""s = set(input("enter the elements:").split())
t = set (input("enter the 2ns set :").split())
u= set(input("enter the 3rd set:").split())
if s==t==u:
    print("true")
else:
    print("false")    
    """
    
"""s = set(input("enter the elements:").split())
t = set (input("enter the 2ns set :").split())
u= set(input("enter the 3rd set:").split())
print(s.isdisjoint(t))    
print(t.issubset(u))
print(u.issubset(s))"""

"""k = set(input("enter the 1st set:").split())
l = set(input("enter the 2nd set:").split())
print(k^l)"""



"""l = set(input("enter the 2nd set:").split())
print(l.clear())"""

"""l = set(input("enter the elements set:").split())
print(l.copy())"""

"""target = int(input("Enter the target sum: "))
k = set(map(int, input("enter the elements: ").split()))
pairs = []
for i in k:
    if (i + 1) in k and i + (i + 1) == target:
        pairs.append({i, i + 1})
if pairs:
    for pair in pairs:
        print(pair)
else:
    print("No consecutive pair sums to the target")'''"""

"""numbers = set(map(int, input("enter the elements:").split()))
target = int(input("Enter the target sum: "))

for i in numbers:
    for j in numbers:
        if i + j == target:
            print((i, j))"""

'''s = set(map(int, input("enter the elements:").split()))
for x in s:
    if s.count(x) ==1:
        print(x)
        break'''

"""s = list(map(int,input("enter the elements:").split()))
i = 0
for i in s:
    if i ==0:
        s.remove(i)
        s.append(i)
print(s)"""
 


"""s = list(map(int,input("enter the elements :").split()))
for i in s:
    for j in s:
        if count(i)>1 :
             
            print(i)"""

l= list(map(int,input("enter the elements in the list ").split()))
ans = []
for i in range(len(l)):
    p=1
    for j in range(len(  l)):
        if  i!=j:
            p*=l[i]
    ans.append(p)
print(ans)            


        
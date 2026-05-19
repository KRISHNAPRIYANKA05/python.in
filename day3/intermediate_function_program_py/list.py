l = list(map(int, input("enter the elements in the list ").split()))
ans = []
for i in range(len(l)):
    p = 1
    for j in range(len(l)):
        if i != j:
            p *= l[j]
    ans.append(p)
print(ans)     
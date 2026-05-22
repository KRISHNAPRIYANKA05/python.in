"""binary search :in binary search ,we dont check every possible way of 
solving the problem we consider the nearest solurion that gives 2 with floor division 
is 2."""
# binary search example in midvalue
def binary(arr,k):
    l,r=0,len(arr)-1
    ans=-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid]==k:
            ans=mid-1
            return mid
        elif arr[mid]<k:
            l=mid+1
        elif arr[mid]>k:
            r=mid-1
    return ans
ls=list(map(int,input("enter:").split())) 
key =int(input("enter the key to find:"))
res=print(binary(ls,key))

      
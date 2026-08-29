n=int(input("enter n"))
a=[]
for _ in range(n):
    a.append(int(input("enter a integer: ")))
def search(array,o):
    low,high=0,(len(array))
    while low<high:
        mid=(low+high)//2
        if array[mid]== o:
            return mid
        elif array[mid]< o:
            low=mid+1
        elif array[mid]> o:
            high=mid-1
    return low;
           
def hash1(x):
    sublist=[[] for i in range(10)]
    for j in x:
        r= j%10
        x=search(sublist[r],j)
        sublist[r].insert(x,j)
    return sublist
table = hash1(a)
for i in range(10):
    print(f"Sublist {i}: {table[i]}")
    
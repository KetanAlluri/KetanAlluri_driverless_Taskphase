import bisect
n=int(input("enter n"))
a=[]
for _ in range(n):
    a.append(int(input("enter a integer: ")))
a=list(set(a))
a=list(set(a))
def hash1(x):
    sublist=[[] for i in range(10)]
    for j in x:
        r= j%10
        l=bisect.bisect(sublist[r],j)
        sublist[r].insert(l,j)
    return sublist
table = hash1(a)
for i in range(10):
    print(f"Sublist {i}: {table[i]}")

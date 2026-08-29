n=int(input("enter n"))
a=[]
for _ in range(n):
    a.append(int(input("enter a integer: ")))
def hash1(x):
    sublist=[[] for i in range(10)]
    for j in x:
        r= j%10
        sublist[r].append(j)
    return sublist
table = hash1(a)
for i in range(10):
    print(f"Sublist {i}: {table[i]}")
    
  
    

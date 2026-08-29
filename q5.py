n=int(input("enter n"))
a=[]
for _ in range(n):
    a.append(int(input("enter a integer: ")))
def hash1(x):
    sublist=[[] for i in range(10)]
    for j in x:
        r= j%10
        sublist[r].append(r)
    return sublist
print(hash1(a))
    
  
    

import math
def sort(x,y):
    a=[(0,1),(0,3),(1,2)]
    return sorted(a,key= lambda p: math.sqrt((x-p[0])**2+(y-p[1])**2))    
x=int(input("enter x coordinate:"))
y=int(input("enter y coordinate:"))
z= sort(x,y)
print(z)

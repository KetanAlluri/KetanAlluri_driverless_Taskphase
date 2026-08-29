import math
def sort(x,y):
    a = [(0,1),(0,3),(1,2)]
    dist_list=[]
    for z, b in a:
        distance =math.sqrt((x-z)*(x-z) + (y-b)*(y-b))
        dist_list.append(distance)
    if dist_list[1]<dist_list[0] and dist_list[1]<dist_list[2]:
        a[0], a[1] = a[1], a[0]
        if dist_list[2]<dist_list[0]:
            a[0], a[2] = a[2], a[0]
    elif dist_list[2]<dist_list[0] and dist_list[2]<dist_list[1]:
        a[0], a[2] = a[2], a[0]
        if dist_list[1]<dist_list[0]:
            a[0], a[1] = a[1], a[0]
    return a
        
    

x=int(input("Enter the x coordinate: "))
y=int(input("Enter the y coordinate: "))
z=sort(x,y)
print(z)
        
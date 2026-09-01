class search:
    def Q2( self, Q1):
        n = len(Q1)
        for i in range(n - 1):
            min = i
            for j in range(i + 1, n):
                if Q1[j] < Q1[min]:
                    min = j
            Q1[i], Q1[min] = Q1[min], Q1[i]
        return Q1      

    def search(self, x, target):
        low,high=0,len(x)-1
        while low<=high:
            mid=(low+high)//2
            if x[mid]==target:
                return mid
            elif x[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return -1
Q1=["Q1", "Delta", "Alpha", "Omega", "Beta"]
t=input("Enter the target to search: ")
a=search().Q2(Q1)
b=search().search(a, t)
if b != -1:
    print("Target found")
else:
    print("Target not found.")
     

        

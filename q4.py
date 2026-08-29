def matrix_multiply(A, B):
   x=len(A)
   y=len(B[0])
   z=len(A[0])
   v=len(B)
   if (z!=v):
       print("Matrix multiplication not possible")
       return None
   C = [[0 for _ in range(y)] for _ in range(x)]
   for i in range(x):
       for j in range(y):
           for k in range(v):
               C[i][j] += A[i][k] * B[k][j]
   return C
A= [[1, 2], [3, 4], [5, 6]]
B= [[1, 2], [3, 4]]
C=matrix_multiply(A, B)
print ("Result of matrix multiplication:"+ str(C))
r1 = int(input("Enter the number of rows of matrix 1:"))
c1 = int(input("Enter the number of columns of matrix 1:"))
r2 = int(input("Enter the number of rows of matrix 2:"))
c2 = int(input("Enter the number of columns of matrix 2:"))
matrix1 = []
matrix2 = []
multiplied_matrix=[]
print("give rowwise entry to matirx1:")
for i in range(r1):         
    row_array =[]
    for j in range(c1):  
         row_array.append(int(input()))
    matrix1.append(row_array)
print("give rowwise entry to matirx2:")    
for i in range(r2):         
    row_array1=[]
    for j in range(c2): 
        row_array1.append(int(input()))
    matrix2.append(row_array1)
print("matrix1:")    
for i in range(r1):
    for j in range(c1):
        print(matrix1[i][j], end = " ")
    print("")
print("matrix2:")    
for i in range(r2):
    for j in range(c2):
        print(matrix2[i][j], end = " ")
    print("")
if c1!=r2 :
    print("matrix multiplication is not possible")
else:
   
   for i in range(r1):
      row=[]
      for j in range(c2):
         row.append(0)
      multiplied_matrix.append(row)
   
   for i in range(r1):
    for j in range(c2):
      for k in range(r2):
            multiplied_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
 
for r in multiplied_matrix:
     print(r)
    
    

    
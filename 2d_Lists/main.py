matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0][1])

for i in range(0,3,1):
    for j in range(0,3,1):
        print(matrix[i][j])
    print("\n") 

for row in matrix:
    for item in row:
        print(item)
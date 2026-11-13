import random

board=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for rows in board:
    print(rows)

for i in range(0,9,1):
    row_num=int(input("Enter the row number: "))
    index_num=int(input("Enter the index number: "))
    board[row_num][index_num]='X'

    row=random.randrange(len(board))
    index=random.randrange(len(board[row]))

    board[row][index]='O'

    for rows in board:
        print(rows)

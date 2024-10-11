def valid_sudoku(board):

    # ROWS
    for i in range(9):
        result = set()
        for j in range(9):
            item = board[i][j]
            if item in result:
                return False
            elif item != '.':
                result.add(item)
    
    # COLUMNS
    for i in range(9):
        result = set()
        for j in range(9):
            item = board[j][i]
            if item in result:
                return False
            elif item != '.':
                result.add(item)

    # SUB BOXES
    starts = [(0,0) , (0,3) ,(0,6),
              (3,0) , (3,3) ,(3,6),
              (6,0) , (6,3) ,(6,6),
                ]
    for i , j in starts:
        result = set()
        for rows in range(i , i+3):
            for cols in range(j , j+3):
                item = board[rows][cols]
                if item in result:
                    return False
                elif item != '.':
                    result.add(item)

    return True
    



    
board = [
    ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
    ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
    ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
    ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
    ['4', '.', '3', '.', '.', '8', '.', '4', '5'],
    ['7', '.', '.', '2', '.', '1', '7', '.', '6'],
    ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
    ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
    ['.', '.', '.', '.', '8', '.', '.', '7', '9']
]

print(valid_sudoku(board))
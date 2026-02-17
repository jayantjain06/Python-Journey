def isValidSudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):
            value=board[r][c]
            box_index=(r//3)*3+(c//3)
            if value == ".":
                continue
            if value in rows[r] or value in cols[c] or value in boxes[box_index]:
                return False
            rows[r].add(value)
            cols[c].add(value)
            boxes[box_index].add(value)
    return True        
    
print(isValidSudoku(board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
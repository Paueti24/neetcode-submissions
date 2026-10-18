class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows and columns
        for i in range(9):
            seenRows = [False] * 11 # 1-indexed
            seenCols = [False] * 11 # 1-indexed
            for j in range(9):
                x, y = board[i][j], board[j][i]

                if x.isdigit():
                    x = int(x)
                    if seenRows[x]:
                        #print(f"Repetition in row {i} ({j}), num: {x}")
                        return False
                    seenRows[x] = True
                
                if y.isdigit():
                    y = int(y)
                    if seenCols[y]:
                        #print(f"Repetition in col {j}")
                        return False
                    seenCols[y] = True
        
        # Check 3x3 sub-boxes
        for x in [1,4,7]:
            for y in [1,4,7]:
                seen = [False] * 11 # 1-indexed
                for xi in [-1,0,1]:
                    for yi in [-1,0,1]:
                        num = board[y+yi][x+xi]
                        if num.isdigit():
                            num = int(num)
                            if seen[num]:
                                #print(f"Repetition in box {x}-{y}")
                                return False
                            seen[num] = True
        
        # All checked
        return True


                
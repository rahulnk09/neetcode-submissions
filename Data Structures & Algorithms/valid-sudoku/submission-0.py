class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        box=[[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                val=board[i][j]
                if val=='.':
                    continue

                if val in rows[i]:
                    return False
                else:
                    rows[i].add(val)
                
                if val in cols[j]:
                    return False
                else:
                    cols[j].add(val)
                
                if val in box[(i//3)][(j//3)]:
                    return False
                else:
                    box[(i//3)][(j//3)].add(val)
    
        return True
                    
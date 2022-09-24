class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        sub_box = defaultdict(set)
        

        
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c == '.':
                    continue
                if c in row[i] or c in col[j] or c in sub_box[(i // 3, j // 3)]:
                    return False
                else:
                    row[i].add(c)
                    col[j].add(c)
                    sub_box[(i//3, j//3)].add(c)
        
        return True
                    
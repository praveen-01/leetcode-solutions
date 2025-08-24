class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = defaultdict(list)
        c = defaultdict(list)
        box = defaultdict(list)
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num==".": continue
                if num in r[i] or num in c[j] or num in box[(i//3,j//3)]:
                    return False
                r[i].append(num)
                c[j].append(num)
                box[(i//3,j//3)].append(num)
        return True
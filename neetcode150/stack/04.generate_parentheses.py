class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(opb,closb,st):
            if opb==closb and opb+closb==2*n:
                res.append(st)
                return
            if opb<n:
                dfs(opb+1,closb,st+"(")
            if closb<opb:
                dfs(opb,closb+1,st+")")
        dfs(0,0,"")
        return res

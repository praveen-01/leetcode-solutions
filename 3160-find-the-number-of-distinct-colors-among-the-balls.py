#could only solve after looking at hint
#link: https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        vis={}
        colored={}
        res=[]
        for query in queries:
            ball,color = query
            if ball not in vis:
                vis[ball]=color
                if color in colored:
                    colored[color]+=1
                else:
                    colored[color]=1
            else:
                temp=vis[ball]
                if temp in colored:
                    colored[temp]-=1
                    if colored[temp]==0:
                        del colored[temp]
                vis[ball]=color
                if color in colored:
                    colored[color]+=1
                else:
                    colored[color]=1
            res.append(len(colored))

        return res

        

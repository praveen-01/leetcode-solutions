'''
idea is to do bfs with both chances for all the nodes where water is present
similar to island to problem?
'''
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def bfs(x,y):
            vis[x][y]=True
            max_sum=0
            trav=[(x,y)]
            while trav:
                idx,idy=trav.pop(0)
                max_sum+=grid[idx][idy]
                for nx,ny in [(-1,0),(1,0),(0,1),(0,-1)]:
                    ndx,ndy = idx+nx,idy+ny
                    if ndx>=0 and ndx<n and ndy>=0 and ndy<m and vis[ndx][ndy]==False and grid[ndx][ndy]>0:
                        trav.append((ndx,ndy))
                        vis[ndx][ndy]=True
            return max_sum
            
        n=len(grid)
        m=len(grid[0])
        vis=[[False for _ in range(m)] for j in range(n)]
        ans=0
        for i in range(n):
            for j in range(m):
                if vis[i][j]==False and grid[i][j]>0:
                    max_sum=bfs(i,j)
                    ans=max(ans,max_sum)
        return ans


        

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        rank = [0]*(n+1)
        parent = [i for i in range(n+1)]
        def find(node):
            if node!=parent[node]:
                parent[node]=find(parent[node])
            return parent[node]
        def union(p1,p2):
            u1,u2 = find(p1),find(p2)
            if u1==u2:
                return False
            else:
                if rank[u1]>rank[u2]:
                    parent[u2]=u1
                    rank[u1]+=rank[u2]
                else:
                    parent[u1]=u2
                    rank[u2]+=rank[u1]
                return True
        for edge in edges:
            if not union(edge[0],edge[1]):
                return edge
        

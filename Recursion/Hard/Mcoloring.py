class Solution:
    def check(self, i, node, clr, adj):
        for nei in adj[node]:
            if clr[nei] == i:
                return False 
        return True 
            
    def possible(self, node, m, n, clr, adj):
        if node == n:
            return True 
        for i in range(1, m + 1):
            if self.check(i, node, clr, adj):
                clr[node] = i
                if self.possible(node + 1, m, n, clr, adj):
                    return True 
                clr[node] = 0
        return False
        
    def graphcolour(self, edges, m, n):
        adj = [ [] for _ in range(n) ]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        clr = [0] * n
        return self.possible(0, m, n, clr, adj)
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [i for i in range(n + 1)]

        def find(i):
            if par[i] == i:
                return i
            par[i] = find(par[i])
            return par[i]

        def union(i, j):
            root_i = find(i)
            root_j = find(j)

            if root_i == root_j:
                return False

            par[root_i] = root_j
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]
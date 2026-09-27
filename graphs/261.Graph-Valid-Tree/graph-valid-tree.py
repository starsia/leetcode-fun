class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # a valid tree is a graph without cycle, and should be fully connected
        # kahn's algo is useful here, it relies on an indegree list, however it is undirected
        if not n:
            return True

        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        print(adj)
        visited = set()
        def dfs(i, prev): 
            if i in visited:
                return False
            visited.add(i)

            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False # loop detected

            return True

        return dfs(0, -1) and n == len(visited)


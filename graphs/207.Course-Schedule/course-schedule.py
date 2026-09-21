class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        visited = set()

        # create adjacency list
        for item in prerequisites:
            course = item[0]
            prereq = item[1]
            # prereq -> course

            adj[prereq].append(course)
        
        in_degrees= [0] * numCourses
        # create in-degree list

        for i in range(numCourses):
            for item in adj[i]:
                in_degrees[item] += 1

        # populate queue
        queue = collections.deque()
        for i in range(numCourses):
            if in_degrees[i] == 0:
                queue.append(i)

        
        # kahn's algorithm
        while queue:
            temp = queue.popleft()
            visited.add(temp)

            for item in adj[temp]:
                # decrement indegree of all neighbours
                in_degrees[item] -=1

                if in_degrees[item] == 0 :
                    queue.append(item)

        return len(visited) == numCourses



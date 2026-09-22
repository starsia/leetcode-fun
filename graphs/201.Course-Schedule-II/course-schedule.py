    # create adjacency list
    for prerequisite in prerequisites:
        course = prerequisite[0]
        prereq = prerequisite[1]
        
        # contains neighbours pointing to
        adjacency[prereq].append(course)
    
    print(adjacency)
    # create in-degrees list
    indegrees = [0] * n
    
    for i in range(n):
        for node in adjacency[i]:
            indegrees[node] += 1
        
    print(indegrees)
    
    # kahn's algo
    queue = collections.deque()
    for i in range(n):
        if indegrees[i] == 0:
            queue.append(i)
        
    while queue:
        temp = queue.popleft()
        visited.append(temp)
        
        for neighbour in adjacency[temp]:
            indegrees[neighbour] -= 1
            if indegrees[neighbour] == 0:
                queue.append(neighbour)
        
        
        
    if len(visited) == n:
        return visited 
    else: 
        return []

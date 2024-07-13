import queue

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node):
        if not node:
            return

        # Keep track of cloned vertices
        visited = {node:Node(node.val)}

        # Queue to perform BFS
        q = queue.Queue()
        q.put(node)

        while not q.empty():
            u = q.get()

            for v in u.neighbors:
                # If the neighbour does not yet have a clone, we make a clone for it
                if v not in visited:
                    visited[v] = Node(v.val)
                    # Then, we put the neighbour in the queue to visit it later
                    q.put(v)
                # We append the clone of the current vertice to include the clone of the neighbour
                visited[u].neighbors.append(visited[v])

        # Return the clone of the first node
        return visited[node]


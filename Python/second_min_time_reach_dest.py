import queue
from typing import List


class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj_list = [[] for _ in range(n)]
        # We essentially convert the vertices to 0-based indexing
        for v, u in edges:
            adj_list[v - 1].append(u - 1)
            adj_list[u - 1].append(v - 1)

        # Perform BFS to find edges that are in the shortest path from node 0 to n - 1
        q = queue.Queue()
        q.put((0, 0))
        # We can conservatively keep track of the top 2 timings that get to the node
        shortest_times = [[float('inf'), float('inf')] for _ in range(n)]
        # Set shortest time to the first node as 0, since we start from there
        shortest_times[0][0] = 0

        while not q.empty():
            node, time_elapsed = q.get()

            # Check if the signals are currently red
            next_time = time_elapsed
            if (time_elapsed // change) % 2:
                next_time = (time_elapsed // change + 1) * change
            next_time += time

            for neighbour in adj_list[node]:
                # If this traversal is the new shortest path to this relevant node, we set it as the shortest
                # We move the current shortest time as the 2nd shortest
                curr_shortest = shortest_times[neighbour][0]
                if next_time < curr_shortest:
                    shortest_times[neighbour][1] = curr_shortest
                    shortest_times[neighbour][0] = next_time
                    q.put((neighbour, next_time))
                elif curr_shortest < next_time < shortest_times[neighbour][1]:
                    shortest_times[neighbour][1] = next_time
                    q.put((neighbour, next_time))

        # Finally, return the second shortest time to reach the n - 1 node
        return shortest_times[n - 1][1]

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for u, v, time in roads:
            adj_list[u].append((v, time))
            adj_list[v].append((u, time))

        dist = [float('inf')] * n
        dist[0] = 0
        path_count = [0] * n
        path_count[0] = 1

        pq = []
        heappush(pq, (0, 0))  # (time, next_node)
        while pq:
            time, node = heappop(pq)
            if time > dist[node]:
                continue
            for next_node, travel in adj_list[node]:
                new_time = time + travel
                if new_time < dist[next_node]:
                    dist[next_node] = new_time
                    path_count[next_node] = path_count[node]
                    heappush(pq, (new_time, next_node))
                elif new_time == dist[next_node]:
                    path_count[next_node] = (path_count[next_node] + path_count[node]) % (10 ** 9 + 7)
        return path_count[n - 1]

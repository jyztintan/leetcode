class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for u, v, w in times:
            adj_list[u].append((v, w))
        visited = set()
        pq = [(0, k)]
        latest = 0
        while pq:
            time, node = heappop(pq)
            if node in visited:
                continue
            visited.add(node)
            latest = time
            for v, w in adj_list[node]:
                if v not in visited:
                    heappush(pq, (time + w, v))
        if len(visited) != n:
            return -1
        return latest

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = defaultdict(list)
        for fro, to, price in flights:
            adj_list[fro].append((to, price))

        min_heap = []  # step, price, destination
        heappush(min_heap, (0, 0, src))
        visited = {}

        while min_heap:
            price, step, curr = heappop(min_heap)
            if curr == dst:
                return price
            if curr in visited and visited[curr] <= step:
                continue
            visited[curr] = step
            if step == k + 1:
                continue
            for nxt, nxt_price in adj_list[curr]:
                heappush(min_heap, (price + nxt_price, step + 1, nxt))

        return -1

class Solution:
    def maximumInvitations(self, favourite: List[int]) -> int:
        n = len(favourite)

        in_degree = [0] * n
        for person in favourite:
            in_degree[person] += 1

        q = deque()
        for idx in range(n):
            if in_degree[idx] == 0:
                q.append(idx)

        # How many people you can reach starting from respective index
        reach = [1] * n

        while q:
            curr = q.popleft()
            person = favourite[curr]
            reach[person] = max(reach[person], reach[curr] + 1)
            in_degree[person] -= 1
            if in_degree[person] == 0:
                q.append(person)

        # Handle cycles and pairs
        largest_cycle = 0
        pairs = 0
        for person in range(n):
            if in_degree == 0:
                continue

            cycle = 0
            curr = person
            while in_degree[curr] != 0:
                in_degree[curr] = 0
                cycle += 1
                curr = favourite[curr]

            if cycle == 2:
                pairs += reach[person] + reach[favourite[person]]
            else:
                largest_cycle = max(largest_cycle, cycle)

        return max(largest_cycle, pairs)

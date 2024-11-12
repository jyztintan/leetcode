import heapq


class Solution:
    def maximumBeauty(self, items, queries):
        queries = [(query, i) for i, query in enumerate(queries)]

        # Sort items and queries by increasing price
        queries.sort()
        items.sort()
        ptr = 0
        n = len(items)

        # Keep track of items beauty in a max heap
        max_heap_beauty = []

        # keep track of answer to possible queries
        answers = []

        for query, i in queries:
            while ptr < n and items[ptr][0] <= query:
                heapq.heappush(max_heap_beauty, -items[ptr][1])
                ptr += 1
            if not max_heap_beauty:
                answers.append((0, i))
            else:
                # Get the max beauty given the current cost
                answers.append((-max_heap_beauty[0], i))

        answers.sort(key=lambda x:x[1])
        answers = list(map(lambda x:x[0], answers))
        return answers

# items = [[1,2],[3,2],[2,4],[5,6],[3,5]]
# queries = [1,2,3,4,5,6]
# print(Solution().maximumBeauty(items, queries))

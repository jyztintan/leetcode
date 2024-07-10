import heapq
class Solution:
    def lastStoneWeight(self, stones) -> int:

        # We want to use a max heap as we want to easily access the heaviest stones
        max_heap = []
        heapq.heapify(max_heap)

        for stone in stones:

            # Negate the weights for max heap
            heapq.heappush(max_heap, -stone)

        # While there are at least 2 stones, we smash them together
        while len(max_heap) > 1:
            first, second = heapq.heappop(max_heap), heapq.heappop(max_heap)

            # The second stone is guaranteed to be lighter or equal than the first
            diff = second - first

            # If there is a heavier rock, then we add back whatever is remaining
            if diff:
                heapq.heappush(max_heap, - diff)

        # There is a possibility of no rocks left. If so, we output 0.
        if not max_heap:
            return 0
        return - max_heap[0]
import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []

        if a > 0:
            heapq.heappush(max_heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(max_heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(max_heap, (-c, 'c'))

        ans = ''
        while True:

            # If character quota has been met
            if not max_heap:
                return ans

            # Get the highest quota character -> we want to use it more
            count, best = heapq.heappop(max_heap)

            # If the highest quota character has already been added prev 2 times,
            # Return false if there are no other alternatives
            # Else use the 2nd highest quota character
            if ans[-2:] == best * 2:
                if len(max_heap) == 0:
                    return ans
                else:
                    highest_count, highest_best = count, best
                    count, best = heapq.heappop(max_heap)
                    heapq.heappush(max_heap, (highest_count, highest_best))

            ans += best
            count += 1

            # Push back to pq if there is still quota. Note that we reverse < instead of > due to underlying min heap
            if count < 0:
                heapq.heappush(max_heap, (count, best))

print(Solution().longestDiverseString(7,1,0))




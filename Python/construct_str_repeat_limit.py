class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = Counter(s)

        max_heap = []
        for char, count in freq.items():
            heappush(max_heap, ((-ord(char), count)))

        res = ""
        while max_heap:
            char_ord, count = heappop(max_heap)
            char = chr(-char_ord)
            use = min(count, repeatLimit)
            res += char * use

            if count > use and max_heap:
                next_char_ord, next_count = heappop(max_heap)
                res += chr(-next_char_ord)
                if next_count > 1:
                    heappush(max_heap, (next_char_ord, next_count - 1))
                heappush(max_heap, (char_ord, count - use))

        return res

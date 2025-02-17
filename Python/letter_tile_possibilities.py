class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def count_seqs(counter: dict):
            if sum(counter.values()) == 0:
                return 0

            total = 0
            for c in counter:
                if counter[c] > 0:
                    counter[c] -= 1
                    total += count_seqs(counter) + 1
                    counter[c] += 1

            return total

        counter = Counter(tiles)
        ans = count_seqs(counter)
        return int(ans)

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        freq = {}
        count = 0
        for a, b in dominoes:
            if b < a:
                a, b = b, a
            if (a, b) in freq:
                count += freq[(a, b)]
            freq[(a, b)] = freq.get((a, b), 0) + 1
        return count

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x:x[1])
        curr = - float('inf')
        count = 0
        for start, end in pairs:
            if curr < start:
                count += 1
                curr = end
        return count

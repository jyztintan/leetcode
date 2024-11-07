class Solution:
    def largestCombination(self, candidates) -> int:
        count = [0] * 24

        for num in candidates:
            binary = bin(num)[2:][::-1]
            for i, bit in enumerate(binary):
                if bit == '1':
                    count[i] += 1

        return max(count)


candidates = [16,17,71,62,12,24,14]
print(Solution().largestCombination(candidates))



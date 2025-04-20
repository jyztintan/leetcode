class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq = {}
        for answer in answers:
            freq[answer] = freq.get(answer, 0) + 1

        count = 0
        for num in freq:
            count += ceil(freq[num] / (num + 1)) * (num + 1)
        return count

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        low, high = 1, n - 1
        while '0' in str(low) + str(high):
            low += 1
            high -= 1
        return [low, high]

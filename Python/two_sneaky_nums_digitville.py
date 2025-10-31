class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = set()
        sneaky = []
        for num in nums:
            if num in seen:
                sneaky.append(num)
            seen.add(num)
        return sneaky

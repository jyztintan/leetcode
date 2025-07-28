# O(N) time, O(1) space
# Essentially, there can only be up to 2 results. Using Boyer-Moore, we can find the 2 possible candidates,
# and from there count them to verify if they are indeed majority. All operations take O(N) time.
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1 = [None, 0]
        candidate2 = [None, 0]
        for num in nums:
            if candidate1[0] == num:
                candidate1[1] += 1
            elif candidate2[0] == num:
                candidate2[1] += 1
            elif candidate1[1] == 0:
                candidate1 = [num, 1]
            elif candidate2[1] == 0:
                candidate2 = [num, 1]
            else:
                candidate1[1] -= 1
                candidate2[1] -= 1

        res = []
        if nums.count(candidate1[0]) > len(nums) // 3:
            res.append(candidate1[0])
        if nums.count(candidate2[0]) > len(nums) // 3:
            res.append(candidate2[0])
        return res


# O(N) time, O(N) space for frequency counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        majority = set()
        for num in nums:
            if freq[num] > len(nums) // 3:
                majority.add(num)
        return list(majority)

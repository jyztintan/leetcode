class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrack(curr, left):
            if not left:
                ans.append(curr.copy())
                return

            for num in left.copy():
                curr.append(num)
                left.remove(num)
                backtrack(curr, left)
                curr.pop()
                left.add(num)

        ans = []
        backtrack([], set(nums))
        return ans
class Solution:
    def canArrange(self, arr, k: int) -> bool:
        d = {i:0 for i in range(k)}
        for num in arr:
            remainder = num % k
            if d[(k - remainder) % k] > 0:
                d[(k - remainder) % k] -= 1
            else:
                d[remainder] += 1
        for key in d:
            if d[key] > 0:
                return False
        return True

print(Solution().canArrange([1,2,3,4,5,10,6,7,8,9], 5))

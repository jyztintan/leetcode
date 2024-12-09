# O(M + N) Prefix Sum, count number of violations across array and check if there is the same number of violations
# at the start and end of the subarr
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        prefix = [0] * n
        for idx in range(1, n):
            prefix[idx] = prefix[idx - 1]
            if nums[idx] % 2 == nums[idx - 1] % 2:
                prefix[idx] += 1

        response = []
        for start, end in queries:
            if prefix[end] - prefix[start] == 0:
                response.append(True)
            else:
                response.append(False)
        return response

# O(M + NlogN)
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        same_parity = []
        n = len(nums)
        for idx in range(n - 1):
            if nums[idx] % 2 == nums[idx + 1] % 2:
                same_parity.append(idx)

        ptr = 0
        response = {}
        for start, end in sorted(queries):
            while ptr < len(same_parity) and same_parity[ptr] < start:
                ptr += 1

            if ptr == len(same_parity):
                response[(start, end)] = True
                continue

            if start <= same_parity[ptr] < end:
                response[(start, end)] = False
            else:
                response[(start, end)] = True

        return [response[(start, end)] for start, end in queries]

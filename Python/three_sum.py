def threeSum(nums):
    nums.sort()
    res = []
    for i, a in enumerate(nums):
        if i <= 0 or a != nums[i-1]:
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = a + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1]:
                        l += 1
    return res


    # def twoSum(nums, target: int):
    #     ans = []
    #     d = {}
    #     for num in nums:
    #         if num in d:
    #             ans.append([d[num], num])
    #         d[target - num] = num
    #     return ans

    # ans = []
    # for i in range(len(nums)):
    #     res = twoSum(nums[i+1:], -nums[i])
    #     if res != None:
    #         res = list(map(lambda x:[nums[i]] + x, res))
    #         res = list(map(lambda x:sorted(x), res))
    #         for subres in res:
    #             if subres not in ans:
    #                 ans.append(subres)
    # return ans


nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))
    
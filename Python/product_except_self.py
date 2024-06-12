from functools import reduce
def productExceptSelf(nums):
    if nums.count(0) > 1:
        return [0 for i in range(len(nums))]
    elif nums.count(0) == 1:
        ans = list(filter(lambda x:x!=0, nums))
        special = reduce(lambda x,y: x*y, ans, 1)
        return list(map(lambda x:0 if x != 0 else special, nums))
    total = reduce(lambda x,y:x*y, nums, 1)
    return list(map(lambda x:total/x, nums))

# nums1 = [1,2,3,4]
# nums2 = [-1,1,0,-3,3]
# print(productExceptSelf(nums1))
# print(productExceptSelf(nums2))

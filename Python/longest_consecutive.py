def longestConsecutive(nums) -> int:
    max = 0
    if len(nums) == 0:
        return max
    nums = list(set(nums))
    nums.sort()
    print(nums)
    cache = nums[0]
    count = 1
    for num in nums[1:]:
        if num == cache + 1:
            count+=1
        else:
            if count > max:
                max = count
            count = 1
        cache = num
    return count if count > max else max




lst1 = [100,4,200,1,3,2]
lst2 = [0,3,7,2,5,8,4,6,0,1]
lst3 = [9,1,-3,2,4,8,3,-1,6,-2,-4,7]
print(longestConsecutive(lst1))
print(longestConsecutive(lst2))
print(longestConsecutive(lst3))
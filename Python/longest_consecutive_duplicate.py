def longestConsecutive(nums) -> int:
    highest = 0
    nums = set(nums)
    for num in nums:
        if (num - 1) not in nums:
            count = 0
            num_copy = num
            while num_copy in nums:
                count += 1
                num_copy += 1
        highest = max(highest, count)
    return highest



lst1 = [100,4,200,1,3,2]
lst2 = [0,3,7,2,5,8,4,6,0,1]
lst3 = [9,1,-3,2,4,8,3,-1,6,-2,-4,7]
print(longestConsecutive(lst1))
print(longestConsecutive(lst2))
print(longestConsecutive(lst3))
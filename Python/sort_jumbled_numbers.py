class Solution:
    def sortJumbled(self, mapping, nums):
        new = []

        # We use a counter to help us resolve tie-breakers
        # by sorting the numbers by the order they were inputted
        count = 0
        for num in nums:
            count += 1

            # Keep a pristine copy as we want to output in terms of the original numbers
            num_copy = num
            new_num = 0

            # Keep track of digit place
            digit = 1
            if num == 0:
                new_num = mapping[0]
                new.append([new_num, count, num_copy])
                continue

            # Iterate each digit of the number and return the new mapping
            while num:
                new_num += mapping[num % 10] * digit
                num //= 10
                digit *= 10
            new.append([new_num, count, num_copy])
        new.sort()
        return [c for a, b, c in new]

# mapping = [0,1,2,3,4,5,6,7,8,9]
# nums = [9,8,7,6,5,4,3,2,1,0]
# print(Solution().sortJumbled(mapping, nums))
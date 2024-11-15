from typing import List


class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        ptr1, ptr2, ptr3 = 0, 0, 0
        x, y, z = len(arr1), len(arr2), len(arr3)
        ans = []
        while ptr1 < x and ptr2 < y and ptr3 < z:
            num1, num2, num3 = arr1[ptr1], arr2[ptr2], arr3[ptr3]
            if num1 == num2 == num3:
                ans.append(num1)
                ptr1 += 1
                ptr2 += 1
                ptr3 += 1
            else:
                smallest = min(num1, num2, num3)
                if smallest == num1:
                    ptr1 += 1
                if smallest == num2:
                    ptr2 += 1
                if smallest == num3:
                    ptr3 += 1

        return ans

# O(N1 + N2) 2 pointer
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ans = []
        ptr1, ptr2 = 0, 0
        n1, n2 = len(nums1), len(nums2)

        while ptr1 < n1 and ptr2 < n2:
            id1, val1 = nums1[ptr1]
            id2, val2 = nums2[ptr2]

            if id1 == id2:
                ans.append([id1, val1 + val2])
                ptr1 += 1
                ptr2 += 1
            elif id1 < id2:
                ans.append([id1, val1])
                ptr1 += 1
            else:
                ans.append([id2, val2])
                ptr2 += 1

        while ptr1 < n1:
            ans.append(nums1[ptr1])
            ptr1 += 1

        while ptr2 < n2:
            ans.append(nums2[ptr2])
            ptr2 += 1

        return ans

# O((N1 + N2)log(N1 + N2)) due to final sorting
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        id_val = {}
        for id, val in nums1:
            id_val[id] = id_val.get(id, 0) + val
        for id, val in nums2:
            id_val[id] = id_val.get(id, 0) + val
        return sorted(list([id, val] for id, val in id_val.items()))

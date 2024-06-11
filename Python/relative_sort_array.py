'''
This solution uses a hash map for counting and sorting

Time Complexity: O(n + m + k), where k = 1000 in this case
1. Loop through elements of arr1 - O(n)
2. Loop through elements of arr2 - O(m)
3. Counting sort - O(k)

Space Complexity: O(k)
Count array requires a size of k, where k = max(arr1) + 1
'''
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        high = max(arr1) + 1
        buckets = [0] * high
        for ele in arr1:
            buckets[ele] += 1
        res = []
        for ele in arr2:
            for i in range(buckets[ele]):
                res.append(ele)
            buckets[ele] = 0
        for i in range(high):
            while buckets[i] > 0:
                res.append(i)
                buckets[i] -= 1
        return res

'''
This solution uses a hash map for counting and sorting

Time Complexity: O(m + n + m + nlogn + n) = O(m + nlogn)
1. Initialising map with elements from arr2 - O(m)
2. Count occurrences of elements in arr1 - O(n)
3. Loop through elements from arr2 again - O(m)
4. Sort reamining elements in arr1 not in arr2, worst case n elements - O(nlogn)
5. Extending these remaining elements - O(n)

Space Complexity: O(n + m)
1. Map with m elements - O(m)
2. Store elements in arr1 not in arr2, worst case n elements - O(n)
'''
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        items_appeared = {}
        for num in arr2:
            items_appeared[num] = 0
        items_missing = []
        for num in arr1:
            if num not in items_appeared:
                items_missing.append(num)
            else:
                items_appeared[num] += 1
        result = []
        for num in arr2:
            for i in range(items_appeared[num]):
                result.append(num)
        items_missing.sort()
        result.extend(items_missing)
        return result
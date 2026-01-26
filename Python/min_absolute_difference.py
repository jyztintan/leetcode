class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        n = len(arr)

        diff = inf
        for i in range(n - 1):
            diff = min(diff, arr[i + 1] - arr[i])

        lst = []
        for i in range(n - 1):
            if arr[i + 1] - arr[i] == diff:
                lst.append((arr[i], arr[i + 1]))

        return lst

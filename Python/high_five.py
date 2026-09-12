class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        items.sort(key=lambda x:(x[0],-x[1]))
        n = len(items)
        ans = []
        ptr = 0
        while ptr < n:
            student = items[ptr][0]
            total = 0
            for _ in range(5):
                total += items[ptr][1]
                ptr += 1
            ans.append((student, total//5))
            while ptr < n and items[ptr][0] == student:
                ptr += 1
        return ans

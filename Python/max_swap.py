class Solution:
    def maximumSwap(self, num: int) -> int:
        str_num = list(str(num))
        ideal = sorted(str_num, reverse=True)
        idx = -1
        original_high = -1
        for i, c in enumerate(str_num):
            if idx == -1:
                if c != ideal[i]:
                    idx = i
            else:
                if c == ideal[idx]:
                    original_high = i
        str_num[idx], str_num[original_high] = str_num[original_high], str_num[idx]
        return int("".join(str_num))

# print(Solution().maximumSwap(1993))
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        string_num = ""
        for c in s:
            string_num += str(ord(c) - ord('`'))
        for _ in range(k):
            string_num = str(sum(map(int, list(string_num))))
        return int(string_num)

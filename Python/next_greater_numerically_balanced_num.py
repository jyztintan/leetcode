class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def is_balanced(num):
            num = str(num)
            for d in range(10):
                if num.count(str(d)) != 0 and num.count(str(d)) != d:
                    return False
            return True

        curr = n + 1
        while not is_balanced(curr):
            curr += 1
        return curr

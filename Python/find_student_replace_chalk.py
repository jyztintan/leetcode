class Solution:
    def chalkReplacer(self, chalk, k: int) -> int:
        k = k % sum(chalk)
        ptr = 0
        for student in chalk:
            k -= student
            if k < 0:
                return ptr
            ptr += 1
        return 0
    
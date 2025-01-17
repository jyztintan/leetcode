class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        original = [True]
        n = len(derived)

        for idx in range(n - 1):
            if derived[idx] == 1:
                original.append(not original[-1])
            else:
                original.append(original[-1])

        return original[-1] ^ original[0] == derived[-1]

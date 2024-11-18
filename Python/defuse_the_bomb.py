class Solution:
    def decrypt(self, code, k: int):
        n = len(code)
        if k == 0:
            return [0] * n

        if k > 0:
            ptr = 0
        else:
            ptr = n - abs(k) - 1

        # Starting window
        curr = 0
        for i in range(abs(k)):
            ptr += 1
            curr += code[ptr]
            if ptr == n:
                ptr = 0

        ans = [curr]
        for i in range(n - 1):
            remove_idx = ptr - abs(k) + 1
            if remove_idx < 0:
                remove_idx += n
            curr -= code[remove_idx]
            ptr += 1
            if ptr == n:
                ptr = 0
            curr += code[ptr]
            ans.append(curr)

        return ans


code = [2,4,9,3]
print(Solution().decrypt(code, -2))
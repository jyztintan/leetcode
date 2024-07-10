class Solution:
    def letterCombinations(self, digits: str):
        table = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        ans = []
        if not digits:
            return ans

        def backtrack(pointer, substring):
            if pointer == len(digits):
                ans.append(substring)
                return
            for char in table[int(digits[pointer])]:
                substring += char
                backtrack(pointer + 1, substring)
                substring = substring[:-1]

        backtrack(0, "")
        return ans

print(Solution().letterCombinations("23"))




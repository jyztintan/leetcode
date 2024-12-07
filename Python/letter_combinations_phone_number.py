class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mapping = {"2": "abc", "3": "def", "4": "ghi", "5": 'jkl', '6': "mno", '7': 'pqrs', '8': 'tuv', '9': "wxyz"}
        combinations = []
        curr = []

        def backtrack(idx):
            if idx == len(digits):
                s = "".join(curr)
                combinations.append(s)
                return

            num = digits[idx]
            for possible_char in mapping[num]:
                curr.append(possible_char)
                backtrack(idx + 1)
                curr.pop()

        backtrack(0)
        return combinations



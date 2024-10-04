class Solution:
    def dividePlayers(self, skill) -> int:
        total = sum(skill)
        num_teams = len(skill) // 2
        if total % num_teams:
            return -1
        freq = {}
        for num in skill:
            freq[num] = freq.get(num, 0) + 1

        chemistry = 0
        equal = total // num_teams
        for num in freq:
            if freq.get(equal - num, 0) != freq[num]:
                return -1
            chemistry += (equal - num) * num * freq[num]
        return chemistry // 2

skill = [3,2,5,1,3,4]
print(Solution().dividePlayers(skill))
class Solution:
    def countSeniors(self, details) -> int:
        ans = 0
        for person in details:
            age = int(person[11:13])
            if age > 60:
                ans += 1
        return ans
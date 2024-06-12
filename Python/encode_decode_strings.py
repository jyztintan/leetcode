class Solution:

    def encode(self, strs):
        res = ""
        for s in strs:
            res += len(s) + "#" + s
        return res
    def decode(self, s):
        index = 0
        ans = []
        while index < len(s):
            pos = s.find("#", index)
            if pos == -1:
                return ans
            num = int(s[index:pos])
            ans.append(s[pos+1:pos+num+1])
            index = pos + num + 1
        return ans

# s = Solution()
# print(s.decode("3#hat4#thor"))
class Solution(object):
    def pushDominoes(self, dominoes):
        n = len(dominoes)
        force = [0] * n

        curr = 0
        for i in range(n):
            if dominoes[i] == "R":
                curr = n
            elif dominoes[i] == "L":
                curr = 0
            else:
                curr = max(curr - 1, 0)
            force[i] = curr

        for i in range(n - 1, -1, -1):
            if dominoes[i] == "L":
                curr = n
            elif dominoes[i] == "R":
                curr = 0
            else:
                curr = max(curr - 1, 0)
            force[i] -= curr

        ans = ""
        for domino in force:
            if domino > 0:
                ans += "R"
            elif domino < 0:
                ans += "L"
            else:
                ans += "."

        return ans

# dominoes = "RR.L"
# ret = Solution().pushDominoes(dominoes)
# print(ret)
# assert ret == "RR.L"
#
# dominoes = ".L.R...LR..L.."
# ret = Solution().pushDominoes(dominoes)
# print(ret)
# assert ret == "LL.RR.LLRRLL.."
#
# dominoes = ".L..LR."
# ret = Solution().pushDominoes(dominoes)
# print(ret)
# assert ret == "LLLLLRR"

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        st = []
        for num in nums:
            curr = num
            while st:
                g = gcd(st[-1], curr)
                if g == 1:
                    break
                curr = curr * st.pop() // g
            st.append(curr)
        return st

    def gcd(num1, num2):
        while num2 != 0:
            num1, num2 = num2, num1 % num2
        return num1

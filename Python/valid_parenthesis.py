class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []

        # Close and open bracket mapping for O(1) look up
        match = {")": '(', "]": '[', "}": "{"}
        for c in s:

            # If character is a closing bracket, it should have the opening bracket at top of stack
            if c in match:
                if not st or st.pop() != match[c]:
                    return False

            # Character is an open bracket, append to stack
            else:
                st.append(c)

        # If there are unmatched open brackets, it is still invalid
        if st:
            return False
        return True

# sol = Solution()
# print(sol.isValid("()[]"))
# print(sol.isValid("()[}]"))

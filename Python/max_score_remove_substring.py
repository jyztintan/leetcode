class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        # We check if getting 'ab' or 'ba' is better as we want to employ a greedy solution
        if x > y:
            better, worse = x, y
            first, second = 'a', 'b'
        else:
            better, worse = y, x
            first, second = 'b', 'a'

        # Our stack will hold all unmatched 'a's and 'b's
        st = []

        # Keep track of points accumulated as we iterate through the string
        ans = 0

        for c in s:

            # If the character is not 'a' or 'b', we need to flush our stack since it is impossible to match these
            if c not in "ab":

                # If there is a second character of the optimal string in the stack,
                # it can only be used to form the suboptimal string.
                # We check if the characters in our stack can form the suboptimal string
                new_st = []
                for c in st:
                    if c == first and new_st and new_st[-1] == second:
                        new_st.pop()
                        ans += worse
                    else:
                        new_st.append(c)

                st = []

            # If this character is the second character of the optimal substring, we check if we had just stored
            # the first character in our stack. If so, we form the optimal substring and remove both letters
            elif c == second and st and st[-1] == first:
                st.pop()
                ans += better

            # Either an unmatched second character of the optimal string
            # Or a pending matching first character of the optimal string
            else:
                st.append(c)

        # Repeat process to check for unmatched characters to see if we can form combinations
        # of the suboptimal substring instead.
        new_st = []
        for c in st:
            if c == first and new_st and new_st[-1] == second:
                new_st.pop()
                ans += worse
            else:
                new_st.append(c)

        return ans

# print(Solution().maximumGain("cdbcbbaaabab", 4, 5))
# O(N) Stack solution
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2:
            return False

        st = []
        unlocked = []

        for idx, c in enumerate(s):
            if locked[idx] == '0':
                unlocked.append(idx)
            elif c == '(':
                st.append(idx)
            elif c == ')':
                if st:
                    st.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False

        while st and unlocked and st[-1] < unlocked[-1]:
            st.pop()
            unlocked.pop()

        return not st




# O(N) Solution using variables
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2:
            return False

        max_open, min_open = 0, 0
        for idx, c in enumerate(s):
            if locked[idx] == '1':
                if c == '(':
                    max_open += 1
                    min_open += 1
                else:
                    max_open -= 1
                    min_open -= 1
            else:
                max_open += 1
                min_open -= 1

            if max_open < 0:
                return False
            min_open = max(min_open, 0)
        return min_open == 0
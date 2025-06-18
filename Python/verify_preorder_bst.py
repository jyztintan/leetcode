class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        limit = -float('inf')
        st = []
        for num in preorder:
            while st and num > st[-1]:
                limit = max(limit, st.pop())

            if num < limit:
                return False
            st.append(num)
        return True

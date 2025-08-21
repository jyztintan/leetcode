class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        heights = [0] * len(mat[0])
        ans = 0
        for row in mat:
            for col, num in enumerate(row):
                heights[col] = 0 if num == 0 else heights[col] + 1
            st = [[-1, 0, -1]]
            for col, height in enumerate(heights):
                while st[-1][2] >= height:
                    st.pop()
                prev_col, prev, _ = st[-1]
                curr = prev + (col - prev_col) * height
                st.append([col, curr, height])
                ans += curr
        return ans

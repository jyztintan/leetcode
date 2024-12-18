# Elegant Monotonic Stack O(N)
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        ans = [0] * n

        # Store value and index of previous prices
        st = []

        for idx, price in enumerate(prices):
            while st and st[-1][1] >= price:
                prev_idx, prev_price = st.pop()
                ans[prev_idx] = prev_price - price

            st.append((idx, price))

        while st:
            prev_idx, prev_price = st.pop()
            ans[prev_idx] = prev_price

        return ans

# Brute Force O(N^2)
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)

        ans = []
        for left, price in enumerate(prices):
            right = left + 1
            while right < n and prices[left] < prices[right]:
                right += 1
            if right == n:
                ans.append(prices[left])
            else:
                ans.append(prices[left] - prices[right])
        return ans
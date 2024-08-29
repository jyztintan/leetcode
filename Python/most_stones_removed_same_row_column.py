class Solution:
    def removeStones(self, stones) -> int:
        by_rows = {}
        by_cols = {}
        connected = {}

        for row, col in stones:
            if row not in by_rows:
                by_rows[row] = set()
            for stone in by_rows[row]:
                if stone not in connected:
                    connected[stone] = set()
                connected[stone].add((row, col))
                if (row, col) not in connected:
                    connected[(row, col)] = set()
                connected[(row, col)].add(stone)
            by_rows[row].add((row, col))

            if col not in by_cols:
                by_cols[col] = set()
            for stone in by_cols[col]:
                if stone not in connected:
                    connected[stone] = set()
                connected[stone].add((row, col))
                if (row, col) not in connected:
                    connected[(row, col)] = set()
                connected[(row, col)].add(stone)
            by_cols[col].add((row, col))

        # Perform DFS to remove stones
        visited = set()
        remain = 0
        st = []
        for row, col in stones:
            if (row, col) not in visited:
                remain += 1
                st.append((row, col))
                while st:
                    curr_stone = st.pop()
                    visited.add(curr_stone)
                    if curr_stone not in connected:
                        continue
                    for next_stone in connected[curr_stone]:
                        if next_stone not in visited:
                            st.append(next_stone)
        return len(stones) - remain




stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
print(Solution().removeStones(stones))

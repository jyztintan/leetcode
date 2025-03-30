class Solution:
    def partitionLabels(self, s: str):
        last_occur = {}
        # Get last occurrence first
        for idx, c in enumerate(s):
            last_occur[c] = idx

        # Build components
        components = []
        start = end = 0
        for idx, c in enumerate(s):
            # Extend the end
            end = max(end, last_occur[c])
            if end == idx:
                components.append(end - start + 1)
                start = end + 1
        return components

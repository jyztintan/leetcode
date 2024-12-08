class Solution:
    def partitionLabels(self, s: str):
        last_occur = {}
        for idx, c in enumerate(s):
            last_occur[c] = idx

        start = end = 0
        partitions = []
        for i,c in enumerate(s):
            # As we iterate through the characters, we extend the end
            end = max(end, last_occur[c])
            if i == end:
                partitions.append(end - start + 1)
                start = end + 1

        return partitions

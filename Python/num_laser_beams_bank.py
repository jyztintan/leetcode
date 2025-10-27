class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0
        total = 0
        for row in bank:
            devices = row.count("1")
            if devices > 0:
                total += devices * prev
                prev = devices
        return total

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        bit_count = []
        for num in arr:
            set_bits = bin(num).count("1")
            bit_count.append((set_bits, num))
        bit_count.sort()
        return list(num for set_bits, num in bit_count)

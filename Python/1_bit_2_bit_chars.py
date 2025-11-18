class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        ptr = 0
        is_one = None
        while ptr < len(bits):
            if bits[ptr] == 0:
                ptr += 1
                is_one = True
            else:
                ptr += 2
                is_one = False
        return is_one

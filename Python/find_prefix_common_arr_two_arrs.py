class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        set_a = set()
        set_b = set()

        C = []
        common = 0

        for idx in range(len(A)):
            ele_a, ele_b = A[idx], B[idx]

            if ele_a in set_b:
                set_b.remove(ele_a)
                common += 1
            else:
                set_a.add(ele_a)

            if ele_b in set_a:
                set_a.remove(ele_b)
                common += 1
            else:
                set_b.add(ele_b)

            C.append(common)

        return C

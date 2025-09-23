class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = list(map(int, version1.split('.')))
        version2 = list(map(int, version2.split('.')))
        ptr1, ptr2 = 0, 0
        limit1, limit2 = len(version1), len(version2)
        while ptr1 < limit1 and ptr2 < limit2:
            if version1[ptr1] > version2[ptr2]:
                return 1
            elif version1[ptr1] < version2[ptr2]:
                return -1
            ptr1 += 1
            ptr2 += 1

        if ptr2 == limit2 and any(num > 0 for num in version1[ptr1:]):
            return 1
        if ptr1 == limit1 and any(num > 0 for num in version2[ptr2:]):
            return -1
        return 0

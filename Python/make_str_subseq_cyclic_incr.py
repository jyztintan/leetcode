class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        # Pointer for str1
        ptr1 = 0
        # Pointer for str2
        ptr2 = 0

        while ptr2 < len(str2) and ptr1 < len(str1):
            char1 = str1[ptr1]
            char2 = str2[ptr2]
            if char1 == "z":
                next_char = "a"
            else:
                next_char = chr(ord(char1) + 1)
            # If we can match the characters from both pointers
            # They are either the same character	 or ascii value + 1
            if char1 == char2 or next_char == char2:
                ptr1 += 1
                ptr2 += 1

            else:
                ptr1 += 1

        # Check if we had iterated through the entire str2
        return ptr2 == len(str2)

Solution().canMakeSubsequence("abc", "ab")
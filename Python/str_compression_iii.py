class Solution:
    def compressedString(self, word: str) -> str:
        ptr = 0
        comp = ""
        n = len(word)
        while ptr < n:
            curr = word[ptr]
            count = 1
            while ptr + 1 < n and word[ptr + 1] == curr:
                count += 1
                ptr += 1

            # Handle count greater than 9
            while count > 9:
                count -= 9
                comp += f"9{curr}"
            # Handle Edge case: count = 0 when it was some multiple of 9
            if count:
                comp += f"{count}{curr}"

            ptr += 1
        return comp



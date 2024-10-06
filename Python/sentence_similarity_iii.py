class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        sentence1 = sentence1.split(" ")
        sentence2 = sentence2.split(" ")
        if len(sentence2) < len(sentence1):
            sentence1, sentence2 = sentence2, sentence1

        ptr1 = 0
        n = len(sentence1)
        ptr2 = 0
        m = len(sentence2)

        # Process prefix
        while ptr1 < n and ptr2 < m and sentence2[ptr2] == sentence1[ptr1]:
            ptr1 += 1
            ptr2 += 1
            # Only if sentence1 is a pure prefix of sentence2
            if ptr1 == n:
                return True
        # Ignore middle
        ptr2 = m - (n - ptr1)
        # Process suffix
        while ptr1 < n and ptr2 < m and sentence2[ptr2] == sentence1[ptr1]:
            ptr1 += 1
            ptr2 += 1
            if ptr1 == n and ptr2 == m:
                return True
        return False


# sentence1 = "c h p Ny"
# sentence2 = "c BDQ r h p Ny"
# print(Solution().areSentencesSimilar(sentence1, sentence2))


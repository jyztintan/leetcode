class Solution:
    def uncommonFromSentences(self, s1: str, s2: str):
        duplicated = set()

        s1_words = s1.split(" ")
        set_s1 = set()
        for word in s1_words:
            if word in set_s1:
                set_s1.remove(word)
                duplicated.add(word)
            else:
                set_s1.add(word)

        s2_words = s2.split(" ")
        set_s2 = set()
        for word in s2_words:
            if word in set_s2:
                set_s2.remove(word)
                duplicated.add(word)
            else:
                set_s2.add(word)

        return set_s1.symmetric_difference(set_s2).difference(duplicated)


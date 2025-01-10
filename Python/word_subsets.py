class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        universal = []

        mega_subset = [0] * 26
        for subset in words2:
            subset_freq = [0] * 26
            for c in subset:
                subset_freq[ord(c) - ord('a')] += 1

            # Keep the highest freq for each character
            for idx in range(26):
                mega_subset[idx] = max(mega_subset[idx], subset_freq[idx])

        universal = []
        for word in words1:
            word_freq = [0] * 26
            for c in word:
                word_freq[ord(c) - ord('a')] += 1
            is_universal = True
            for idx in range(26):
                if word_freq[idx] < mega_subset[idx]:
                    is_universal = False
                    break
            if is_universal:
                universal.append(word)

        return universal

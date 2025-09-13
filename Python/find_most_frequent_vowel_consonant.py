class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = 'aeiou'
        vowel_freq = defaultdict(int)
        consonant_freq = defaultdict(int)
        for c in s:
            if c in vowels:
                vowel_freq[c] += 1
            else:
                consonant_freq[c] += 1
        return max(vowel_freq.values(), default=0) + max(consonant_freq.values(), default=0)

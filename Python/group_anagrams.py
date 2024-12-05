from collections import defaultdict
from typing import List

# Time/Space: O(N * K) solution, since we are iterating through every word and getting a frequency count for characters
# Thereafter we get a tuple representation and store it as key
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupings = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            count = tuple(count)
            groupings[count].append(word)
        return list(groupings.values())

# O(N*KlogK) where N and K are the number of words and K is the (max) length of the words.
# This is because we iterate through each N words and sort the word in KlogK time.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupings = defaultdict(list)
        for word in strs:
            sorted_word = str(sorted(word))
            groupings[sorted_word].append(word)
        return list(groupings.values())

# strs = ["eat","tea","tan","ate","nat","bat"]
# print(groupAnagrams(strs))

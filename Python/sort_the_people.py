from typing import List
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = list(zip(names, heights))
        # Set the key to person's height as we want to sort by height
        # Set reverse as true since we want to sort in non-decreasing order
        people.sort(key=lambda person:person[1], reverse=True)
        return list(name for name, height in people)
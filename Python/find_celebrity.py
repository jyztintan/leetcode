# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        celeb = 0
        # Get the 'last' known person
        for friend in range(1, n):
            if knows(celeb, friend):
                celeb = friend
        # Make sure this 'last known' person does not know anyone, and anyone before must know this person
        for friend in range(n):
            if friend == celeb:
                continue
            if not knows(friend, celeb) or knows(celeb, friend):
                return -1
        return celeb


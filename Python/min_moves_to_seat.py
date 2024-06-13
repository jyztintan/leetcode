
"""
This solution uses the idea that when students and seats are sorted, the order in which the
students are positioned should move to the respective seat ordering, as it would be the nearest possible seat.

For example, consider the scenario where students are in positions [1, 3, 6, 10] and seats in positions [2, 5, 9, 80].
We would want the 1st student to move to the 1st seat, 2nd student to move to the 2nd seat ... i-th student to i-th seat.

Time Complexity: O(nlogn + nlogn + n) = O(nlogn)
1. Sorting seats and students - O(nlogn)
2. Loop through arrays to find the difference in positions - O(n)

Space Complexity: O(n)
1. Seats array - O(n)
2. Students array - O(n)
"""
class Solution:
    def minMovesToSeat(self, seats, students):
        seats.sort()
        students.sort()
        n = len(seats)
        ans = 0
        for i in range(n):
            ans += abs(seats[i] - students[i])
        return ans

"""
This solution uses the counting sort to increase time efficiency as n is noted to be <= 100.
Seats are represented by an integer 1 while students are represented by an integer -1.
We then count the total displacement between all students and seats to get the answer.

Time Complexity: O(m + n + n + m) = O(m + n), where m is the maximum position of a seat/student.
1. Create the positions array - O(m)
2. Loop through arrays to indicate student/seat - O(n + n)
3. Loop through positions array to count total displacement - O(m)

Space Complexity: O(n)
1. Seats array - O(n)
2. Students array - O(n)
3. Positions array - O(m)
"""
class Solution:
    def minMovesToSeat(self, seats, students):
        max_position = max(max(seats), max(students))
        positions = [0] * max_position

        # Seats are represented by 1 in the position array
        for seat in seats:
            positions[seat - 1] += 1

        # Students are represented by -1 in the position array.
        # Hence if a student is already sitting in a seat, the total displacement would be 0.
        for student in students:
            positions[student - 1] -= 1

        ans = 0
        displacement = 0
        for pos in positions:

            # We take the absolute value as we can view that the move of a seat/student has a cost of 1
            ans += abs(displacement)

            # We change the current displacement value,
            # increase if we now have more unmatched seats/students
            # decrease if we now have more matched seats/students
            displacement += pos

        return ans

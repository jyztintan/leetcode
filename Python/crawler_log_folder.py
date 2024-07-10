class Solution:
    def minOperations(self, logs) -> int:
        count = 0
        for log in logs:

            # Stay same directory, no movement
            if log == "./":
                continue

            # Move back one directory or stay in home dir
            elif log == "../":

                # Not in home dir, so move back one
                if count:
                    count -= 1

                # Already in home dir, remain in home dir
                else:
                    count = 0

            # Navigate to a child folder
            else:
                count += 1

        return count
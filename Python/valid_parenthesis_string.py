class Solution:
    def checkValidString(self, s: str) -> bool:
        # to store indices of '('
        open_stack = []
        # to store indices of '*'
        asterisk_stack = []

        for i, c in enumerate(s):
            if c == '(':
                open_stack.append(i)
            elif c == '*':
                asterisk_stack.append(i)
            elif c == ')':
                # Preferably use the opening brackets to match closing brackets first
                if open_stack:
                    open_stack.pop()
                elif asterisk_stack:
                    asterisk_stack.pop()
                else:
                    return False

        # Now check the remaining '(' with possible '*' replacements
        while open_stack:
            # There are no asterisk to match opening brackets
            if not asterisk_stack:
                return False
            # Get the index of the last '(' and the last '*'
            open_index = open_stack.pop()
            asterisk_index = asterisk_stack.pop()

            # If the asterisk comes before the '(', it cannot close it
            if open_index > asterisk_index:
                return False

        return True
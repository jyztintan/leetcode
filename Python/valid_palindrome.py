def isPalindrome(s: str) -> bool:
    new_str = ''
    for char in s:
        if char.isalpha():
            new_str += char.lower()
        if char.isnumeric():
            new_str += char
    return new_str == new_str[::-1]
        
s1 = "A man, a plan, a canal: Panama"
print(isPalindrome(s1))
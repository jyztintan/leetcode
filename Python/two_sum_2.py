def twoSum(numbers, target: int):
    left = 0
    right = len(numbers) - 1
    while True:
        total = numbers[left] + numbers[right]
        if total < target:
            left += 1
        elif total > target:
            right -= 1
        else:
            return [left + 1, right + 1]
numbers = [2,3,4] 
print(twoSum(numbers, 6))
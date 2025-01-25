class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)

        connected_components = []
        num_component = {}

        for num in sorted(nums):
            # If no component yet or limit exceeded, then we create a new component
            if not connected_components or abs(num - connected_components[-1][-1]) > limit:
                connected_components.append(deque())
            # Add num to component and record component index
            connected_components[-1].append(num)
            num_component[num] = len(connected_components) - 1

        result = []
        for num in nums:
            # Get the component by its index
            component = connected_components[num_component[num]]
            result.append(component.popleft())
        return result

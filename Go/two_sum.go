package Go

func twoSum(nums []int, target int) []int {
	seen := make(map[int]int)
	for i, num := range nums {
		if j, ok := seen[num]; ok {
			return []int{j, i}
		}
		seen[target-num] = i
	}
	return nil
}

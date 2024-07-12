package main

import (
	"fmt"
)

func main() {
	fmt.Println(getMaximumGenerated(7))
}

func getMaximumGenerated(n int) int {
	if n == 0 {
		return 0
	}
	nums := make([]int, n+1)
	nums[0], nums[1] = 0, 1
	for i := 0; i < len(nums)/2; i++ {
		if 2*i >= 2 && 2*i <= n {
			nums[2*i] = nums[i]
		}
		if 2*i+1 >= 2 && 2*i+1 <= n {
			nums[2*i+1] = nums[i] + nums[i+1]
		}
	}
	max := -1
	for _, i := range nums {
		if i > max {
			max = i
		}
	}
	return max
}

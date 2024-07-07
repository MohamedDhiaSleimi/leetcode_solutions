package main

import (
	"fmt"
)

func main() {
	fmt.Println(plusOne([]int{9}))
}

func plusOne(digits []int) []int {
	digits = append([]int{0}, digits...)
	for i := len(digits) - 1; i >= 0; i-- {
		digits[i] += 1
		if digits[i] > 9 {
			digits[i] = 0
		} else {
			if digits[0] == 0 {
				digits = digits[1:]
			}
			return digits
		}
	}
	ans := make([]int, len(digits)+1)
	ans[0] = 1
	return ans
}

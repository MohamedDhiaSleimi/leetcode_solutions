package main

import (
	"fmt"
)

func main() {
	fmt.Println(mySqrt(999999999999999999))
}

func mySqrt(x int) int {
	if x < 2 {
		return x
	}

	left, right := 1, x/2
	var mid int

	for left <= right {
		mid = left + (right-left)/2
		if mid*mid == x {
			return mid
		} else if mid*mid < x {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}

	return right
}

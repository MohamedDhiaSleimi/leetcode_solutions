package main

import (
	"fmt"
	"slices"
)

func main() {
	arr1 := []int{0, 1, 2, 3, 4}
	arr2 := []int{0, 1, 2, 2, 1}
	fmt.Println(createTargetArray(arr1, arr2))
	arr1 = []int{4, 2, 4, 3, 2}
	arr2 = []int{0, 0, 1, 3, 1}
	fmt.Println(createTargetArray(arr1, arr2))
}

func createTargetArray(nums []int, index []int) []int {
	res := make([]int, len(nums))
	for i := 0; i < len(nums); i++ {
		res = slices.Insert(res, index[i], nums[i])
	}
	return res[:len(nums)]
}

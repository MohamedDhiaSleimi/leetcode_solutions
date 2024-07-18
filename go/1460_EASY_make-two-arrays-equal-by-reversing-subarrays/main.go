package main

import (
	"fmt"
	"sort"
)

func canBeEqual(target []int, arr []int) bool {
	if len(arr) != len(target) {
		return false
	}
	sort.Ints(arr)
	sort.Ints(target)
	for i := range arr {
		if arr[i] != target[i] {
			return false
		}
	}
	return true
}

func main() {
	target := []int{1, 2, 3, 4}
	arr := []int{2, 4, 1, 3}
	fmt.Println(canBeEqual(target, arr))
}

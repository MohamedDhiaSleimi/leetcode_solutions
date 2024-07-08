package main

import (
	"fmt"
)

func main() {
	fmt.Println(findTheWinner(5, 2))
}

func findTheWinner(n int, k int) int {
	grp := make([]int, n)
	for i := 1; i < n+1; i++ {
		grp[i-1] = i
	}
	index := 0
	for len(grp) > 1 {
		index = (index + k - 1) % len(grp)
		grp = append(grp[0:index], grp[index+1:]...)
	}
	return grp[0]
}

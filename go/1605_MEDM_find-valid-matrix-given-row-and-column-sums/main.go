package main

import (
	"fmt"
)

func main() {
	printMatrix(restoreMatrix([]int{3, 8}, []int{4, 7}))
	printMatrix(restoreMatrix([]int{14, 9}, []int{6, 9, 8}))
}

func printMatrix(matrix [][]int) {
	for _, v := range matrix {
		fmt.Println(v)
	}
}

func restoreMatrix(rowSum []int, colSum []int) [][]int {
	n, m := len(rowSum), len(colSum)
	fmt.Println(n, m)
	res := make([][]int, n)
	for i := range res {
		res[i] = make([]int, m)
	}

	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			res[i][j] = min(rowSum[i], colSum[j])
			rowSum[i] -= res[i][j]
			colSum[j] -= res[i][j]
		}
	}
	return res
}

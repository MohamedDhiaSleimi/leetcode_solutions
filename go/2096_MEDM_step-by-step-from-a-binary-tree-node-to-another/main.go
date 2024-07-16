package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func getDirections(root *TreeNode, startValue int, destValue int) string {
	_, pathToStart := findInTree(root, startValue)
	_, pathToDest := findInTree(root, destValue)

	i := 0
	for i < len(pathToStart) && i < len(pathToDest) && pathToStart[i] == pathToDest[i] {
		i++
	}

	pathToStart = pathToStart[i:]
	pathToDest = pathToDest[i:]

	result := ""
	for range pathToStart {
		result += "U"
	}
	result += pathToDest

	return result
}

func findInTree(root *TreeNode, val int) (bool, string) {
	if root == nil {
		return false, ""
	}
	if root.Val == val {
		return true, ""
	}

	if root.Left != nil {
		ok1, path1 := findInTree(root.Left, val)
		if ok1 {
			return true, "L" + path1
		}
	}

	if root.Right != nil {
		ok2, path2 := findInTree(root.Right, val)
		if ok2 {
			return true, "R" + path2
		}
	}

	return false, ""
}

func main() {
	root := &TreeNode{Val: 1}
	root.Left = &TreeNode{Val: 2}
	root.Right = &TreeNode{Val: 3}
	root.Left.Left = &TreeNode{Val: 4}
	root.Left.Right = &TreeNode{Val: 5}
	root.Right.Left = &TreeNode{Val: 6}
	root.Right.Right = &TreeNode{Val: 7}

	startValue := 4
	destValue := 7
	fmt.Println(getDirections(root, startValue, destValue))
}

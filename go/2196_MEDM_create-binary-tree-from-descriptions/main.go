package main

import (
	"fmt"
	"strings"
)

// TreeNode defines a node in the binary tree
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func createBinaryTree(descriptions [][]int) *TreeNode {
	created := make(map[int]*TreeNode)
	parentCount := make(map[int]int)

	for _, desc := range descriptions {
		parentVal, childVal, isLeft := desc[0], desc[1], desc[2]
		var parentNode, childNode *TreeNode
		var ok bool

		if parentNode, ok = created[parentVal]; !ok {
			parentNode = &TreeNode{Val: parentVal}
			created[parentVal] = parentNode
		}

		if childNode, ok = created[childVal]; !ok {
			childNode = &TreeNode{Val: childVal}
			created[childVal] = childNode
		}

		if isLeft == 1 {
			parentNode.Left = childNode
		} else {
			parentNode.Right = childNode
		}

		parentCount[childVal]++
		if _, ok := parentCount[parentVal]; !ok {
			parentCount[parentVal] = 0
		}
	}

	var root *TreeNode
	for val, count := range parentCount {
		if count == 0 {
			root = created[val]
			break
		}
	}

	return root
}

// Helper function to print the binary tree (for testing purposes)
func printTree(root *TreeNode, level int) {
	if root == nil {
		return
	}
	printTree(root.Right, level+1)
	fmt.Printf("%s%d\n", strings.Repeat(string("    "), level), root.Val)
	printTree(root.Left, level+1)
}

func main() {
	descriptions := [][]int{
		{20, 15, 1},
		{20, 17, 0},
		{50, 20, 1},
		{50, 80, 0},
		{80, 19, 1},
	}
	root := createBinaryTree(descriptions)
	printTree(root, 0)
}

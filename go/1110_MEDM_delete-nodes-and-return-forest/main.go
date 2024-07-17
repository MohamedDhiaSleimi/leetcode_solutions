package main

import (
	"fmt"
	"strings"
)

func main() {
	// Example usage
	root := &TreeNode{
		Val: 1,
		Left: &TreeNode{
			Val: 2,
			Left: &TreeNode{
				Val: 4,
			},
			Right: &TreeNode{
				Val: 5,
			},
		},
		Right: &TreeNode{
			Val: 3,
			Left: &TreeNode{
				Val: 6,
			},
			Right: &TreeNode{
				Val: 7,
			},
		},
	}

	to_delete := []int{3, 5}
	result := delNodes(root, to_delete)

	for _, tree := range result {
		printTree(tree, 0)
		fmt.Println()
	}
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func delNodes(root *TreeNode, to_delete []int) []*TreeNode {
	toDeleteMap := make(map[int]bool)
	for _, val := range to_delete {
		toDeleteMap[val] = true
	}

	var res []*TreeNode

	var remove func(node *TreeNode) *TreeNode
	remove = func(node *TreeNode) *TreeNode {
		if node == nil {
			return nil
		}

		node.Left = remove(node.Left)
		node.Right = remove(node.Right)

		if toDeleteMap[node.Val] {
			if node.Left != nil {
				res = append(res, node.Left)
			}
			if node.Right != nil {
				res = append(res, node.Right)
			}
			return nil
		}

		return node
	}

	root = remove(root)
	if root != nil {
		res = append(res, root)
	}

	return res
}

func printTree(root *TreeNode, level int) {
	if root == nil {
		return
	}
	printTree(root.Right, level+1)
	fmt.Printf("%s%d\n", strings.Repeat("    ", level), root.Val)
	printTree(root.Left, level+1)
}

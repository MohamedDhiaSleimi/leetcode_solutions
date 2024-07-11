package main

import (
	"fmt"
	"strings"
)

func main() {
	testCases := []struct {
		input    string
		expected string
	}{
		{"(abcd)", "dcba"},
		{"(ed(et(oc))el)", "leetcode"},
		{"ta()usw((((a))))", "tauswa"},
		{"obxdpc()z()cgeuqvpf(d())", "obxdpczcgeuqvpfd"},
		{"s()uteawj((eg))", "suteawjeg"},
	}

	for _, testCase := range testCases {
		result := reverseParentheses(testCase.input)

		if result == testCase.expected {
			fmt.Println("-----------------------------------")
			fmt.Printf("input %v, Got: %v\n", testCase.input, result)
			fmt.Println("-----------------------------------")
		} else {
			fmt.Println("===================================")
			fmt.Printf("input %v\nExpected: %v Got: %v\n", testCase.input, testCase.expected, result)
			fmt.Println("===================================")
		}
	}
}

func reverseParentheses(s string) string {
	stack := []string{}
	for _, char := range s {
		if char == ')' {
			temp := ""
			for stack[len(stack)-1] != "(" {
				temp += stack[len(stack)-1]
				stack = stack[:len(stack)-1]
			}
			stack = stack[:len(stack)-1] // pop '('
			for _, c := range temp {
				stack = append(stack, string(c))
			}
		} else {
			stack = append(stack, string(char))
		}
	}
	return strings.Join(stack, "")
}

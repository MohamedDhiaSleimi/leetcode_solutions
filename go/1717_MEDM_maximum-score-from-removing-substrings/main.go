package main

import (
	"fmt"
)

func main() {
	testCases := []struct {
		input    []interface{}
		expected int
	}{
		{[]interface{}{"cdbcbbaaabab", 4, 5}, 19},
	}
	for _, testCase := range testCases {
		result := maximumGain(testCase.input[0].(string), testCase.input[1].(int), testCase.input[2].(int))

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

func maximumGain(s string, x int, y int) int {
	res := 0
	remove := func(weight int, str string) {
		stack := []byte{}
		for i := 0; i < len(s); i++ {
			char := s[i]
			if len(stack) > 0 && char == str[1] && stack[len(stack)-1] == str[0] {
				stack = stack[:len(stack)-1]
				res += weight
			} else {
				stack = append(stack, char)
			}
		}
		s = string(stack)
	}
	if x < y {
		remove(y, "ba")
		remove(x, "ab")
	} else {
		remove(x, "ab")
		remove(y, "ba")
	}
	return res
}

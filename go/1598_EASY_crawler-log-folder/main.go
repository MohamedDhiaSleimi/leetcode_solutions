package main

import (
	"fmt"
)

func main() {
	testCases := []struct {
		input    []string
		expected int
	}{
		{[]string{"d1/", "d2/", "../", "d21/", "./"}, 2},
	}

	for _, testCase := range testCases {
		result := minOperations(testCase.input)

		if result == testCase.expected {
			fmt.Printf("Test passed for input %v. Expected: %v, Got: %v\n", testCase.input, testCase.expected, result)
		} else {
			fmt.Printf("Test failed for input %v. Expected: %v, Got: %v\n", testCase.input, testCase.expected, result)
		}
	}
}

func minOperations(logs []string) int {
	stepsNeeded := 0
	for _, i := range logs {
		switch i {
		case "../":
			if stepsNeeded > 0 {
				stepsNeeded--
			}
		case "./":
			continue
		default:
			stepsNeeded++
		}
	}
	return stepsNeeded
}

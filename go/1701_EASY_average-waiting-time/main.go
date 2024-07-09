package main

import "fmt"

func main() {
	testCases := []struct {
		input    [][]int
		expected float64
	}{
		{[][]int{{1, 2}, {2, 5}, {4, 3}}, 5.00000},
	}

	for _, testCase := range testCases {
		result := averageWaitingTime(testCase.input)

		if result == testCase.expected {
			fmt.Printf("Test passed for input %v. Expected: %f, Got: %f\n", testCase.input, testCase.expected, result)
		} else {
			fmt.Printf("Test failed for input %v. Expected: %f, Got: %f\n", testCase.input, testCase.expected, result)
		}
	}
}

func averageWaitingTime(customers [][]int) float64 {
	expectedEndTime := 0
	waitTimes := 0
	for _, v := range customers {
		if expectedEndTime < v[0] {
			expectedEndTime = v[0] + v[1]
		} else {
			expectedEndTime += v[1]
		}
		waitTimes += expectedEndTime - v[0]
	}
	return float64(waitTimes) / float64(len(customers))
}

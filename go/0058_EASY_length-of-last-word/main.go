package main

import (
	"fmt"
	"strings"
	"unicode/utf8"
)

func main() {
	fmt.Println(lengthOfLastWord("test    test   "))
}

func lengthOfLastWord(s string) int {
	split := delete_empty(strings.Split(s, " "))

	return utf8.RuneCountInString(split[len(split)-1])
}

func delete_empty(s []string) []string {
	var r []string
	for _, str := range s {
		if str != "" {
			r = append(r, str)
		}
	}
	return r
}

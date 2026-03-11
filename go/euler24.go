// euler24 находит миллионную словарную перестановку из цифр 0-9.
//
// Решение задачи Эйлера №24.
package main

import (
	"fmt"
	"sort"
	"time"
)

func permutations(arr []int) [][]int {
	result := [][]int{{}}
	for _, elem := range arr {
		newResult := [][]int{}
		for _, permutation := range result {
			for i := 0; i <= len(permutation); i++ {
				newPermutation := make([]int, len(permutation)+1)
				copy(newPermutation, permutation[:i])
				newPermutation[i] = elem
				copy(newPermutation[i+1:], permutation[i:])
				newResult = append(newResult, newPermutation)
			}
		}
		result = newResult
	}
	return result
}

func euler24() {
	n := 1000000

	startTime := time.Now()
	arr := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	perms := permutations(arr)
	if n-1 < len(perms) {
		for _, v := range perms[n-1] {
			fmt.Print(v)
		}
		fmt.Println()
	}
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	fmt.Println(time.Since(startTime))
}

func main() {
	euler24()
}

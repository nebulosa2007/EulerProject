// euler41 находит наибольшее n-значное пан-цифровое простое число.
//
// Решение задачи Эйлера №41.
package main

import (
	"fmt"
	"math"
	"time"
)

func isPrime(number int) bool {
	if number < 2 {
		return false
	}
	if number == 2 || number == 3 || number == 5 || number == 7 {
		return true
	}
	if number%2 == 0 || number%3 == 0 || number%5 == 0 {
		return false
	}
	sqrt := int(math.Sqrt(float64(number)))
	for i := 5; i <= sqrt; i += 6 {
		if number%i == 0 || number%(i+2) == 0 {
			return false
		}
	}
	return true
}

func euler41() {
	n := 9

	startTime := time.Now()
	maxPanPrime := 0
	for z := n; z > 1; z-- {
		// Generate all permutations of 1..z
		perms := generatePermutations(z)
		for _, p := range perms {
			if p[0] == 0 {
				continue
			}
			num := 0
			for _, d := range p {
				num = num*10 + d
			}
			if isPrime(num) && num > maxPanPrime {
				maxPanPrime = num
			}
		}
		if maxPanPrime > 0 {
			break
		}
	}
	fmt.Println(maxPanPrime)
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	fmt.Println(time.Since(startTime))
}

func generatePermutations(n int) [][]int {
	arr := make([]int, n)
	for i := 0; i < n; i++ {
		arr[i] = i + 1
	}
	return permute(arr)
}

func permute(arr []int) [][]int {
	result := [][]int{}
	permuteHelper(arr, 0, &result)
	return result
}

func permuteHelper(arr []int, i int, result *[][]int) {
	if i == len(arr) {
		tmp := make([]int, len(arr))
		copy(tmp, arr)
		*result = append(*result, tmp)
	} else {
		for j := i; j < len(arr); j++ {
			arr[i], arr[j] = arr[j], arr[i]
			permuteHelper(arr, i+1, result)
			arr[i], arr[j] = arr[j], arr[i]
		}
	}
}

func main() {
	euler41()
}

// euler49 находит 12-значное число из трех членов арифметической
// прогрессии простых чисел.
//
// Решение задачи Эйлера №49.
package main

import (
	"fmt"
	"math"
	"sort"
	"time"
)

func eratosfen(number int) []bool {
	sieve := make([]bool, number+1)
	for i := range sieve {
		sieve[i] = true
	}
	sieve[0] = false
	sieve[1] = false
	for i := 2; i*i <= number; i++ {
		if sieve[i] {
			for j := i * i; j <= number; j += i {
				sieve[j] = false
			}
		}
	}
	return sieve
}

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

func twelveDigit(panPrimesCheck []int) string {
	for i := 0; i < len(panPrimesCheck); i++ {
		for j := i + 1; j < len(panPrimesCheck); j++ {
			delta := panPrimesCheck[j] - panPrimesCheck[i]
			if contains(panPrimesCheck, panPrimesCheck[j]+delta) {
				return fmt.Sprintf("%d%d%d",
					panPrimesCheck[i],
					panPrimesCheck[j],
					panPrimesCheck[j]+delta)
			}
		}
	}
	return ""
}

func euler49() {
	n := 4

	startTime := time.Now()
	sieve := eratosfen(powInt(10, n))
	primes := make([]int, 0)
	for i := 1000; i <= powInt(10, n); i++ {
		if sieve[i] {
			primes = append(primes, i)
		}
	}
	primePermutation := make([]int, 0)
	for _, setsPrimes := range primes {
		perms := permutations(digitsToSlice(setsPrimes))
		prCheck := make([]int, 0)
		seen := make(map[int]bool)
		for _, p := range perms {
			num := sliceToInt(p)
			if sieve[num] && !seen[num] {
				prCheck = append(prCheck, num)
				seen[num] = true
			}
		}
		sort.Ints(prCheck)
		if len(prCheck) >= 3 {
			found := twelveDigit(prCheck)
			if found != "" && !contains(primePermutation, toInt(found)) {
				primePermutation = append(primePermutation, toInt(found))
			}
		}
	}
	maxVal := 0
	for _, v := range primePermutation {
		if v > maxVal {
			maxVal = v
		}
	}
	fmt.Println(maxVal)
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	fmt.Println(time.Since(startTime))
}

func contains(slice []int, val int) bool {
	for _, v := range slice {
		if v == val {
			return true
		}
	}
	return false
}

func digitsToSlice(n int) []int {
	var result []int
	for n > 0 {
		result = append([]int{n % 10}, result...)
		n /= 10
	}
	return result
}

func sliceToInt(slice []int) int {
	result := 0
	for _, v := range slice {
		result = result*10 + v
	}
	return result
}

func toInt(s string) int {
	result := 0
	for _, c := range s {
		result = result*10 + int(c-'0')
	}
	return result
}

func powInt(base, exp int) int {
	result := 1
	for i := 0; i < exp; i++ {
		result *= base
	}
	return result
}

func main() {
	euler49()
}

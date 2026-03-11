// euler35 считает количество круговых простых чисел меньше миллиона.
//
// Решение задачи Эйлера №35.
package main

import (
	"fmt"
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

func rotate(n int, power int) int {
	s := fmt.Sprintf("%d", n)
	rotated := s[1:] + s[:1]
	result := 0
	fmt.Sscan(rotated, &result)
	return result
}

func euler35() {
	n := 1000000

	startTime := time.Now()
	sieve := eratosfen(n)
	primes := make(map[int]bool)
	for i := 2; i <= n; i++ {
		if sieve[i] {
			primes[i] = true
		}
	}
	delete(primes, 0)
	delete(primes, 1)
	circularPrimes := make([]int, 0)
	for i := range primes {
		hasZero := false
		for _, c := range fmt.Sprintf("%d", i) {
			if c == '0' {
				hasZero = true
				break
			}
		}
		if hasZero {
			continue
		}

		power := len(fmt.Sprintf("%d", i)) - 1
		nextNum := i
		circularPrimesCheck := []int{i}
		for j := 0; j < power; j++ {
			nextNum = rotate(nextNum, power)
			if primes[nextNum] {
				circularPrimesCheck = append(circularPrimesCheck, nextNum)
			} else {
				circularPrimesCheck = nil
				break
			}
		}
		if circularPrimesCheck != nil {
			for _, x := range circularPrimesCheck {
				if !contains(circularPrimes, x) {
					circularPrimes = append(circularPrimes, x)
				}
			}
		}
	}
	fmt.Println(len(circularPrimes))
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	primesBool := make([]bool, n+1)
	for i := range primesBool {
		primesBool[i] = true
	}
	i := 2
	for i*i <= n {
		if primesBool[i] {
			for j := i * 2; j <= n; j += i {
				primesBool[j] = false
			}
		}
		i++
	}
	primesBool[0] = false
	primesBool[1] = false
	count := 0
	for i = 1; i <= n; i++ {
		if !primesBool[i] {
			continue
		}
		nextNum := fmt.Sprintf("%d", i)
		flag := true
		for range nextNum {
			nextNum = nextNum[1:] + nextNum[:1]
			num := 0
			fmt.Sscan(nextNum, &num)
			flag = flag && primesBool[num]
		}
		if flag {
			count++
		}
	}
	fmt.Println(count)
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

func main() {
	euler35()
}

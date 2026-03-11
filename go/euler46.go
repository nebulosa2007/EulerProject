// euler46 находит наименьшее нечетное составное число, которое нельзя
// записать как сумму простого числа и удвоенного квадрата.
//
// Решение задачи Эйлера №46.
package main

import (
	"fmt"
	"math"
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

func euler46() {
	n := 10000

	startTime := time.Now()
	sieve := eratosfen(n)
	goldbahConjecture := make(map[int]bool)
	primes := make([]int, 0)
	for i := 2; i <= n; i++ {
		if sieve[i] {
			primes = append(primes, i)
			goldbahConjecture[i] = true
		}
	}
	for _, p := range primes {
		for k := 0; k*k*2 < n; k++ {
			goldbahConjecture[p+2*k*k] = true
		}
	}
	result := -1
	for i := 3; i < n; i += 2 {
		if !sieve[i] && !goldbahConjecture[i] {
			result = i
			break
		}
	}
	fmt.Println(result)
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	fmt.Println(time.Since(startTime))
}

func main() {
	euler46()
}

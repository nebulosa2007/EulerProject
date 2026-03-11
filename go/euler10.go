// euler10 находит сумму всех простых чисел меньше двух миллионов.
//
// Решение задачи Эйлера №10.
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

func euler10() {
	n := 2000000

	startTime := time.Now()
	sieve := eratosfen(n)
	sum := 0
	for i := 2; i <= n; i++ {
		if sieve[i] {
			sum += i
		}
	}
	fmt.Println(sum)
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	sieve = eratosfen(n)
	sum = 0
	for i := 2; i <= n; i++ {
		if sieve[i] {
			sum += i
		}
	}
	fmt.Println(sum)
	fmt.Println(time.Since(startTime))
}

func main() {
	euler10()
}

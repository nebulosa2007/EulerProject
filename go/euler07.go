// euler07 находит 10001-е простое число.
//
// Решение задачи Эйлера №7.
package main

import (
	"fmt"
	"time"
)

func isPrime(n int) bool {
	if n < 2 {
		return false
	}
	if n == 2 {
		return true
	}
	if n%2 == 0 {
		return false
	}
	for i := 3; i*i <= n; i += 2 {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func euler07() {
	n := 10001

	startTime := time.Now()
	count := 0
	num := 2
	for {
		if isPrime(num) {
			count++
			if count == n {
				fmt.Println(num)
				break
			}
		}
		num++
	}
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	count = 0
	num = 2
	for {
		if isPrime(num) {
			count++
			if count == n {
				fmt.Println(num)
				break
			}
		}
		num++
	}
	fmt.Println(time.Since(startTime))
}

func main() {
	euler07()
}

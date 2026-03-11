// euler05 находит самое маленькое число, делящееся нацело на все числа от 1 до 20.
//
// Решение задачи Эйлера №5.
package main

import (
	"fmt"
	"math"
	"time"
)

// eratosfen генерирует простые числа вплоть до заданного числа (решето Эратосфена).
func eratosfen(number int) []int {
	sieve := make([]int, number+1)
	for i := range sieve {
		sieve[i] = i
	}
	sieve[1] = 0
	for i := 2; i*i <= number; i++ {
		if sieve[i] != 0 {
			for j := 2 * i; j <= number; j += i {
				sieve[j] = 0
			}
		}
	}
	result := make([]int, 0)
	for _, v := range sieve {
		if v != 0 {
			result = append(result, v)
		}
	}
	return result
}

// isPrime проверка числа на простоту перебором делителей.
func isPrime(number int) bool {
	primes := []int{2, 3, 5, 7}
	for _, p := range primes {
		if number == p {
			return true
		}
	}
	if number < 2 || number%2 == 0 {
		return false
	}
	if number%3 == 0 || number%5 == 0 {
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

// euler05 решает задачу Эйлера №5.
//
// Какое самое маленькое число делится нацело на все числа от 1 до 20?
func euler05() {
	n := 20
	// Вариант 1
	startTime := time.Now()
	result := 1
	primes := eratosfen(n)
	for _, k := range primes {
		if k > 1 {
			i := 1
			for powInt(k, i+1) < n {
				i++
			}
			result *= powInt(k, i)
		}
	}
	fmt.Println(result)
	fmt.Println(time.Since(startTime))

	// Вариант 2
	startTime = time.Now()
	result = 1
	for k := 2; k <= n; k++ {
		if isPrime(k) {
			maxPower := 1
			for powInt(k, maxPower+1) < n {
				maxPower++
			}
			result *= powInt(k, maxPower)
		}
	}
	fmt.Println(result)
	fmt.Println(time.Since(startTime))
}

func powInt(base, exp int) int {
	result := 1
	for i := 0; i < exp; i++ {
		result *= base
	}
	return result
}

func main() {
	euler05()
}

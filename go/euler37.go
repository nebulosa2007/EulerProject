// euler37 находит сумму одиннадцати простых чисел, из которых можно
// выбрасывать цифры как справа налево, так и слева направо.
//
// Решение задачи Эйлера №37.
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

func delDigitLeftOrRight(number int) []int {
	result := []int{number}
	numberStr := fmt.Sprintf("%d", number)
	power := len(numberStr) - 1
	for k := 1; k <= power; k++ {
		left := numberStr[k:]
		right := numberStr[:len(numberStr)-k]
		if left != "" {
			l, _ := fmt.Sscan(left, &l)
			result = append(result, l)
		}
		if right != "" {
			r, _ := fmt.Sscan(right, &r)
			result = append(result, r)
		}
	}
	return result
}

func euler37() {
	n := 11

	startTime := time.Now()
	dimension := 1000000
	sieve := eratosfen(dimension)
	primes := make([]int, 0)
	for i := 2; i <= dimension; i++ {
		if sieve[i] && i != 2 && i != 3 && i != 5 && i != 7 {
			primes = append(primes, i)
		}
	}
	trucalablePrimes := make([]int, 0)
	counter := 0
	for len(trucalablePrimes) < n && counter < len(primes) {
		nextPrime := primes[counter]
		counter++
		allPrime := true
		for _, v := range delDigitLeftOrRight(nextPrime) {
			if !isPrime(v) {
				allPrime = false
				break
			}
		}
		if allPrime {
			trucalablePrimes = append(trucalablePrimes, nextPrime)
		}
	}
	sum := 0
	for _, v := range trucalablePrimes {
		sum += v
	}
	fmt.Println(sum)
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	c := 0
	s := 0
	i := n
	for c < n {
		allPrime := true
		for _, v := range delDigitLeftOrRight(i) {
			if !isPrime(v) {
				allPrime = false
				break
			}
		}
		if allPrime {
			c++
			s += i
		}
		i += 2
	}
	fmt.Println(s)
	fmt.Println(time.Since(startTime))
}

func main() {
	euler37()
}

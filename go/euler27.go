// euler27 находит произведение коэффициентов a и b для квадратичного
// выражения с максимальным числом простых чисел.
//
// Решение задачи Эйлера №27.
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

func euler27() {
	n := 1000

	startTime := time.Now()
	primesNum := make([]int, 0)
	sieve := eratosfen(n)
	for i := 2; i <= n; i++ {
		if sieve[i] {
			primesNum = append(primesNum, i)
		}
	}
	primesNum = append([]int{1}, primesNum...)
	maxNPrimes := 0
	axb := 0
	for _, b := range primesNum {
		for _, a := range primesNum {
			i := 0
			for x := a; x > -2*a; x -= 2 * a {
				quadratic := i*i + x*i + b
				if !isPrime(quadratic) || quadratic <= 0 {
					if i-1 > maxNPrimes {
						maxNPrimes = i - 1
						axb = x * b
					}
					break
				}
				i++
			}
		}
	}
	fmt.Println(axb)
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	fmt.Println(time.Since(startTime))
}

func main() {
	euler27()
}

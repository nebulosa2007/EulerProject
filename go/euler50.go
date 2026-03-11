// euler50 находит простое число меньше миллиона, которое может быть
// записано как сумма наибольшего количества последовательных простых чисел.
//
// Решение задачи Эйлера №50.
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

func euler50() {
	n := 1000000

	startTime := time.Now()
	conPrimes := make([]int, 0)
	sumConPrimes := 0
	for i := 2; ; i++ {
		if !isPrime(i) {
			continue
		}
		if sumConPrimes+i >= n {
			for !isPrime(sumConPrimes) {
				sumConPrimes -= conPrimes[0]
				conPrimes = conPrimes[1:]
			}
			break
		}
		conPrimes = append(conPrimes, i)
		sumConPrimes += i
	}
	fmt.Printf("%d %d\n", sumConPrimes, len(conPrimes))
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	fmt.Println(time.Since(startTime))
}

func main() {
	euler50()
}

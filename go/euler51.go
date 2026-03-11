// euler51 находит наименьшее простое число из восьми простых чисел,
// полученных заменой части цифр одинаковыми цифрами.
//
// Решение задачи Эйлера №51.
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

func euler51() {
	startTime := time.Now()
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	fmt.Println(time.Since(startTime))
}

func main() {
	euler51()
}

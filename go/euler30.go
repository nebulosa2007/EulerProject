// euler30 находит сумму всех чисел, которые могут быть записаны как
// сумма пятых степеней их цифр.
//
// Решение задачи Эйлера №30.
package main

import (
	"fmt"
	"time"
)

func sumPowerOfDigits(x int, n int) int {
	sum := 0
	for x > 0 {
		digit := x % 10
		pow := 1
		for i := 0; i < n; i++ {
			pow *= digit
		}
		sum += pow
		x /= 10
	}
	return sum
}

func euler30() {
	n := 5

	startTime := time.Now()
	numList := make([]int, 0)
	upperBound := n * powInt(9, n)
	for x := 2; x < upperBound; x++ {
		if sumPowerOfDigits(x, n) == x {
			numList = append(numList, x)
		}
	}
	sum := 0
	for _, v := range numList {
		sum += v
	}
	fmt.Println(sum)
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	sum = 0
	for x := 2; x < upperBound; x++ {
		if sumPowerOfDigits(x, n) == x {
			sum += x
		}
	}
	fmt.Println(sum)
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
	euler30()
}

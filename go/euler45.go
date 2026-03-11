// euler45 находит следующее треугольное число, являющееся также
// пятиугольным и шестиугольным.
//
// Решение задачи Эйлера №45.
package main

import (
	"fmt"
	"math"
	"time"
)

func figurateNumber(number int, base int) int {
	return int(((base-2)*number*number - (base-4)*number) / 2)
}

func isFigurateNumber(testNumber int, base int) bool {
	r := math.Sqrt(float64(8*(base-2)*testNumber + (base-4)*(base-4)))
	val := (r + float64(base-4)) / float64(2*base-4)
	_, frac := math.Modf(val)
	return frac < 0.000001 || frac > 0.999999
}

func euler45() {
	n := 143

	startTime := time.Now()
	i := n + 1
	testNumber := figurateNumber(i, 6)
	for !isFigurateNumber(testNumber, 5) {
		i++
		testNumber = figurateNumber(i, 6)
	}
	result := figurateNumber(i*2-1, 3)
	fmt.Println(result)
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	fmt.Println(time.Since(startTime))
}

func main() {
	euler45()
}

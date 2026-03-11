// euler44 находит пару пятиугольных чисел с минимальной разностью.
//
// Решение задачи Эйлера №44.
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

func euler44() {
	startTime := time.Now()
	i := 1
	flag := true
	result := 0
	for flag {
		i++
		nextPent := figurateNumber(i, 5)
		for j := i - 1; j > 0; j-- {
			prevPent := figurateNumber(j, 5)
			diff := nextPent - prevPent
			if isFigurateNumber(diff, 5) && isFigurateNumber(prevPent+nextPent, 5) {
				result = diff
				flag = false
				break
			}
		}
	}
	fmt.Println(result)
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	fmt.Println(time.Since(startTime))
}

func main() {
	euler44()
}

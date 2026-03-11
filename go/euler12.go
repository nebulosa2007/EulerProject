// euler12 находит первое треугольное число с более чем 500 делителями.
//
// Решение задачи Эйлера №12.
package main

import (
	"fmt"
	"math"
	"time"
)

func allFactorsList(number int, justCount bool) int {
	divisor := 2
	divisorList := []int{1, number}
	for i := 2; i <= int(math.Sqrt(float64(number)))+1; i++ {
		if number%i == 0 {
			if justCount {
				divisor += 2
			} else {
				divisorList = append(divisorList, i)
				divisorList = append(divisorList, number/i)
			}
		}
	}
	if justCount {
		if int(math.Sqrt(float64(number)))*int(math.Sqrt(float64(number))) == number {
			return divisor - 1
		}
		return divisor
	}
	if int(math.Sqrt(float64(number)))*int(math.Sqrt(float64(number))) == number {
		return len(divisorList) - 1
	}
	return len(divisorList)
}

func figurateNumber(number int, base int) int {
	return int(((base-2)*number*number - (base-4)*number) / 2)
}

func euler12() {
	n := 500

	startTime := time.Now()
	i := 1
	triangle := figurateNumber(i, 3)
	divisors := allFactorsList(triangle, true)
	for divisors < n {
		i++
		triangle = figurateNumber(i, 3)
		divisors = allFactorsList(triangle, true)
	}
	fmt.Printf("%d-th triangle number: %d with %d divisors\n", i, triangle, divisors)
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	fmt.Println(time.Since(startTime))
}

func main() {
	euler12()
}

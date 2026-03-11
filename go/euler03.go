// euler03 находит самый большой делитель числа 600 851 475 143,
// являющийся простым числом.
//
// Решение задачи Эйлера №3.
package main

import (
	"fmt"
	"math"
	"time"
)

// primeFactorsList возвращает список простых множителей заданного числа.
func primeFactorsList(n int) []int {
	divisor := 2
	nodarray := make([]int, 0)
	for divisor*divisor <= n {
		if n%divisor == 0 {
			n /= divisor
			nodarray = append(nodarray, divisor)
		} else {
			divisor++
		}
	}
	if n != 1 {
		nodarray = append(nodarray, n)
	}
	return nodarray
}

// euler03 решает задачу Эйлера №3.
//
// Каков самый большой делитель числа 600 851 475 143,
// являющийся простым числом?
func euler03() {
	n := 600_851_475_143
	// Вариант 1
	startTime := time.Now()
	factors := primeFactorsList(n)
	maxFactor := 0
	for _, f := range factors {
		if f > maxFactor {
			maxFactor = f
		}
	}
	fmt.Println(maxFactor)
	fmt.Println(time.Since(startTime))

	// Вариант 2
	startTime = time.Now()
	result := n
	divisor := 2
	for divisor*divisor <= result {
		if result%divisor == 0 {
			result /= divisor
		} else {
			if divisor == 2 {
				divisor = 3
			} else {
				divisor += 2
			}
		}
	}
	fmt.Println(result)
	fmt.Println(time.Since(startTime))
}

func main() {
	euler03()
}

// euler23 находит сумму всех положительных чисел, которые не могут
// быть записаны как сумма двух избыточных чисел.
//
// Решение задачи Эйлера №23.
package main

import (
	"fmt"
	"math"
	"time"
)

func allFactorsList(number int) []int {
	divisorList := []int{1, number}
	for i := 2; i <= int(math.Sqrt(float64(number)))+1; i++ {
		if number%i == 0 {
			divisorList = append(divisorList, i)
			divisorList = append(divisorList, number/i)
		}
	}
	return divisorList
}

func euler23() {
	n := 28123

	startTime := time.Now()
	numberList := make([]int, n)
	startSum := 0
	for i := 0; i < n; i++ {
		startSum += i
	}
	for i := 0; i < n; i++ {
		divisorList := allFactorsList(i)[:len(allFactorsList(i))-1]
		if sumSlice(divisorList) > i {
			numberList[i] = i
		}
	}
	result := 0
	for i := 0; i < n; i++ {
		if i*2 < n {
			result += i * 2
		}
	}
	fmt.Println(startSum - result)
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	fmt.Println(time.Since(startTime))
}

func sumSlice(slice []int) int {
	total := 0
	for _, v := range slice {
		total += v
	}
	return total
}

func main() {
	euler23()
}

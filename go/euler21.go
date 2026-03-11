// euler21 считает сумму всех дружественных чисел меньше 10000.
//
// Решение задачи Эйлера №21.
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

func euler21() {
	n := 10000

	startTime := time.Now()
	amicablePairs := make([]int, 0)
	for x := 10; x < n; x++ {
		if !contains(amicablePairs, x) {
			xSumDivisors := sumSlice(allFactorsList(x)) - x
			ySumDivisors := sumSlice(allFactorsList(xSumDivisors)) - xSumDivisors
			if ySumDivisors == x && x != xSumDivisors {
				amicablePairs = append(amicablePairs, x)
				amicablePairs = append(amicablePairs, xSumDivisors)
			}
		}
	}
	fmt.Println(sumSlice(amicablePairs))
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	divisorSum := make([]int, n)
	for i := 1; i < n; i++ {
		for j := i * 2; j < n; j += i {
			divisorSum[j] += i
		}
	}
	sumAmicPairs := 0
	for i := 1; i < n; i++ {
		j := divisorSum[i]
		if j != i && j < n && divisorSum[j] == i {
			sumAmicPairs += i
		}
	}
	fmt.Println(sumAmicPairs)
	fmt.Println(time.Since(startTime))
}

func contains(slice []int, val int) bool {
	for _, v := range slice {
		if v == val {
			return true
		}
	}
	return false
}

func sumSlice(slice []int) int {
	total := 0
	for _, v := range slice {
		total += v
	}
	return total
}

func main() {
	euler21()
}

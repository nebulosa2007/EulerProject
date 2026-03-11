// euler47 находит первое число из четырех последовательных чисел с
// четырьмя различными простыми множителями.
//
// Решение задачи Эйлера №47.
package main

import (
	"fmt"
	"time"
)

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

func uniqueFactors(n int) int {
	factors := make(map[int]bool)
	divisor := 2
	for divisor*divisor <= n {
		if n%divisor == 0 {
			factors[divisor] = true
			for n%divisor == 0 {
				n /= divisor
			}
		}
		divisor++
	}
	if n > 1 {
		factors[n] = true
	}
	return len(factors)
}

func euler47() {
	n := 4

	startTime := time.Now()
	i := 1
	counter := 0
	resultI := 0
	for {
		i++
		if uniqueFactors(i) == n {
			counter++
			if counter == n {
				resultI = i
				break
			}
		} else {
			counter = 0
		}
	}
	fmt.Println(i - n + 1)
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	siege := make([]int, 150000)
	counter = 0
	resultI = 0
	for i := 2; i < len(siege); i++ {
		if siege[i] == n {
			counter++
			if counter == n {
				resultI = i
				break
			}
		} else {
			counter = 0
			if siege[i] == 0 {
				for j := i; j < len(siege); j += i {
					siege[j]++
				}
			}
		}
	}
	if resultI == 0 {
		fmt.Println("Need to increase siege")
	} else {
		fmt.Println(resultI - n + 1)
	}
	fmt.Println(time.Since(startTime))
}

func main() {
	euler47()
}

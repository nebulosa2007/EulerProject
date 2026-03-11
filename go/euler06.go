// euler06 находит разность между суммой квадратов и квадратом суммы
// первых ста натуральных чисел.
//
// Решение задачи Эйлера №6.
package main

import (
	"fmt"
	"time"
)

func euler06() {
	n := 100

	startTime := time.Now()
	sum := 0
	sumSq := 0
	for i := 1; i <= n; i++ {
		sum += i
		sumSq += i * i
	}
	fmt.Println(sum*sum - sumSq)
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	sum = 0
	sumSq = 0
	for i := 1; i <= n; i++ {
		sum += i
		sumSq += i * i
	}
	fmt.Println(sum*sum - sumSq)
	fmt.Println(time.Since(startTime))
}

func main() {
	euler06()
}

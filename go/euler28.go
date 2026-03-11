// euler28 находит сумму чисел в диагоналях спирали 1001×1001.
//
// Решение задачи Эйлера №28.
package main

import (
	"fmt"
	"time"
)

func euler28() {
	n := 1001

	startTime := time.Now()
	num := 1
	result := 0
	lyr := 2
	for lyr <= n {
		for i := 0; i < 4; i++ {
			num += lyr
			result += num
		}
		lyr += 2
	}
	result++
	fmt.Println(result)
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	sum := 1
	for i := 3; i <= n; i += 2 {
		sum += 4*i*i - 6*(i-1)
	}
	fmt.Println(sum)
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	res := (4*n*n*n + 3*n*n + 8*n - 9) / 6
	fmt.Println(res)
	fmt.Println(time.Since(startTime))
}

func main() {
	euler28()
}

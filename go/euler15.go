// euler15 находит количество маршрутов в сетке 20×20.
//
// Решение задачи Эйлера №15.
package main

import (
	"fmt"
	"time"
)

var memory = make(map[[2]int]int)

func f(x, y int) int {
	key := [2]int{x, y}
	if v, ok := memory[key]; ok {
		return v
	}
	var result int
	if x == 0 {
		result = f(x, y-1)
	} else if y == 0 {
		result = f(x-1, y)
	} else {
		result = f(x-1, y) + f(x, y-1)
	}
	memory[key] = result
	return result
}

func euler15() {
	n := 20

	memory = make(map[[2]int]int)
	memory[[2]int{1, 0}] = 1
	memory[[2]int{0, 1}] = 1

	startTime := time.Now()
	fmt.Println(f(n, n))
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	counter := 1
	for i := 0; i < n; i++ {
		counter = counter * (2*n - i) / (1 + i)
	}
	fmt.Println(counter)
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	dp := make(map[[2]int]int)
	for i := 0; i <= n; i++ {
		for j := 0; j <= n; j++ {
			if i == 0 || j == 0 {
				dp[[2]int{i, j}] = 1
			} else {
				dp[[2]int{i, j}] = dp[[2]int{i - 1, j}] + dp[[2]int{i, j - 1}]
			}
		}
	}
	fmt.Println(dp[[2]int{n, n}])
	fmt.Println(time.Since(startTime))
}

func main() {
	euler15()
}

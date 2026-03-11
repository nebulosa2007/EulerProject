// euler40 находит произведение цифр числа Чамбертоуна.
//
// Решение задачи Эйлера №40.
package main

import (
	"fmt"
	"time"
)

func euler40() {
	n := 1000000

	startTime := time.Now()
	champernowne := ""
	for i := 0; i <= n; i++ {
		champernowne += fmt.Sprintf("%d", i)
	}
	positions := make([]int, 0)
	for i := 0; i < len(fmt.Sprintf("%d", n)); i++ {
		positions = append(positions, powInt(10, i))
	}
	result := 1
	for _, pos := range positions {
		if pos < len(champernowne) {
			digit := int(champernowne[pos] - '0')
			result *= digit
		}
	}
	fmt.Println(result)
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	fmt.Println(time.Since(startTime))
}

func powInt(base, exp int) int {
	result := 1
	for i := 0; i < exp; i++ {
		result *= base
	}
	return result
}

func main() {
	euler40()
}

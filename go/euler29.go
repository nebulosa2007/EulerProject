// euler29 считает количество различных членов последовательности a^b
// для 2 ≤ a ≤ 100 и 2 ≤ b ≤ 100.
//
// Решение задачи Эйлера №29.
package main

import (
	"fmt"
	"time"
)

func euler29() {
	n := 100

	startTime := time.Now()
	powers := make(map[int]bool)
	for a := 2; a <= n; a++ {
		for b := 2; b <= n; b++ {
			pow := 1
			for i := 0; i < b; i++ {
				pow *= a
			}
			powers[pow] = true
		}
	}
	fmt.Println(len(powers))
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	powers = make(map[int]bool)
	for a := 2; a <= n; a++ {
		for b := 2; b <= n; b++ {
			pow := 1
			for i := 0; i < b; i++ {
				pow *= a
			}
			powers[pow] = true
		}
	}
	fmt.Println(len(powers))
	fmt.Println(time.Since(startTime))
}

func main() {
	euler29()
}

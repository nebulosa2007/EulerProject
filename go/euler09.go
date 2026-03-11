// euler09 находит произведение abc для единственной тройки Пифагора,
// где a + b + c = 1000.
//
// Решение задачи Эйлера №9.
package main

import (
	"fmt"
	"time"
)

func euler09() {
	n := 1000

	startTime := time.Now()
	for a := 1; a < n/3; a++ {
		for b := a + 1; b < (n-a)/2; c := n - a - b; b++ {
			if a*a+b*b == c*c {
				fmt.Println(a * b * c)
			}
		}
	}
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	fmt.Println(time.Since(startTime))
}

func main() {
	euler09()
}

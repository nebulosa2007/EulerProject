// euler02 находит сумму всех четных элементов ряда Фибоначчи,
// которые не превышают четыре миллиона.
//
// Решение задачи Эйлера №2.
package main

import (
	"fmt"
	"time"
)

// fibonacci возвращает канал с числами Фибоначчи.
func fibonacci() chan int {
	ch := make(chan int)
	go func() {
		f1, f2 := 0, 1
		for {
			ch <- f1
			f1, f2 = f2, f1+f2
		}
	}()
	return ch
}

// euler02 решает задачу Эйлера №2.
//
// Находит сумму всех четных элементов ряда Фибоначчи,
// которые не превышают четыре миллиона.
func euler02() {
	n := 4_000_000

	// Вариант 1
	startTime := time.Now()
	oddFbSum := 0
	iterator := fibonacci()
	for fbNum := range iterator {
		if fbNum >= n {
			break
		}
		if fbNum%2 == 0 {
			oddFbSum += fbNum
		}
	}
	fmt.Println(oddFbSum)
	fmt.Println(time.Since(startTime))

	// Вариант 2
	startTime = time.Now()
	sum := 0
	iterator = fibonacci()
	for fbNum := range iterator {
		if fbNum >= n {
			break
		}
		if fbNum%2 == 0 {
			sum += fbNum
		}
	}
	fmt.Println(sum)
	fmt.Println(time.Since(startTime))
}

func main() {
	euler02()
}

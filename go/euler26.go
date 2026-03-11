// euler26 находит значение d < 1000, для которого 1/d содержит самую
// длинную повторяющуюся последовательность цифр.
//
// Решение задачи Эйлера №26.
package main

import (
	"fmt"
	"time"
)

func euler26() {
	n := 1000

	startTime := time.Now()
	maxPattern := ""
	for x := 1; x < n; x++ {
		pattern := repeatInside(fmt.Sprintf("%g", 1.0/float64(x))[2:])
		if len(pattern) > len(maxPattern) {
			maxPattern = pattern
		}
	}
	fmt.Println(maxPattern)
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	period := 0
	ans := make(map[int]int)
	for x := 1; x <= n; x++ {
		ans[x] = 0
		origX := x
		for x%2 == 0 {
			x /= 2
		}
		for x%5 == 0 {
			x /= 5
		}
		if x != 1 {
			for i := 1; ; i++ {
				pow := 1
				for j := 0; j < i; j++ {
					pow *= 10
				}
				if pow%x == 0 {
					period = i
					break
				}
			}
			ans[origX] = period
		}
	}

	maxPeriod := ans[1]
	denominator := 1
	for x := 1; x <= n; x++ {
		if ans[x] > maxPeriod {
			maxPeriod = ans[x]
			denominator = x
		}
	}
	fmt.Println(denominator, maxPeriod)
	fmt.Println(time.Since(startTime))
}

func repeatInside(text string) string {
	maxLen := 0
	result := ""
	for i := 0; i < len(text); i++ {
		for j := i + 1; j <= len(text); j++ {
			sub := text[i:j]
			count := 0
			idx := 0
			for idx < len(text) {
				if text[idx:idx+len(sub)] == sub {
					count++
					idx += len(sub)
				} else {
					break
				}
			}
			if count > 1 && len(sub) > maxLen {
				maxLen = len(sub)
				result = sub
			}
		}
	}
	return result
}

func main() {
	euler26()
}

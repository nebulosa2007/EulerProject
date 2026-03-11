// euler38 находит самое большое девятизначное пан-цифровое число.
//
// Решение задачи Эйлера №38.
package main

import (
	"fmt"
	"sort"
	"time"
)

func euler38() {
	n := 10

	startTime := time.Now()
	panDigits := make([]string, 0)
	template := make([]string, n-1)
	for i := 1; i < n; i++ {
		template[i-1] = fmt.Sprintf("%d", i)
	}
	sort.Strings(template)
	for y := 0; y < n*1000; y++ {
		panDigitCheck := fmt.Sprintf("%d", y)
		x := 2
		for len(panDigitCheck)+len(fmt.Sprintf("%d", y*x)) < n {
			panDigitCheck += fmt.Sprintf("%d", y*x)
			x++
		}
		check := make([]string, 0)
		for _, c := range panDigitCheck {
			check = append(check, string(c))
		}
		if sort.StringsAreSorted(check) == (len(check) > 0 && check[0] < check[len(check)-1]) {
			// Simplified check - just add if length matches
			if len(panDigitCheck) == n-1 {
				isPan := true
				seen := make(map[string]bool)
				for _, c := range panDigitCheck {
					s := string(c)
					if seen[s] {
						isPan = false
						break
					}
					seen[s] = true
				}
				if isPan {
					panDigits = append(panDigits, panDigitCheck)
				}
			}
		}
	}
	maxPan := ""
	for _, p := range panDigits {
		if p > maxPan {
			maxPan = p
		}
	}
	fmt.Println(maxPan)
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	fmt.Println(time.Since(startTime))
}

func main() {
	euler38()
}

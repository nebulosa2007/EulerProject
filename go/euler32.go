// euler32 находит сумму всех пан-цифровых произведений.
//
// Решение задачи Эйлера №32.
package main

import (
	"fmt"
	"sort"
	"time"
)

func isqrt(x int) int {
	i := 1
	for i*i <= x {
		i *= 2
	}
	y := 0
	for i > 0 {
		if (y+i)*(y+i) <= x {
			y += i
		}
		i /= 2
	}
	return y
}

func isPandigitalProduct(n int) bool {
	for i := 1; i <= isqrt(n); i++ {
		if n%i == 0 {
			temp := fmt.Sprintf("%d%d%d", n, i, n/i)
			if isPandigital(temp) {
				return true
			}
		}
	}
	return false
}

func isPandigital(s string) bool {
	if len(s) != 9 {
		return false
	}
	digits := make([]bool, 10)
	for _, c := range s {
		digit := int(c - '0')
		if digit == 0 || digits[digit] {
			return false
		}
		digits[digit] = true
	}
	for i := 1; i <= 9; i++ {
		if !digits[i] {
			return false
		}
	}
	return true
}

func euler32() {
	n := 10

	startTime := time.Now()
	panProduct := make(map[[2]int]int)
	template := make([]int, n-1)
	for i := 1; i < n; i++ {
		template[i-1] = i
	}
	sort.Ints(template)
	for a := 99; a > 1; a-- {
		for b := 9999; b > 1; b-- {
			digits := make([]int, 0)
			for _, c := range fmt.Sprintf("%d%d%d", a, b, a*b) {
				digits = append(digits, int(c-'0'))
			}
			sort.Ints(digits)
			match := true
			for i, d := range digits {
				if d != template[i] {
					match = false
					break
				}
			}
			if match {
				_, exists := panProduct[[2]int{a, b}]
				if !exists {
					panProduct[[2]int{a, b}] = a * b
				}
			}
		}
	}
	sum := 0
	seen := make(map[int]bool)
	for _, v := range panProduct {
		if !seen[v] {
			sum += v
			seen[v] = true
		}
	}
	fmt.Println(sum)
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	sum = 0
	for i := 1; i < 10000; i++ {
		if isPandigitalProduct(i) {
			sum += i
		}
	}
	fmt.Println(sum)
	fmt.Println(time.Since(startTime))
}

func main() {
	euler32()
}

// euler04 находит самый большой палиндром,
// полученный умножением двух трехзначных чисел.
//
// Решение задачи Эйлера №4.
package main

import (
	"fmt"
	"strconv"
	"time"
)

// checkPalindrom проверяет заданное число на палиндром.
func checkPalindrom(number string) bool {
	return number == reverseString(number)
}

// reverseString разворачивает строку.
func reverseString(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

// euler04 решает задачу Эйлера №4.
//
// Найдите самый большой палиндром,
// полученный умножением двух трехзначных чисел.
func euler04() {
	n := 1000
	// Вариант 1
	startTime := time.Now()
	pol := make([]int, 0)
	for i := 100; i < n; i++ {
		for j := 100; j < n; j++ {
			if checkPalindrom(strconv.Itoa(i * j)) {
				pol = append(pol, i*j)
			}
		}
	}
	maxPal := 0
	for _, p := range pol {
		if p > maxPal {
			maxPal = p
		}
	}
	fmt.Println(maxPal)
	fmt.Println(time.Since(startTime))

	// Вариант 2
	startTime = time.Now()
	maxPal = 0
	for i := 100; i < n; i++ {
		for j := 100; j < n; j++ {
			product := i * j
			if checkPalindrom(strconv.Itoa(product)) && product > maxPal {
				maxPal = product
			}
		}
	}
	fmt.Println(maxPal)
	fmt.Println(time.Since(startTime))
}

func main() {
	euler04()
}

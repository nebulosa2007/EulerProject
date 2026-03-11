// euler01 находит сумму всех чисел меньше 1000, кратных 3 или 5.
//
// Решение задачи Эйлера №1.
package main

import (
	"fmt"
	"time"
)

// reduce выполняет свертку элементов слайса
func reduce[T any, R any](slice []T, fn func(R, T) R, initial R) R {
	acc := initial
	for _, v := range slice {
		acc = fn(acc, v)
	}
	return acc
}

// filter возвращает отфильтрованный слайс
func filter[T any](slice []T, fn func(T) bool) []T {
	result := make([]T, 0)
	for _, v := range slice {
		if fn(v) {
			result = append(result, v)
		}
	}
	return result
}

// rangeToSlice преобразует диапазон в слайс
func rangeToSlice(n int) []int {
	result := make([]int, n)
	for i := 0; i < n; i++ {
		result[i] = i
	}
	return result
}

func euler01() {
	n := 1000

	// Вариант 1
	startTime := time.Now()
	total := 0
	for i := 0; i < n; i++ {
		if i%3 == 0 || i%5 == 0 {
			total += i
		}
	}
	fmt.Println(total)
	fmt.Println(time.Since(startTime))

	// Вариант 2
	startTime = time.Now()
	sum := reduce(
		filter(rangeToSlice(n), func(x int) bool { return x%3 == 0 || x%5 == 0 }),
		func(acc, x int) int { return acc + x },
		0,
	)
	fmt.Println(sum)
	fmt.Println(time.Since(startTime))
}

func main() {
	euler01()
}

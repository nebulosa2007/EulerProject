// euler08 находит наибольшее произведение тринадцати последовательных
// цифр в 1000-значном числе.
//
// Решение задачи Эйлера №8.
package main

import (
	"fmt"
	"os"
	"time"
)

func loadFileToList(namefile string) []byte {
	data, err := os.ReadFile(namefile)
	if err != nil {
		return nil
	}
	var result []byte
	for _, c := range data {
		if c >= '0' && c <= '9' {
			result = append(result, c-'0')
		}
	}
	return result
}

func multiplyNumbers(nums []byte) int {
	result := 1
	for _, n := range nums {
		result *= int(n)
	}
	return result
}

func euler08() {
	n := 13

	startTime := time.Now()
	number := loadFileToList("python/euler08.txt")
	if number == nil {
		fmt.Println("File not found")
		return
	}
	maxProd := 0
	for i := 0; i <= len(number)-n; i++ {
		prod := multiplyNumbers(number[i : i+n])
		if prod > maxProd {
			maxProd = prod
		}
	}
	fmt.Println(maxProd)
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	maxProd = 0
	for i := 0; i <= len(number)-n; i++ {
		prod := multiplyNumbers(number[i : i+n])
		if prod > maxProd {
			maxProd = prod
		}
	}
	fmt.Println(maxProd)
	fmt.Println(time.Since(startTime))
}

func main() {
	euler08()
}

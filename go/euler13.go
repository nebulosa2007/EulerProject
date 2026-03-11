// euler13 находит первые десять цифр суммы ста 50-значных чисел.
//
// Решение задачи Эйлера №13.
package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

func readMatrix(namefile string) [][]int {
	data, err := os.ReadFile(namefile)
	if err != nil {
		return nil
	}
	var matrix [][]int
	for _, line := range strings.Split(strings.TrimSpace(string(data)), "\n") {
		if line == "" {
			continue
		}
		var row []int
		for _, s := range strings.Fields(line) {
			n, _ := strconv.Atoi(s)
			row = append(row, n)
		}
		matrix = append(matrix, row)
	}
	return matrix
}

func euler13() {
	n := 10

	startTime := time.Now()
	numbers := readMatrix("python/euler13.txt")
	if numbers == nil {
		fmt.Println("File not found")
		return
	}
	sumVertical := 0
	total := 0
	for j := 1; j <= len(numbers[0]); j++ {
		for i := 0; i < len(numbers); i++ {
			sumVertical += numbers[i][len(numbers[0])-j]
		}
		total += sumVertical * powInt(10, j-1)
		sumVertical = 0
	}
	result := strconv.Itoa(total)
	if len(result) >= n {
		fmt.Println(result[:n])
	} else {
		fmt.Println(result)
	}
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
	euler13()
}

// euler42 считает количество треугольных слов в файле.
//
// Решение задачи Эйлера №42.
package main

import (
	"fmt"
	"math"
	"os"
	"strings"
	"time"
)

func figurateNumber(number int, base int) int {
	return int(((base-2)*number*number - (base-4)*number) / 2)
}

func isFigurateNumber(testNumber int, base int) bool {
	r := math.Sqrt(float64(8*(base-2)*testNumber + (base-4)*(base-4)))
	val := (r + float64(base-4)) / float64(2*base-4)
	return int(val*1000000)%1000000 == 0
}

func euler42() {
	startTime := time.Now()
	data, err := os.ReadFile("python/euler42.txt")
	if err != nil {
		fmt.Println("File not found")
		return
	}
	words := strings.Split(strings.ReplaceAll(string(data), "\"", ""), ",")
	count := 0
	for _, w := range words {
		sum := 0
		for _, c := range w {
			sum += int(c) - 64
		}
		if isFigurateNumber(sum, 3) {
			count++
		}
	}
	fmt.Println(count)
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	maxN := 0
	for _, w := range words {
		sum := 0
		for _, c := range w {
			sum += int(c) - 64
		}
		if sum > maxN {
			maxN = sum
		}
	}
	triangleNumbers := make(map[int]bool)
	for i := 1; i <= maxN; i++ {
		triangleNumbers[figurateNumber(i, 3)] = true
	}
	count = 0
	for _, w := range words {
		sum := 0
		for _, c := range w {
			sum += int(c) - 64
		}
		if triangleNumbers[sum] {
			count++
		}
	}
	fmt.Println(count)
	fmt.Println(time.Since(startTime))
}

func main() {
	euler42()
}

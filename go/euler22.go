// euler22 считает сумму очков имен в файле.
//
// Решение задачи Эйлера №22.
package main

import (
	"fmt"
	"os"
	"sort"
	"strings"
	"time"
)

func readMatrix(namefile string, mode string) []string {
	data, err := os.ReadFile(namefile)
	if err != nil {
		return nil
	}
	if mode == "text" {
		content := strings.ReplaceAll(string(data), "\"", "")
		return strings.Split(content, ",")
	}
	return nil
}

func namesPoints(names ...string) int {
	sum := 0
	for i, name := range names {
		for _, j := range name {
			sum += (int(j) - 64) * (i + 1)
		}
	}
	return sum
}

func euler22() {
	startTime := time.Now()
	names := readMatrix("python/euler22.txt", "text")
	if names == nil {
		fmt.Println("File not found")
		return
	}
	sort.Strings(names)
	fmt.Println(namesPoints(names...))
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	fmt.Println(time.Since(startTime))
}

func main() {
	euler22()
}

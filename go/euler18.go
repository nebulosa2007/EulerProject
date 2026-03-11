// euler18 находит максимальную сумму пути от вершины до основания треугольника.
//
// Решение задачи Эйлера №18.
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

func msu(rows [][]int, nLine int) int {
	for i := 0; i < len(rows[nLine]); i++ {
		maxVal := rows[nLine+1][i]
		if rows[nLine+1][i+1] > maxVal {
			maxVal = rows[nLine+1][i+1]
		}
		rows[nLine][i] += maxVal
	}
	if len(rows[nLine]) == 1 {
		return rows[nLine][0]
	}
	return msu(rows, nLine-1)
}

func euler18() {
	n := 15

	startTime := time.Now()
	matrix := readMatrix("python/euler18.txt")
	if matrix == nil {
		fmt.Println("File not found")
		return
	}
	fmt.Println(msu(matrix, n-2))
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	fmt.Println(time.Since(startTime))
}

func main() {
	euler18()
}

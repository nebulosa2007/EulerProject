// euler11 находит наибольшее произведение четырех подряд идущих чисел
// в таблице 20×20.
//
// Решение задачи Эйлера №11.
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

func productMultiply(matrix [][]int, n int) []int {
	product := make([]int, 0)
	for i := 0; i <= len(matrix[0])-n; i++ {
		for j := 0; j < len(matrix); j++ {
			num := 1
			for k := 0; k < n; k++ {
				num *= matrix[j][i+k]
			}
			product = append(product, num)
		}
	}
	return product
}

func productMultiplyDiagonals(matrix [][]int, n int) int {
	maxProduct := 0
	for x := 0; x <= len(matrix[0])-n; x++ {
		for y := 0; y <= len(matrix[0])-n; y++ {
			num := 1
			for i := 0; i < n; i++ {
				num *= matrix[x+i][y+i]
			}
			if num > maxProduct {
				maxProduct = num
			}
		}
	}
	return maxProduct
}

func euler11() {
	n := 4

	startTime := time.Now()
	matrix := readMatrix("python/euler11.txt")
	if matrix == nil {
		fmt.Println("File not found")
		return
	}
	matrixTranspose := make([][]int, len(matrix[0]))
	for i := range matrixTranspose {
		matrixTranspose[i] = make([]int, len(matrix))
	}
	for i := 0; i < len(matrix); i++ {
		for j := 0; j < len(matrix[0]); j++ {
			matrixTranspose[j][i] = matrix[i][j]
		}
	}

	maxProd := 0
	for _, p := range productMultiply(matrix, n) {
		if p > maxProd {
			maxProd = p
		}
	}
	for _, p := range productMultiply(matrixTranspose, n) {
		if p > maxProd {
			maxProd = p
		}
	}
	diag := productMultiplyDiagonals(matrix, n)
	if diag > maxProd {
		maxProd = diag
	}
	fmt.Println(maxProd)
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	maxProd = 0
	for _, p := range productMultiply(matrix, n) {
		if p > maxProd {
			maxProd = p
		}
	}
	for _, p := range productMultiply(matrixTranspose, n) {
		if p > maxProd {
			maxProd = p
		}
	}
	diag = productMultiplyDiagonals(matrix, n)
	if diag > maxProd {
		maxProd = diag
	}
	fmt.Println(maxProd)
	fmt.Println(time.Since(startTime))
}

func main() {
	euler11()
}

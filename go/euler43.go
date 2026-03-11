// euler43 находит сумму всех пан-цифровых чисел из цифр от 0 до 9.
//
// Решение задачи Эйлера №43.
package main

import (
	"fmt"
	"time"
)

func eratosfenLists(number int, dimension int) []int {
	start := 1
	if dimension > 0 {
		start = dimension
	}
	sieve := make([]int, 0)
	isComposite := make([]bool, number+1)
	for i := 2; i <= number/2; i++ {
		for j := 2 * i; j <= number; j += i {
			isComposite[j] = true
		}
	}
	for k := start; k <= number; k++ {
		if !isComposite[k] {
			sieve = append(sieve, k)
		}
	}
	return sieve
}

func euler43() {
	n := 10

	startTime := time.Now()
	panNumbers := generatePermutations10()
	panNumbersSub := make([]int, 0)
	divisors := []int{2, 3, 5, 7, 11, 13, 17}
	for _, i := range panNumbers {
		if i[0] != 0 {
			valid := true
			for y := 1; y <= len(i)-3; y++ {
				num := i[y]*100 + i[y+1]*10 + i[y+2]
				if num%divisors[y-1] != 0 {
					valid = false
					break
				}
			}
			if valid {
				num := 0
				for _, d := range i {
					num = num*10 + d
				}
				panNumbersSub = append(panNumbersSub, num)
			}
		}
	}
	sum := 0
	for _, v := range panNumbersSub {
		sum += v
	}
	fmt.Println(sum)
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	fmt.Println(time.Since(startTime))
}

func generatePermutations10() [][]int {
	arr := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	return permute10(arr)
}

func permute10(arr []int) [][]int {
	result := [][]int{}
	permute10Helper(arr, 0, &result)
	return result
}

func permute10Helper(arr []int, i int, result *[][]int) {
	if i == len(arr) {
		tmp := make([]int, len(arr))
		copy(tmp, arr)
		*result = append(*result, tmp)
	} else {
		for j := i; j < len(arr); j++ {
			arr[i], arr[j] = arr[j], arr[i]
			permute10Helper(arr, i+1, result)
			arr[i], arr[j] = arr[j], arr[i]
		}
	}
}

func main() {
	euler43()
}

// euler36 находит сумму всех чисел меньше миллиона, являющихся
// палиндромами по основаниям 10 и 2.
//
// Решение задачи Эйлера №36.
package main

import (
	"fmt"
	"time"
)

func checkPalindrom(number string) bool {
	for i := 0; i < len(number)/2; i++ {
		if number[i] != number[len(number)-1-i] {
			return false
		}
	}
	return true
}

func toBinary(n int) string {
	if n == 0 {
		return "0"
	}
	result := ""
	for n > 0 {
		result = fmt.Sprintf("%d", n%2) + result
		n /= 2
	}
	return result
}

func euler36() {
	n := 1000000

	startTime := time.Now()
	sumDbPalindromes := 0
	for i := 0; i < n; i++ {
		if checkPalindrom(fmt.Sprintf("%d", i)) {
			if checkPalindrom(toBinary(i)) {
				sumDbPalindromes += i
			}
		}
	}
	fmt.Println(sumDbPalindromes)
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	sumDbPalindromes = 0
	for i := 0; i < n; i++ {
		if checkPalindrom(fmt.Sprintf("%d", i)) && checkPalindrom(toBinary(i)) {
			sumDbPalindromes += i
		}
	}
	fmt.Println(sumDbPalindromes)
	fmt.Println(time.Since(startTime))
}

func main() {
	euler36()
}

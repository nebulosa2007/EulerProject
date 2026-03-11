// euler20 находит сумму цифр в числе 100!
//
// Решение задачи Эйлера №20.
package main

import (
	"fmt"
	"math/big"
	"time"
)

func factorialSelf(number int) int {
	if number == 0 {
		return 1
	}
	result := 1
	for i := 1; i <= number; i++ {
		result *= i
	}
	return result
}

func euler20() {
	n := 100

	startTime := time.Now()
	fact := big.NewInt(1)
	for i := 2; i <= n; i++ {
		fact.Mul(fact, big.NewInt(int64(i)))
	}
	sum := 0
	for _, c := range fact.String() {
		sum += int(c - '0')
	}
	fmt.Println(sum)
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	fact = big.NewInt(1)
	for i := 2; i <= n; i++ {
		fact.Mul(fact, big.NewInt(int64(i)))
	}
	sum = 0
	for _, c := range fact.String() {
		sum += int(c - '0')
	}
	fmt.Println(sum)
	fmt.Println(time.Since(startTime))
}

func main() {
	euler20()
}

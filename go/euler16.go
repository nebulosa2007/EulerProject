// euler16 находит сумму цифр числа 2 в степени 1000.
//
// Решение задачи Эйлера №16.
package main

import (
	"fmt"
	"math/big"
	"time"
)

func euler16() {
	n := 1000

	startTime := time.Now()
	result := big.NewInt(1)
	exp := big.NewInt(int64(n))
	base := big.NewInt(2)
	result.Exp(base, exp, nil)
	sum := 0
	for _, c := range result.String() {
		sum += int(c - '0')
	}
	fmt.Println(sum)
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	result = big.NewInt(1)
	result.Exp(base, exp, nil)
	sum = 0
	for _, c := range result.String() {
		sum += int(c - '0')
	}
	fmt.Println(sum)
	fmt.Println(time.Since(startTime))
}

func main() {
	euler16()
}

// euler48 находит последние десять цифр суммы 1^1 + 2^2 + ... + 1000^1000.
//
// Решение задачи Эйлера №48.
package main

import (
	"fmt"
	"math/big"
	"time"
)

func euler48() {
	n := 10

	startTime := time.Now()
	longNumber := big.NewInt(0)
	mod := big.NewInt(1)
	for i := 0; i < n; i++ {
		mod.Mul(mod, big.NewInt(10))
	}
	for i := 1; i <= 1000; i++ {
		exp := big.NewInt(int64(i))
		base := big.NewInt(int64(i))
		pow := big.NewInt(0)
		pow.Exp(base, exp, mod)
		longNumber.Add(longNumber, pow)
		longNumber.Mod(longNumber, mod)
	}
	fmt.Println(fmt.Sprintf("%d", longNumber))
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	result := 0
	longNumber = big.NewInt(0)
	for i := 1; i <= 1000; i++ {
		temp := big.NewInt(int64(i))
		exp := big.NewInt(int64(i))
		temp.Exp(temp, exp, mod)
		result += int(temp.Int64())
		result %= 10000000000
	}
	fmt.Println(result)
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	sum := big.NewInt(0)
	for i := 1; i <= 1000; i++ {
		exp := big.NewInt(int64(i))
		base := big.NewInt(int64(i))
		pow := big.NewInt(0)
		pow.Exp(base, exp, nil)
		sum.Add(sum, pow)
	}
	str := fmt.Sprintf("%d", sum)
	if len(str) >= n {
		fmt.Println(str[len(str)-n:])
	} else {
		fmt.Println(str)
	}
	fmt.Println(time.Since(startTime))
}

func main() {
	euler48()
}

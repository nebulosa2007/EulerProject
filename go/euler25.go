// euler25 находит порядковый номер первого числа Фибоначчи с 1000 цифрами.
//
// Решение задачи Эйлера №25.
package main

import (
	"fmt"
	"math/big"
	"time"
)

func euler25() {
	n := 1000

	startTime := time.Now()
	fbCounter := 0
	f1 := big.NewInt(0)
	f2 := big.NewInt(1)
	fbNum := big.NewInt(0)
	one := big.NewInt(1)
	ten := big.NewInt(10)
	pow := big.NewInt(int64(n - 1))
	limit := ten.Exp(ten, pow, nil)
	for {
		if fbNum.BitLen() >= n {
			break
		}
		fbCounter++
		fbNum.Add(f1, f2)
		f1, f2 = f2, fbNum
	}
	fmt.Println(fbCounter)
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	fbCounter = 0
	f1 = big.NewInt(0)
	f2 = big.NewInt(1)
	for {
		if len(f1.String()) == n {
			break
		}
		fbCounter++
		f1.Add(f1, f2)
		f1, f2 = f2, f1
	}
	fmt.Println(fbCounter)
	fmt.Println(time.Since(startTime))
}

func main() {
	euler25()
}

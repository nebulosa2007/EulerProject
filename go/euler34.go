// euler34 находит сумму всех чисел, равных сумме факториалов их цифр.
//
// Решение задачи Эйлера №34.
package main

import (
	"fmt"
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

func getPower(n int, factorialList []int) int {
	test := n - 1
	power := 1
	for factorialList[n-1]*power > test {
		test = test*10 + n - 1
		power++
	}
	return power
}

func euler34() {
	n := 10

	startTime := time.Now()
	factorialList := make([]int, n)
	for i := 0; i < n; i++ {
		factorialList[i] = factorialSelf(i)
	}
	curiousNumbers := make([]int, 0)
	upperBound := powInt(n, getPower(n, factorialList))
	for i := 3; i < upperBound; i++ {
		sumNumberList := 0
		temp := i
		for temp > 0 {
			sumNumberList += factorialList[temp%10]
			temp /= 10
		}
		if sumNumberList == i {
			curiousNumbers = append(curiousNumbers, i)
		}
	}
	sum := 0
	for _, v := range curiousNumbers {
		sum += v
	}
	fmt.Println(sum)
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	factorialList = make([]int, n)
	for i := 0; i < n; i++ {
		factorialList[i] = factorialSelf(i)
	}
	sumFactNot0 := make([]int, 10000)
	sumFact0 := make([]int, 10000)
	for i := 0; i < 10000; i++ {
		sumFactNot0[i] = factorialList[i%10]
		if i >= 10 {
			sumFactNot0[i] += factorialList[(i/10)%10]
		}
		if i >= 100 {
			sumFactNot0[i] += factorialList[(i/100)%10]
		}
		if i >= 1000 {
			sumFactNot0[i] += factorialList[i/1000]
		}
	}
	for i := 0; i < 10000; i++ {
		str := fmt.Sprintf("%04d", i)
		sumFact0[i] = factorialList[int(str[0]-'0')]
		for j := 1; j < 4; j++ {
			sumFact0[i] += factorialList[int(str[j]-'0')]
		}
	}
	upperBound = powInt(10, getPower(n, factorialList))
	sum = 0
	for i := 3; i < upperBound; i++ {
		result := 0
		for i >= 10000 {
			result += sumFact0[i%10000]
			i /= 10000
		}
		result += sumFactNot0[i]
		if result == i {
			sum += i
		}
	}
	fmt.Println(sum)
	fmt.Println(time.Since(startTime))
}

func powInt(base, exp int) int {
	result := 1
	for i := 0; i < exp; i++ {
		result *= base
	}
	return result
}

func main() {
	euler34()
}

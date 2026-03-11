// euler14 находит начальный элемент последовательности Коллатца меньше
// миллиона с самой длинной последовательностью.
//
// Решение задачи Эйлера №14.
package main

import (
	"fmt"
	"time"
)

var collatzCache = make(map[int]int)

func collatz(number int) int {
	if number == 1 {
		return 1
	}
	if v, ok := collatzCache[number]; ok {
		return v
	}
	var result int
	if number%2 == 0 {
		result = number / 2
	} else {
		result = number*3 + 1
	}
	collatzCache[number] = result
	return result
}

func collatzRecursion(number int, counter int) int {
	if number == 1 {
		return counter
	}
	if number%2 == 0 {
		return collatzRecursion(number/2, counter+1)
	}
	return collatzRecursion(3*number+1, counter+1)
}

func euler14() {
	n := 1000000

	startTime := time.Now()
	maxCounter := 2
	counter := 2
	winner := 0
	for number := 3; number < n; number++ {
		x := number
		for x != 2 {
			x = collatz(x)
			counter++
		}
		if maxCounter < counter {
			maxCounter = counter
			winner = number
		}
		counter = 2
	}
	fmt.Printf("%d : %d\n", winner, maxCounter)
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	counter = 0
	maxCounter = 0
	winner = 0
	for i := 13; i < n; i++ {
		counter = collatzRecursion(i, 1)
		if counter > maxCounter {
			winner = i
			maxCounter = counter
		}
	}
	fmt.Printf("%d : %d\n", winner, maxCounter)
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	knownCollatz := make(map[int]int)
	for i := 1; i < n; i++ {
		knownCollatz[i] = 0
	}
	maxCounter = 0
	winner = 0
	for number := 1; number < n; number++ {
		temp := number
		counter := 1
		for temp > 1 {
			temp = collatz(temp)
			if v, ok := knownCollatz[temp]; ok && v != 0 {
				counter += v
				break
			}
			counter++
		}
		knownCollatz[number] = counter
		if counter > maxCounter {
			maxCounter = counter
			winner = number
		}
	}
	fmt.Printf("%d : %d\n", winner, maxCounter)
	fmt.Println(time.Since(startTime))
}

func main() {
	euler14()
}

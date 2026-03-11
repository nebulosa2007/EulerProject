// euler17 считает количество букв для записи всех чисел от 1 до 1000.
//
// Решение задачи Эйлера №17.
package main

import (
	"fmt"
	"time"
)

var numbers = map[int]string{
	1: "one", 2: "two", 3: "three", 4: "four",
	5: "five", 6: "six", 7: "seven", 8: "eight",
	9: "nine", 10: "ten", 11: "eleven", 12: "twelve",
	13: "thirteen", 14: "fourteen", 15: "fifteen",
	16: "sixteen", 17: "seventeen", 18: "eighteen",
	19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty",
	50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty",
	90: "ninety", 100: "hundred", 1000: "thousand",
}

func numerals(number int) string {
	result := ""
	for x := 1000; x >= 100; x /= 10 {
		if number >= x {
			result += numbers[number/x] + numbers[x]
			number = number - number/x*x
		}
	}
	if result != "" && number > 0 {
		result += "and"
	}
	if number >= 20 {
		result += numbers[number/10*10]
		number = number - number/10*10
	}
	if _, ok := numbers[number]; ok {
		result += numbers[number]
	}
	return result
}

func euler17() {
	n := 1000

	startTime := time.Now()
	total := 0
	for x := 1; x <= n; x++ {
		total += len(numerals(x))
	}
	fmt.Printf("From 1 to %d sum symbols is: %d\n", n, total)
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	total = 0
	for x := 1; x <= n; x++ {
		total += len(numerals(x))
	}
	fmt.Printf("From 1 to %d sum symbols is: %d\n", n, total)
	fmt.Println(time.Since(startTime))
}

func main() {
	euler17()
}

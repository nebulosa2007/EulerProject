// euler39 находит значение p ≤ 1000 с максимальным числом
// прямоугольных треугольников.
//
// Решение задачи Эйлера №39.
package main

import (
	"fmt"
	"math"
	"time"
)

func euler39() {
	n := 1000

	startTime := time.Now()
	perimeter := make(map[int]int)
	for p := 2; p <= n; p += 2 {
		counterTriplets := 0
		for a := 1; a < p; a++ {
			for b := a; b < p-a; b++ {
				c := p - a - b
				if a*a+b*b == c*c {
					counterTriplets++
				}
			}
		}
		if counterTriplets > 0 {
			perimeter[p] = counterTriplets
		}
	}
	maxVal := 0
	maxP := 0
	for p, v := range perimeter {
		if v > maxVal {
			maxVal = v
			maxP = p
		}
	}
	fmt.Printf("%d: %d\n", maxP, maxVal)
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	perimeter = make(map[int]int)
	for a := 1; a < n/2; a++ {
		for b := a; b < n/2; b++ {
			c := math.Sqrt(float64(a*a + b*b))
			intC := int(c)
			if float64(intC) == c {
				perimeterTest := a + b + intC
				if perimeterTest <= n {
					perimeter[perimeterTest]++
				}
			}
		}
	}
	maxVal = 0
	maxP = 0
	for p, v := range perimeter {
		if v > maxVal {
			maxVal = v
			maxP = p
		}
	}
	fmt.Printf("%d: %d\n", maxP, maxVal)
	fmt.Println(time.Since(startTime))
}

func main() {
	euler39()
}

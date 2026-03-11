// euler19 считает количество воскресений на первое число месяца
// в двадцатом веке.
//
// Решение задачи Эйлера №19.
package main

import (
	"fmt"
	"time"
)

func isLeapYear(year int) bool {
	return year%400 == 0 || (year%4 == 0 && year%100 != 0)
}

func counterPrimeWeekday(year int, weeknum int) int {
	month30 := []int{4, 6, 9, 11}
	sumDays := 0
	counterPrime := 0
	for y := 1900; y <= year; y++ {
		daysMonth := make([]int, 0)
		for month := 1; month <= 12; month++ {
			if contains(month30, month) {
				daysMonth = append(daysMonth, 30)
			} else if month == 2 {
				if isLeapYear(y) {
					daysMonth = append(daysMonth, 29)
				} else {
					daysMonth = append(daysMonth, 28)
				}
			} else {
				daysMonth = append(daysMonth, 31)
			}
		}
		sumDays += sumSlice(daysMonth)
		daysMonth = nil
	}
	allDays := 0
	for _, x := range sumDays {
		allDays += x
		if (allDays+1)%weeknum == 0 {
			counterPrime++
		}
	}
	return counterPrime
}

func contains(slice []int, val int) bool {
	for _, v := range slice {
		if v == val {
			return true
		}
	}
	return false
}

func sumSlice(slice []int) int {
	total := 0
	for _, v := range slice {
		total += v
	}
	return total
}

func euler19() {
	n := 2000

	startTime := time.Now()
	fmt.Println(counterPrimeWeekday(n, 7) - counterPrimeWeekday(1900, 7))
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	counterPrime := 0
	for year := 1901; year <= n; year++ {
		for month := 1; month <= 12; month++ {
			day := firstDayOfMonth(year, month)
			if day == 6 { // Sunday (0=Monday in Python's weekday())
				counterPrime++
			}
		}
	}
	fmt.Println(counterPrime)
	fmt.Println(time.Since(startTime))
}

func firstDayOfMonth(year, month int) int {
	// Using Zeller's congruence
	if month < 3 {
		month += 12
		year--
	}
	k := year % 100
	j := year / 100
	h := (1 + (13*(month+1))/5 + k + k/4 + j/4 + 5*j) % 7
	return (h + 6) % 7
}

func main() {
	euler19()
}

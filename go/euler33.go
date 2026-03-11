// euler33 находит знаменатель произведения четырех дробей в несократимом виде.
//
// Решение задачи Эйлера №33.
package main

import (
	"fmt"
	"time"
)

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func euler33() {
	n := 100

	startTime := time.Now()
	denominatorProduct := 1
	nominatorProduct := 1
	for denominator := 10; denominator < n; denominator++ {
		for nominator := 10; nominator < denominator; nominator++ {
			if nominator%10 == 0 && denominator%10 == 0 {
				continue
			}
			nominatorStr := fmt.Sprintf("%d", nominator)
			denominatorStr := fmt.Sprintf("%d", denominator)
			common := findCommon(nominatorStr, denominatorStr)
			if len(common) > 0 {
				newNominator := removeDigits(nominatorStr, common)
				newDenominator := removeDigits(denominatorStr, common)
				if newDenominator == "0" {
					continue
				}
				newN, _ := fmt.Sscan(newNominator, newNominator)
				newD, _ := fmt.Sscan(newDenominator, newDenominator)
				if newD == 0 {
					continue
				}
				if float64(nominator)/float64(denominator) == float64(newN)/float64(newD) {
					nominatorProduct *= nominator
					denominatorProduct *= denominator
				}
			}
		}
	}
	g := gcd(nominatorProduct, denominatorProduct)
	fmt.Println(denominatorProduct / g)
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	numer := 1
	denom := 1
	for d := 10; d < n; d++ {
		for nVal := 10; nVal < d; nVal++ {
			n0 := nVal % 10
			n1 := nVal / 10
			d0 := d % 10
			d1 := d / 10
			if n1 == d0 && n0*d == nVal*d1 {
				numer *= nVal
				denom *= d
			}
			if n0 == d1 && n1*d == nVal*d0 {
				numer *= nVal
				denom *= d
			}
		}
	}
	g = gcd(numer, denom)
	fmt.Println(denom / g)
	fmt.Println(time.Since(startTime))
}

func findCommon(a, b string) []rune {
	common := make([]rune, 0)
	for _, ca := range a {
		for _, cb := range b {
			if ca == cb {
				common = append(common, ca)
			}
		}
	}
	return common
}

func removeDigits(s string, digits []rune) string {
	result := s
	for _, d := range digits {
		result = removeChar(result, d)
	}
	if result == "" {
		return "0"
	}
	return result
}

func removeChar(s string, r rune) string {
	result := ""
	for _, c := range s {
		if c != r {
			result += string(c)
		}
	}
	return result
}

func main() {
	euler33()
}

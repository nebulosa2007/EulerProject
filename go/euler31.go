// euler31 считает количество способов составить £2 монетами.
//
// Решение задачи Эйлера №31.
package main

import (
	"fmt"
	"time"
)

func numSets(n int, coins []int) int {
	if n < 0 {
		return 0
	}
	if n == 0 {
		return 1
	}
	if len(coins) == 1 {
		if n%coins[0] == 0 {
			return 1
		}
		return 0
	}
	return numSets(n-coins[0], coins) + numSets(n, coins[1:])
}

func euler31() {
	n := 200
	coins := []int{1, 2, 5, 10, 20, 50, 100, 200}

	startTime := time.Now()
	sets := make([]int, n+1)
	sets[0] = 1
	for _, coin := range coins {
		for i := 0; i <= n-coin; i++ {
			sets[i+coin] += sets[i]
		}
	}
	fmt.Println(sets[n])
	fmt.Println(time.Since(startTime))

	startTime = time.Now()
	// Reverse coins for recursive approach
	coinsReversed := make([]int, len(coins))
	for i, j := 0, len(coins)-1; i < j; i, j = i+1, j-1 {
		coinsReversed[i], coinsReversed[j] = coins[j], coins[i]
	}
	fmt.Println(numSets(n, coinsReversed))
	fmt.Println(time.Since(startTime))
}

func main() {
	euler31()
}

package main

import "fmt"

var sum int = 0
var numbers []int
var target int

func dfs(value int, index int) {
	if index == len(numbers) && value == target {
		sum += 1
	}

	if index != len(numbers) {
		dfs(value+numbers[index], index+1)
		dfs(value-numbers[index], index+1)
	}

}

func solution(numbers []int, target int) int {
	numbers = numbers
	target = target
	dfs(0, 0)
	return sum
}

func main() {

	target = 3
	numbers = []int{1, 1, 1, 1, 1}
	fmt.Println(solution(numbers, target))
}

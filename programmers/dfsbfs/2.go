package main

var (
	graph   [][]int
	visited []bool
	count   int
)

func dfs(node int) {
	visited[node] = true

	for i := 0; i < len(graph[node]); i++ {
		if graph[node][i] == 1 && !visited[i] {
			dfs(i)
		}
	}

}

func solution(n int, computers [][]int) int {
	graph = computers
	visited = make([]bool, n+1)
	for i := 0; i < n; i++ {
		if !visited[i] {
			dfs(i)
			count += 1
		}
	}

	return count
}

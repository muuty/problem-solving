package main

var (
	Begin   string
	Target  string
	Words   []string
	visited []bool
	queue   Queue
)

type Pair struct {
	word  string
	depth int
}

type Queue struct {
	items chan Pair
}

// 값을 저장
func (q *Queue) Set(value Pair) {
	q.items <- value
} // 값을 꺼내기
func (q *Queue) Get() Pair {
	return <-q.items
}

func bfs(pair Pair) int {
	if Target == pair.word {
		return pair.depth
	}

}

func solution(begin string, target string, words []string) int {
	return 0
}

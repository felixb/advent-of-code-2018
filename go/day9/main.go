package main

import (
	"container/ring"
	"fmt"
	"io/ioutil"
	"os"
	"strconv"
	"strings"
)

func readInput() string {
	bytes, _ := ioutil.ReadAll(os.Stdin)
	return string(bytes)
}

func parse(input string, factor int) (int, int) {
	parts := strings.Split(input, " ")
	players, _ := strconv.Atoi(parts[0])
	marbles, _ := strconv.Atoi(parts[6])
	return players, marbles * factor
}

func initScores(players int) map[int]int {
	scores := make(map[int]int)
	for i := 0; i < players; i++ {
		scores[players] = 0
	}
	return scores
}

// initial ring with 3 marbles: 0->2->1
func initRing() (*ring.Ring, *ring.Ring) {
	first := ring.New(3)
	first.Value = 0
	r := first.Next()
	r.Value = 2
	r.Next().Value = 1
	return first, r
}

func inset(r *ring.Ring, marble int) *ring.Ring {
	m := ring.New(1)
	m.Value = marble
	r.Link(m)
	return m
}

func highscore(scores map[int]int) int {
	highscore := 0
	for _, v := range scores {
		if v > highscore {
			highscore = v
		}
	}
	return highscore
}

func run(players, marbles int) int {
	scores := initScores(players)
	_, r := initRing()

	for i := 3; i < marbles; i++ {
		player := i % players
		if i%23 == 0 {
			r = r.Prev().Prev().Prev().Prev().Prev().Prev().Prev().Prev()
			removed := r.Unlink(1)
			r = r.Next()
			scores[player] += i + removed.Value.(int)
		} else {
			r = inset(r.Next(), i)
		}

		//r0.Do(func(p interface{}) {
		//	fmt.Printf("%d ", p.(int))
		//})
		//fmt.Println()
	}

	return highscore(scores)
}

func main() {
	if os.Args[1] == "1" {
		fmt.Println(run(parse(readInput(), 1)))
	} else {
		fmt.Println(run(parse(readInput(), 100)))
	}
}

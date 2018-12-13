(ns aoc2018.day12-test
  (:use clojure.test
        clojure.string
        aoc2018.day12))

(testing
  "day 12"
  (testing "variant 1"

    (is (= (eval-state "#" 0) 0))
    (is (= (eval-state "#.#.#" 0) 6))
    (is (= (eval-state "#" 1) 1))
    (is (= (eval-state ".#" 0) 1))
    (is (= (eval-state "..##" -1) 3))

    (is (= (next-state "#.."
                       {"..#.." "#"}
                       0)
           ["#" 0]))
    (is (= (next-state "..##.."
                       {"..#.." "#"
                        ".##.." "#"}
                       0)
           ["#" 3]))

    (let [lines ["initial state: #..#.#..##......###...###"
                 ""
                 "...## => #"
                 "..#.. => #"
                 ".#... => #"
                 ".#.#. => #"
                 ".#.## => #"
                 ".##.. => #"
                 ".#### => #"
                 "#.#.# => #"
                 "#.### => #"
                 "##.#. => #"
                 "##.## => #"
                 "###.. => #"
                 "###.# => #"
                 "####. => #"]
          input (clojure.string/join "\n" lines)]
      (is (= (run1 input) 325)))
    )
  )

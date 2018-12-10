(ns aoc2018.day9-test
  (:use clojure.test
        clojure.string
        aoc2018.day9))

(testing
  "day 9"
  (testing "variant 1"
    (is (= (run1 "9 players; last marble is worth 25 points") 32))
    (is (= (run1 "10 players; last marble is worth 1618 points") 8317))
    (is (= (run1 "13 players; last marble is worth 7999 points") 146373))
    (is (= (run1 "17 players; last marble is worth 1104 points") 2764))
    (is (= (run1 "21 players; last marble is worth 6111 points") 54718))
    (is (= (run1 "30 players; last marble is worth 5807 points") 37305))
    )
  )

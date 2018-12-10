(ns aoc2018.day8-test
  (:use clojure.test
        clojure.string
        aoc2018.day8))

(testing
  "day 8"
  (testing "variant 1"
    (is (= 99 (run1 "0 1 99")))
    (is (= 33 (run1 "0 3 10 11 12")))
    (is (= 138 (run1 "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2")))
    ))

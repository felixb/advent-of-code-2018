(ns aoc2018.day1-test
  (:use clojure.test
        aoc2018.day1))

(testing
  "day 1"
  (testing "variant 1"
    (is (= 3 (run1 "+1\n-2\n+3\n+1")))
    (is (= 3 (run1 "+1\n+1\n+1")))
    (is (= 0 (run1 "+1\n+1\n-2")))
    (is (= -6 (run1 "-1\n-2\n-3"))))

  (testing "variant 2"
    (is (= 0 (run2 "+1\n-1")))
    (is (= 10 (run2 "+3\n+3\n+4\n-2\n-4")))
    (is (= 5 (run2 "-6\n+3\n+8\n+5\n-6")))
    (is (= 14 (run2 "+7\n+7\n-2\n-7\n-4"))))
  )
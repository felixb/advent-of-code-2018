(ns aoc2018.day11-test
  (:use clojure.test
        clojure.string
        aoc2018.day11))

(testing
  "day 11"
  (testing "variant 1"

    (is (= (power 8 3 5) 4))
    (is (= (power 57 122 79) -5))
    (is (= (power 39 217 196) 0))
    (is (= (power 71 101 153) 4))

    (is (= (power-of-sqare (create-grid 18) 3 33 45) 29))

    (is (= (run1 "18") "33,45"))
    (is (= (run1 "42") "21,61"))
    )

  ;(testing "variant 2"
  ;  (is (= (run2 "18") "90,269,16"))
  ;  (is (= (run2 "42") "232,251,12"))
  ;  )
  )

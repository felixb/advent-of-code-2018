(ns aoc2018.day7-test
  (:use clojure.test
        clojure.string
        aoc2018.day7))

(testing
  "day 7"
  (testing "variant 1"
    (let [input (join "\n"
                      ["Step C must be finished before step A can begin."
                       "Step C must be finished before step F can begin."
                       "Step A must be finished before step B can begin."
                       "Step A must be finished before step D can begin."
                       "Step B must be finished before step E can begin."
                       "Step D must be finished before step E can begin."
                       "Step F must be finished before step E can begin."])]
      (is (= "CABDFE" (run1 input)))))

  (testing "variant 2"
    (is (= (step-duration "A" 0) 1))
    (is (= (step-duration "Z" 0) 26))
    (is (= (step-duration "A" 60) 61))
    (is (= (step-duration "Z" 60) 86))

    (is (empty? (get-ready-workers {} 0)))
    (is (empty? (get-ready-workers {0 {:id 0 :next-free 1}} 0)))
    (is (=
          [{:id 0 :next-free 1}]
          (get-ready-workers {0 {:id 0 :next-free 1}} 1)))
    (is (=
          [{:id 0 :next-free 0} {:id 1 :next-free 1}]
          (get-ready-workers {0 {:id 0 :next-free 0}
                              1 {:id 1 :next-free 1}
                              2 {:id 2 :next-free 2}}
                             1)))

    (is (= ["A"] (get-steps-in-progress {0 {:last-step "A"
                                            :next-free 5}
                                         1 {:last-step "B"
                                            :next-free 1}}
                                        3)))


    (let [input (join "\n"
                      ["Step C must be finished before step A can begin."
                       "Step C must be finished before step F can begin."
                       "Step A must be finished before step B can begin."
                       "Step A must be finished before step D can begin."
                       "Step B must be finished before step E can begin."
                       "Step D must be finished before step E can begin."
                       "Step F must be finished before step E can begin."])]
      (is (= 15 (run2 input 0 2))))
    ))
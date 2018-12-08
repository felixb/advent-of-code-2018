(ns aoc2018.day1
  (:use clojure.string))

(defn parse [input]
  (map (fn [s] (Integer/parseInt s)) (split-lines input)))

(defn run1 [input]
  (reduce + (parse input)))

(defn run2 [input]
  (let [input (parse input)
        len (count input)]
    (loop [i 0
           sum 0
           freqs (set '())]
      (if (freqs sum)
        sum
        (recur
          (mod (+ i 1) len)
          (+ sum (nth input i))
          (conj freqs sum))))))

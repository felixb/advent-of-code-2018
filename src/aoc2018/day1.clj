(ns aoc2018.day1
  (:use clojure.string))

(defn parse [input]
  (map (fn [s] (Integer/parseInt s)) (split-lines input)))

(defn run1 [input]
  (reduce + input))

(defn run2 [input]
  (let [len (count input)]
    (loop [i 0
           sum 0
           freqs (set '())]
      (if (freqs sum)
        sum
        (recur
          (mod (+ i 1) len)
          (+ sum (nth input i))
          (conj freqs sum))))))

(defn run [variant input]
  (let [parsed (parse input)]
    (if (= 1 variant)
      (run1 parsed)
      (run2 parsed))))

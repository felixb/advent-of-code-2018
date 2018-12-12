(ns aoc2018.day12
  (:require [clojure.set])
  (:require [clojure.string]))

(defn parse-pattern [line]
  (let [parts (clojure.string/split line #" ")]
    [(first parts) (nth parts 2)]))

(defn parse [input]
  (let [lines (clojure.string/split-lines input)
        initial-state (nth (clojure.string/split (first lines) #" ") 2)
        patterns (into {} (map parse-pattern (rest (rest lines))))]
    [initial-state patterns]))

(defn next-position [state patterns i]
  (let [start (- i 2)
        end (+ i 3)]
    (if (or (< start 0) (> end (count state)))
      "."
      (let [s (subs state start end)]
        (get patterns s ".")))))

(defn next-state [state patterns]
  (apply str (map (partial next-position state patterns) (range (count state)))))

(defn eval-position [state first-index i]
  (let [real-index (+ first-index i)
        p (str (nth state i))]
    (* real-index (if (= p "#")
                    1
                    0))))

(defn eval-state [state first-index]
  (apply + (map (partial eval-position state first-index) (range (count state)))))

(defn run1 [input]
  (let [[initial-state patterns] (parse input)
        state (str "........................................" initial-state "........................................")]
    (loop [i 0
           state state]
      (if (= i 20)
        (eval-state state -40)
        (recur (inc i) (next-state state patterns))))))

(defn run2 [input]
  0)
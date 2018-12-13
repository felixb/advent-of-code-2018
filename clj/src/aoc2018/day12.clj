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

(defn next-state [state patterns first-index]
  (let [first-index (- first-index 5)
        state (str "....." (clojure.string/replace state #"\.*$" "....."))
        state (clojure.string/replace (apply str (map (partial next-position state patterns) (range (count state)))) #"\.*$" "")
        orig-state-length (count state)
        state (clojure.string/replace state #"^\.*" "")
        new-state-length (count state)
        first-index (+ first-index (- orig-state-length new-state-length))]
    [state first-index]))

(defn eval-position [state first-index i]
  (let [real-index (+ first-index i)
        p (str (nth state i))]
    (* real-index (if (= p "#")
                    1
                    0))))

(defn eval-state [state first-index]
  (apply + (map (partial eval-position state first-index) (range (count state)))))

(defn length-of-loop [generations old-generation new-generation old-first-index new-first-index]
  (if (some? old-generation)
    (let [length-of-loop (- new-generation old-generation)]
      (if (> generations (+ new-generation length-of-loop))
        (do
          (println "generation:" old-generation "->" new-generation
                   "first-index" old-first-index "->" new-first-index
                   "length:" length-of-loop)
          length-of-loop)))
    nil))

(defn run [input generations]
  (let [[initial-state patterns] (parse input)]
    (loop [i 0
           states {}
           state initial-state
           first-index 0]
      ;(if (or (zero? i) (= i generations) (zero? (mod i 1000)))
      ;  (println i first-index ":" state))
      (if (= i generations)
        (eval-state state first-index)
        (let [[generation-with-same-state old-first-index] (get states state)
              loop-length (length-of-loop generations generation-with-same-state i old-first-index first-index)]
          (if (some? loop-length)
            (let [index-loop (- first-index old-first-index)
                  new-i (+ i loop-length)
                  new-first-index (+ first-index index-loop)]
              (recur new-i states state new-first-index))
            (let [states (assoc states state [i first-index])
                  [new-state first-index] (next-state state patterns first-index)]
              (recur (inc i) states new-state first-index))))))))

(defn run1 [input]
  (run input 20))

(defn run2 [input]
  (run input 50000000000))
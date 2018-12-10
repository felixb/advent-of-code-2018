(ns aoc2018.day8
  (:require [clojure.set])
  (:require [clojure.string]))

(defn parse [input]
  (map #(Integer/parseInt %1) (clojure.string/split input #" ")))

(defn new-reader [input]
  {:position 0
   :sum      0
   :stack    []
   :input    input
   :length   (count input)})

(defn finished? [reader]
  (>= (:position reader) (:length reader)))

(defn dec-stack [stack]
  (if (empty? stack)
    stack
    (let [top (peek stack)
          num-children (dec (first top))
          num-fields (second top)]
      (conj (pop stack) [num-children num-fields]))))

(defn peek-reader [reader]
  (peek (:stack reader)))

(defn read-meta-data [reader]
  (let [num-fields (second (peek-reader reader))
        start (:position reader)
        end (+ start num-fields)
        sum (apply + (map #(nth (:input reader) %1) (range start end)))
        stack (dec-stack (pop (:stack reader)))]
    (assoc reader
      :sum (+ (:sum reader) sum)
      :position (+ start num-fields)
      :stack stack)))

(defn read-header [reader]
  (let [input (:input reader)
        position (:position reader)
        header [(nth input position) (nth input (inc position))]]
    (assoc reader
      :stack (conj (:stack reader) header)
      :position (+ (:position reader) 2))))

(defn children? [reader]
  (> (first (peek-reader reader)) 0))

(defn read-next [reader]
  (if (or (empty? (:stack reader)) (children? reader))
    (read-header reader)
    (read-meta-data reader)))

(defn run1 [input]
  (let [input (parse input)]
    (loop [reader (new-reader input)]
      (if (finished? reader)
        (:sum reader)
        (recur (read-next reader))))))

(defn run2 [input]
  0)
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
    (let [top (peek stack)]
      (conj (pop stack) (assoc top :num-children (dec (:num-children top)))))))

(defn peek-reader [reader]
  (peek (:stack reader)))

(defn read-meta-data [reader]
  (let [num-fields (:num-fields (peek-reader reader))
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
        header {:num-children (nth input position)
                :num-fields   (nth input (inc position))}]
    (assoc reader
      :stack (conj (:stack reader) header)
      :position (+ (:position reader) 2))))

(defn children? [reader]
  (> (:num-children (peek-reader reader)) 0))

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
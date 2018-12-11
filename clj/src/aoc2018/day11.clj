(ns aoc2018.day11
  (:require [clojure.set])
  (:require [clojure.string]))

(defn parse [input]
  (Integer/parseInt (clojure.string/trim input)))

(defn power [sn x y]
  (let [rackid (+ 10 x)]
    (- (mod (int (/ (* rackid (+ sn (* rackid y))) 100)) 10) 5)))

(defn grid-key [x y]
  (str x "," y))

(defn square-power [sn x y]
  (+ (power sn x y) (power sn (+ x 1) y) (power sn (+ x 2) y)
     (power sn x (+ y 1)) (power sn (+ x 1) (+ y 1)) (power sn (+ x 2) (+ y 1))
     (power sn x (+ y 2)) (power sn (+ x 1) (+ y 2)) (power sn (+ x 2) (+ y 2))))

(defn create-point [sn x y]
  {(grid-key x y) (square-power sn x y)})

(defn create-row [sn x]
  (map #(create-point sn x %) (range 1 298)))

(defn max-square [e1 e2]
  (if (> (first (vals e1)) (first (vals e2)))
    e1
    e2))

(defn best-square [sn]
  (reduce max-square (flatten (map (partial create-row sn) (range 1 298)))))

(defn run1 [input]
  (let [sn (parse input)
        best (best-square sn)]
    (first (keys best))))

(defn run2 [input]
  "")
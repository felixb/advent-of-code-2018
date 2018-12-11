(ns aoc2018.day11
  (:require [clojure.set])
  (:require [clojure.string]))

(defn parse [input]
  (Integer/parseInt (clojure.string/trim input)))

(defn power [sn x y]
  (let [rackid (+ 10 x)]
    (- (mod (int (/ (* rackid (+ sn (* rackid y))) 100)) 10) 5)))

(defn grid-key
  ([x y]
   (grid-key x y "-"))
  ([x y l]
   (str x "," y "," l)))

(defn lookup [grid x y]
  (get grid (grid-key x y)))

(defn power-of-row [grid l x y]
  (apply + (map (partial lookup grid x) (range y (+ y l)))))

(defn power-of-sqare [grid l x y]
  (apply + (map #(power-of-row grid l % y) (range x (+ x l)))))

(defn create-point [sn x y]
  {(grid-key x y) (power sn x y)})

(defn create-row [sn x]
  (reduce merge (pmap (partial create-point sn x) (range 1 301))))

(defn create-grid [sn]
  (reduce merge (map (partial create-row sn) (range 1 301))))

(defn create-square [grid l x y]
  {(grid-key x y l) (power-of-sqare grid l x y)})

(defn max-square [e1 e2]
  (if (> (first (vals e1)) (first (vals e2)))
    e1
    e2))

(defn max-square-debug [e1 e2]
  (println e1 "vs" e2)
  (if (> (first (vals e1)) (first (vals e2)))
    e1
    e2))

(defn best-row [grid l x]
  (reduce max-square (pmap (partial create-square grid l x) (range 1 (- 301 l)))))

(defn best-square [grid l]
  (reduce max-square-debug (map (partial best-row grid l) (range 1 (- 301 l)))))

(defn run1 [input]
  (let [sn (parse input)
        grid (create-grid sn)
        best (best-square grid 3)
        sq (first (keys best))
        parts (clojure.string/split sq #",")]
    (str (first parts) "," (second parts))))

(defn best-size [grid]
  (reduce max-square-debug (map (partial best-square grid) (range 1 300))))

(defn run2 [input]
  (let [sn (parse input)
        grid (create-grid sn)
        best (best-size grid)
        sq (first (keys best))]
    sq))
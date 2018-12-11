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

(defn create-items-of-work-for-row [l x]
  (map (fn [y] [x y l]) (range 1 (- 301 l))))

(defn create-items-of-work [l]
  (apply concat (map (partial create-items-of-work-for-row l) (range 1 (- 301 l)))))

(defn create-items-of-work-for-all-sizes []
  (apply concat (map create-items-of-work (range 1 300))))

(defn power-of-item [grid [x y l]]
  [(grid-key x y l) (power-of-sqare grid l x y)])

(defn max-square [e1 e2]
  (if (> (second e1) (second e2))
    e1
    (do
      (println "current best choice:" (first e2) "with power" (second e2))
      e2)))

(defn eval-items [grid items]
  (reduce max-square (pmap (partial power-of-item grid) items)))

(defn run1 [input]
  (let [sn (parse input)
        grid (create-grid sn)
        items (create-items-of-work 3)
        best (eval-items grid items)
        sq (first best)
        parts (clojure.string/split sq #",")]
    (str (first parts) "," (second parts))))

(defn run2 [input]
  (let [sn (parse input)
        grid (create-grid sn)
        items (create-items-of-work-for-all-sizes)
        best (eval-items grid items)
        sq (first (keys best))]
    sq))
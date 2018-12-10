(ns aoc2018.day9
  (:require [clojure.set])
  (:require [clojure.string]))

(defn parse [input factor]
  (let [parts (clojure.string/split input #" ")]
    {:num-players   (Integer/parseInt (first parts))
     :last-marble   (* (Integer/parseInt (nth parts 6)) factor)
     :field         '(0 2 1)
     :position      1
     :next-player   3
     :next-marble   3
     :player-scores {0 0}}))

(defn finished? [state]
  (> (:next-marble state) (:last-marble state)))

(defn high-score [state]
  (apply max (map second (:player-scores state))))

(defn place-marble [state]
  (let [next-marble (:next-marble state)
        next-player (:next-player state)
        num-marbles (count (:field state))
        position (inc (mod (inc (:position state)) num-marbles))
        parts (split-at position (:field state))]
    (if (zero? (mod next-marble 23))
      (let [player-score (get (:player-scores state) next-player 0)
            position (mod (- position 9) num-marbles)
            parts (split-at position (:field state))
            removed-marble (first (second parts))]
        (assoc state :next-player (mod (inc next-player) (:num-players state))
                     :next-marble (inc next-marble)
                     :position position
                     :player-scores (assoc (:player-scores state) next-player (+ player-score next-marble removed-marble))
                     :field (concat (first parts) (rest (second parts)))))
      (assoc state :field (concat (first parts) [next-marble] (second parts))
                   :position position
                   :next-player (mod (inc next-player) (:num-players state))
                   :next-marble (inc next-marble)))))

(defn run1 [input]
  (loop [state (parse input 1)]
    ;(println state)
    (if (finished? state)
      (high-score state)
      (recur (place-marble state)))))

(defn run2 [input]
  (loop [state (parse input 100)]
    ;(println state)
    (if (finished? state)
      (high-score state)
      (recur (place-marble state)))))
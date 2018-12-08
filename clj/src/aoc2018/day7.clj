(ns aoc2018.day7
  (:require [clojure.set])
  (:require [clojure.string]))

(defn parse-line [line]
  (let
    [parts (clojure.string/split line #" ")]
    [(nth parts 1) (nth parts 7)]))

(defn is-req? [step req]
  (= step (second req)))

(defn find-reqs [step reqs]
  (map first (filter (fn [req] (is-req? step req)) reqs)))

(defn has-no-preds? [step steps reqs]
  (let [step-reqs (find-reqs step reqs)]
    (not-any? (set steps) step-reqs)))

(defn with-no-reqs
  ([steps reqs]
   (filter (fn [step] (has-no-preds? step steps reqs)) steps))
  ([steps-in-progress remaining-steps reqs]
   (filter (fn [step] (has-no-preds? step (concat steps-in-progress remaining-steps) reqs)) remaining-steps)))

(defn all-but [step steps]
  (remove (partial = step) steps))

(defn parse [input]
  (map parse-line (clojure.string/split-lines input)))

(defn run1 [input]
  (let [reqs (parse input)
        all-steps (sort (into [] (clojure.set/union (set (map first reqs)) (set (map second reqs)))))]
    (loop [result ""
           steps all-steps]
      (if (empty? steps)
        result
        (let [next-step (first (with-no-reqs steps reqs))
              other-steps (all-but next-step steps)]
          (recur (str result next-step) other-steps))))))

(defn step-duration [step offset]
  (+ (- (Character/codePointAt step 0) 64) offset))

(defn create-worker [id]
  {id
   {:id        id
    :next-free 0
    :last-step ""}})

(defn create-workers [count]
  (reduce merge (map create-worker (range count))))

(defn get-ready-workers [workers clock]
  (filter (fn [w] (<= (:next-free w) clock)) (map second workers)))

(defn get-steps-in-progress [workers clock]
  (map :last-step (filter (fn [w] (> (:next-free w) clock)) (map second workers))))

(defn process [workers worker-id step clock offset]
  (assoc workers worker-id {:id        worker-id
                            :next-free (+ clock (step-duration step offset))
                            :last-step step}))

(defn run2
  ([input]
   (run2 input 60 5))
  ([input offset num-worker]
   (let [reqs (parse input)
         all-steps (sort (into [] (clojure.set/union (set (map first reqs)) (set (map second reqs)))))]
     (loop [workers (create-workers num-worker)
            clock 0
            remaining-steps all-steps]
       (let [ready-workers (get-ready-workers workers clock)
             steps-in-progress (get-steps-in-progress workers clock)]
         (if (and (empty? steps-in-progress) (empty? remaining-steps))
           clock
           (let [finished-steps (map (fn [w] (:last-step w)) ready-workers)
                 remaining-steps (remove (set finished-steps) remaining-steps)]
             (if (empty? ready-workers)
               (recur workers (+ clock 1) remaining-steps)
               (let [next-step (first (with-no-reqs steps-in-progress remaining-steps reqs))]
                 (if (some? next-step)
                   (let [worker (first ready-workers)
                         workers (process workers (:id worker) next-step clock offset)
                         remaining-steps (all-but next-step remaining-steps)]
                     (recur workers clock remaining-steps))
                   (recur workers (+ clock 1) remaining-steps)))))))))))
(ns aoc2018.core
  (:require [aoc2018.day7]))

(defn -main
  [& args]
  (let
    [day (symbol (apply str "aoc2018.day" (first args)))
     variant (Integer/parseInt (second args))
     input (slurp *in*)]
    (println ((ns-resolve day (symbol "run")) variant input))))

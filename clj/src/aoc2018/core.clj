(ns aoc2018.core
  (:require [aoc2018.day1])
  (:require [aoc2018.day7])
  (:require [aoc2018.day8])
  (:require [aoc2018.day9])
  (:require [aoc2018.day11])
  )

(defn -main
  [& args]
  (let
    [day (symbol (apply str "aoc2018.day" (first args)))
     variant (Integer/parseInt (second args))
     run (symbol (str "run" variant))
     input (slurp *in*)]
    (println ((ns-resolve day run) input))))

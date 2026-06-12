

(deftemplate problema
   (slot categoria))

(deftemplate solucion
   (slot causa)
   (slot recomendacion))

; =========================
; REGLAS
; =========================

(defrule problema-fuente
   (problema (categoria sin_energia))
   =>
   (assert
      (solucion
         (causa "Fuente de poder dañada")
         (recomendacion "Revisar cable y fuente"))))

(defrule problema-video
   (problema (categoria sin_video))
   =>
   (assert
      (solucion
         (causa "RAM o tarjeta gráfica")
         (recomendacion "Limpiar RAM y revisar monitor"))))

(defrule problema-ram
   (problema (categoria problema_ram))
   =>
   (assert
      (solucion
         (causa "RAM mal colocada")
         (recomendacion "Retirar y reinstalar RAM"))))

# MCOC2020-P2

FUNCIÓN REDISEÑAR:

En esta función se tomaron los dos posibles casos (trancción y compresión).

Para el diseño en tracción se diseñó pensando en tener una barra de seccion completa, es decir t = R. El cálculo del radio fue bastante simple ya que simplemente se busco un área que satisfaga las condiciones de diseño. En base a esta área se calculó el radio.

Para el diseño en compresión, como no habian limitantes en el problema se supuso un espesor de 1 mm. A continuacion se prosigió encontrando el radio de la forma que se vio en clases. El radio se encontró con la siguente ecuación:

    Solve[l^2 *(r^2 - (r - t)^2) - 300^2 /4 *(r^4 - (r - t)^4) == 0 && t > 0 && r > t && l > r, {r}] 
    --> el 300 viene de la esbeltez
    
El resultado de la ecuacion anterior para r es :  

    {{r -> ConditionalExpression[t/2 + Sqrt[l^2 - 11250 t^2]/(150 Sqrt[2]), t > 0 && l > 150 t]}}

Por último se revisó que la tensión de cada barra no sea mayor a la tensión admisible del acero.

FACTORES DE UTILIZACIÓN NUEVOS Y PESO:

Se puede ver que para las piezas en tracción se logran FUs iguales a uno. Pero que esto no es posible para el caso a compresión, es más si se quiere tener valores cercanos a uno en compresion habría que incumplir el criterio de Esbeltez <= 300. Al tener valores menores que uno es posibble utilizar aceros de menor resistencia (más economicos y más livianos).

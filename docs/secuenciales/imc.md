# Índice de Masa Corporal (IMC)

El Índice de Masa Corporal (IMC) de una persona se calcula dividiendo la masa (peso) en kilogramos, entre la altura (en metros) elevada al cuadrado: $IMC = \text{masa}/\text{altura}^2 \, [\text{kg}/\text{m}^2]$.
Queremos un programa para calcular el $IMC$ de una persona a partir de su peso expresado en libras y su altura expresada como una combinación de pies y pulgadas.

* $1 \,[\text{ft}] = 0.3048 \, [\text{m}]$
* $1 \,[\text{in}] = 0.0254 \, [\text{m}]$
* $1\,[\text{lb}] = 0.45359237 \, [\text{kg}]$

??? danger "Solución"
    ```python
    --8<-- ";python/secuenciales/imc.py"
    ```
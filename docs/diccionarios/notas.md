# Notas

Suponga que tiene un `string` con el siguiente formato:

```
datos = "nombre1 apellido1:curso1=nota1,curso2=nota2;nombre2 apellido2:curso1=nota1;..."
```

De antemano no se sabe cuántos estudiantes aparecen en el texto, ni cuántos cursos asociados tiene cada uno, podría incluso no tener ninguno.

Necesitamos crear la función `obtener_datos(notas)` que permita recibir un texto con ese formato y devolver un diccionario con la siguiente estructura:

```
{
    'nombre1 apellido1': [
        [nota1, curso1],
        [nota2, curso2],
    ],
    'nombre2 apellido2': [
        [nota1, curso1]
    ],
    #...
}
```

La lista con las notas para cada estudiante debe estar ordenada de menor a mayor de acuerdo a sus notas.

## Ejemplos

```
datos = "Carlos Pérez:cálculo=85,física=92;María González:programación=74;José Ramírez:mecánica=68,cálculo=95,álgebra=81;Ana Torres:termodinámica=77,química=88,electricidad=91"

>>> obtener_notas(datos)
{
    'Carlos Pérez': [[85, 'cálculo'], [92, 'física']], 
    'María González': [[74, 'programación']], 
    'José Ramírez': [[68, 'mecánica'], [81, 'álgebra'], [95, 'cálculo']], 
    'Ana Torres': [[77, 'termodinámica'], [88, 'química'], [91, 'electricidad']]
}
```

```
datos = "Carlos Pérez:cálculo=85,física=92;María González:programación=74;José Ramírez:mecánica=68,cálculo=95,álgebra=81;Ana Torres:termodinámica=77,química=88,electricidad=91"

>>> obtener_notas(datos)
{
    'Luis Martínez': [[85, 'geografía'], [90, 'historia']], 
    'Sofía López': [[79, 'física'], [88, 'biología'], [92, 'química']], 
    'Miguel Sánchez': [[95, 'matemáticas']]
}
```



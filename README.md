# Analizador Sintáctico con Árbol de Derivación

Este proyecto implementa un analizador sintáctico en Python para la gramática de expresiones simples dada en la presentación 05.  
El programa construye e imprime el árbol de sintaxis de cada cadena de entrada válida utilizando NetworkX.  

---

## Gramática utilizada

```
E -> E opsuma T
E -> T
T -> T opmul F
F -> F
F -> id
F -> num
F -> pari E pard
```

Donde:
- `opsuma` corresponde al operador **+**  
- `opmul` corresponde al operador **\***  
- `pari` corresponde al símbolo **(**  
- `pard` corresponde al símbolo **)**  
- `num` corresponde a un número entero  

-> la gramática no define el operador `-` ni `/`, por lo tanto cualquier cadena que los contenga será inválida.

---

## Archivos

- `programa.py` → Código principal del analizador.  
- `gra.txt` → Archivo de gramática (no se usa directamente, la gramática está fija en el código).  
- `cadenas.txt` → Archivo de prueba con las cadenas a analizar.  

Ejemplo de `cadenas.txt`:

```
2+3*4
2+3-4
2+3*(4-5)
(2+1)*3+5
```

---

## Uso

Desde consola ejecutar:

```bash
python programa.py gra.txt cadenas.txt
```

---

## ✅ Ejemplo de salida

### Entrada:
```
2+3*4
```

### Resultado:
- En consola:
```
Analizando cadena: 2+3*4
```

- Se abre una ventana con el árbol de derivación sintáctico generado con `NetworkX`.

---

## Cadenas inválidas

Ejemplos de cadenas que se consideran inválidas:

```
2-3+4   # '-' no está definido en la gramática
4/2+1   # '/' no está definido en la gramática
2++3    # error de sintaxis
```

En consola se muestra:
```
Analizando cadena: 2-3+4
Cadena inválida: 2-3+4
```
y **no se grafica nada**.

--- 

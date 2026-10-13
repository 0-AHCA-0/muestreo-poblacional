# Evaluación — Laboratorio: clasificación de variables y población vs. muestra

**Puntaje total:** 100 puntos (+5 de bonus) · **Nota del laboratorio:** puntos/100 × 20 (escala de 20)
**Peso en la materia:** Laboratorios = 20% del curso (este laboratorio ≈ 1.67%)

---

## Rúbrica

| # | Criterio | Pts | Logrado (100%) | Parcial (50%) | No logrado (0) |
|---|---|---|---|---|---|
| 1 | **Clasificación de las 7 variables (Parte A)** | 20 | Las 7 variables clasificadas correctamente y justificadas con el criterio (continuidad, orden), incluida `satisfaccion` como ordinal y la discusión de `edad` | Clasificación correcta sin justificación, o 1–2 errores | Clasificación ausente o con errores de criterio (p. ej. `satisfaccion` numérica sin discusión) |
| 2 | **Verificación en código (Parte A)** | 10 | `dtypes`/`str` y valores únicos reportados **e interpretados**; declara el orden con factor ordenado / `CategoricalDtype` | Verificación presente sin interpretación o sin declarar el orden | No se reporta |
| 3 | **Población, muestra y parámetro (Parte B)** | 10 | Identifica N = 400 como población, calcula el parámetro (1330.72) y justifica por qué se muestrea | Conceptos correctos con errores de cálculo | No distingue población de muestra |
| 4 | **Los tres diseños implementados (Parte B)** | 25 | Conveniencia (`head`), aleatorio simple (`sample`, repetido con varias semillas) y estratificado (`groupby` + `frac`/`slice_sample`) implementados y corridos, con sus medias y la comparación contra el parámetro | Un diseño sin implementar o corrido sin registrar resultados | Dos o más diseños ausentes |
| 5 | **Interpretación del sesgo y la variabilidad (Parte B)** | 15 | Delata el sesgo de selección de `head(20)` con la composición por ciudad (20/20 Quito) y explica el papel del diseño frente al tamaño; distingue sesgo (sistemático) de variabilidad (sorteo) | Menciona el sesgo sin respaldo en las salidas o confunde sesgo con variabilidad | No interpreta |
| 6 | **Informe — resumen y preguntas** | 10 | Resumen ejecutivo y las 5 preguntas respondidas **con base en las salidas** del código | Respuestas sin respaldo en salidas o incompletas | No respondidas |
| 7 | **Informe — conclusiones** | 5 | 2–3 conclusiones fundamentadas, con la lección de diseño en palabras propias (no copiada de la frase ancla) | Conclusión sin justificación | Ausente |
| 8 | **Profesionalismo del repo** | 5 | Commits con mensajes claros (uno por sección), sin archivos basura (`__pycache__`, `.DS_Store`), estructura respetada | Algún ítem faltante | Repo desordenado |
| — | **Bonus: ambos lenguajes** | +5 | Código completo y correcto en **Python y R** (no solo el elegido) | — | — |

**Total: 100 (+5 bonus)**

---

## Niveles de logro — definición de trabajo

- **Logrado (100%):** el criterio se cumple completo y de forma correcta; las salidas respaldan lo reportado.
- **Parcial (50%):** el criterio se cumple a medias: hay resultado pero con errores, sin verificación o sin interpretación.
- **No logrado (0):** no hay evidencia del criterio o el resultado es incorrecto sin justificación.

## Criterios de entrega

1. **Repositorio** (fork del laboratorio) con: `informe.md` completado, los scripts sin TODOs pendientes y la historia de commits coherente.
2. **Fecha límite:** lunes 19/10/2026, 23:59. Descuento de 2 puntos por día de atraso.
3. **Entrega:** el link de tu fork, en el aula virtual.

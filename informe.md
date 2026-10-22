# Informe — Clasificación de variables y población vs. muestra

**Para:** Gerencia de RetailAndina S.A. · **De:** Equipo de Business Intelligence
**Fecha:** 21/10/2026 · **Asunto:** Base de fidelización: tipos de variables y estimación por muestreo

---

## Resumen ejecutivo

Analizando la estructura de la base de fidelización de RetailAndina S.A., se clasificaron sus 7 variables junto con el código identificador para definir qué operaciones matemáticas son válidas en cada columna antes de generar reportes comerciales. Posteriormente, tomando la población completa de 400 clientes (cuyo ingreso mensual promedio real es de `1330.72 USD`), se estimó dicho ingreso con muestras de 20 registros mediante tres diseños: conveniencia, aleatorio simple y estratificado por ciudad. A partir de estas pruebas, se observa que la validez de una muestra depende de cómo se seleccionan los clientes y no solo de cuántos se toman: se requiere un diseño bien estructurado para así evitar sesgos por el orden del archivo y controlar la variación propia del azar antes de tomar decisiones de negocio.

## Parte A — Clasificación de las variables

| Variable | Tipo | Justificación (criterio) | Verificación en código |
|---|---|---|---|
| `cliente_id` | Categórica nominal (identificador) | Funciona únicamente como etiqueta para distinguir a cada cliente, por lo que no mide ninguna cantidad ni tiene sentido promediarla. | `dtype: object` (`chr` en R), 12 valores únicos (`C001` a `C012`). |
| `edad` | Numérica continua (discretizada) | Representa tiempo de vida, donde sí tiene sentido hablar de la mitad del valor o fracciones de año, aunque en la tabla se registre en años cumplidos enteros por practicidad. | `dtype: int64` (`int` en R), 12 valores únicos entre `22` y `48`. |
| `numero_hijos` | Numérica discreta | Proviene de contar personas, de modo que solo admite números enteros y no tiene sentido hablar de la mitad de un hijo. | `dtype: int64` (`int` en R), 5 valores únicos (`0, 1, 2, 3, 4`). |
| `genero` | Categórica nominal | Agrupa a los clientes en categorías descriptivas sin jerarquía entre sí. En esta base es nominal de 3 niveles y no binaria porque incluye la categoría `Otro`. | `dtype: object` (`chr` en R), 3 valores únicos (`Femenino`, `Masculino`, `Otro`). |
| `nivel_educacion` | Categórica ordinal | Clasifica el grado de estudios alcanzado siguiendo una jerarquía clara de avance académico, aunque sin una distancia numérica exacta entre etapas. | `dtype: object` (`chr` en R), 4 valores únicos. Se declaró el orden con `CategoricalDtype` / `factor(..., ordered=TRUE)` comprobando `.min()` = `Primaria`. |
| `ciudad` | Categórica nominal | Indica el lugar de residencia del cliente mediante nombres geográficos que no tienen un orden natural entre ellos. | `dtype: object` (`chr` en R), 3 valores únicos (`Quito`, `Guayaquil`, `Cuenca`). |
| `ingresos_mensuales` | Numérica continua | Mide dinero en dólares, una magnitud donde la mitad del valor y los decimales tienen completo sentido práctico y matemático. | `dtype: int64` (`int` en R), 12 valores únicos entre `760` y `2450` USD. |
| `satisfaccion` | Categórica ordinal | Evalúa el nivel de conformidad en una escala del 1 al 5 donde sí existe un orden de menor a mayor, pero la distancia entre niveles no es proporcional (un 4 no equivale al doble de satisfacción que un 2). | Llega como `int64` (`int` en R) con 4 valores presentes (`2, 3, 4, 5`). Convertida a categoría ordenada `1 < 2 < 3 < 4 < 5`, verificando `.min()` = `2`. |

**P1.** ¿Qué te dijo el dtype de `satisfaccion` y por qué no basta para clasificarla? ¿Qué pasa si una ordinal queda como texto sin declarar el orden?

Revisando los tipos que detecta el programa por defecto, se observa que `satisfaccion` ingresa como número entero (`int64` en Python e `int` en R) únicamente porque en el archivo fue guardada con dígitos del 1 al 5. Sin embargo, esa pista técnica no basta para clasificarla como numérica, ya que los números solo representan etiquetas de opinión: un cliente con calificación 4 está más satisfecho que uno con 2, pero no siente el doble de satisfacción, por lo que calcular promedios directos como si fueran dólares llevaría a conclusiones equivocadas. Por otra parte, dejando una variable ordinal como `nivel_educacion` en texto plano sin declarar su jerarquía, el lenguaje ordena las categorías alfabéticamente (`Posgrado` aparece antes que `Primaria` y `Secundaria`), lo que distorsiona tablas, gráficos y comparaciones como `.min()`. Por ello, se requiere definir el orden de forma explícita con `CategoricalDtype` o `factor(..., ordered=TRUE)` cuidando la escritura exacta de cada nivel, dado que un error mínimo de tipeo como escribir `"Postgrado"` con `t` provoca que los 2 registros de `"Posgrado"` no coincidan con la lista y se conviertan silenciosamente en datos faltantes (`NaN` / `NA`).

## Parte B — Población vs. muestra

### La población y su parámetro

| Concepto | Valor |
|---|---|
| Población (N) | `400` clientes (`200` en Quito, `120` en Guayaquil y `80` en Cuenca) |
| Variable de interés | `ingresos_mensuales` (ingreso mensual en USD) |
| Parámetro poblacional (media) | `1330.72 USD` |

*¿Por qué se muestrea si aquí el parámetro existe y se calculó?*

Considerando que en este ejercicio la base de 400 clientes es pequeña y ya está disponible, se calcula el parámetro real (`1330.72 USD`) para tener un punto de comparación exacto y comprobar qué tan bien funciona cada método de muestreo. En la operación diaria de una empresa con decenas de miles de clientes, levantar información nueva, hacer encuestas telefónicas o auditar registros uno por uno resulta demasiado costoso y lento, por lo que se requiere trabajar con muestras pequeñas sabiendo de antemano qué diseño garantiza resultados confiables.

### Los tres diseños

| Diseño | n | Media estimada | Composición por ciudad | Diferencia vs. parámetro |
|---|---|---|---|---|
| Conveniencia (`head`) | 20 | `1348.50 USD` | Quito: 20, Guayaquil: 0, Cuenca: 0 | `+17.78 USD` |
| Aleatorio simple (`sample`) | 20 | `1336.00 USD` | Cuenca: 8, Quito: 8, Guayaquil: 4 | `+5.28 USD` |
| Estratificado (`groupby` + 5 %) | 20 | `1287.50 USD` | Quito: 10, Guayaquil: 6, Cuenca: 4 | `-43.22 USD` |

*Medias de 5 sorteos distintos del aleatorio simple (semillas 1 a 5 en Python):*

| Semilla | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Media | `1336.00 USD` | `1405.00 USD` | `1235.00 USD` | `1491.50 USD` | `1288.00 USD` |

**P2.** ¿Cuánto vale el parámetro poblacional y cuánto estimó cada diseño? ¿Cuál quedó más cerca y por qué eso **no** alcanza para declarar un ganador?

Comparando las estimaciones frente al parámetro poblacional de `1330.72 USD`, se observa que con la semilla 1 el muestreo por conveniencia arrojó `1348.50 USD` (`+17.78 USD`), el aleatorio simple `1336.00 USD` (`+5.28 USD`) y el estratificado `1287.50 USD` (`-43.22 USD`). Aunque en esta ejecución puntual el aleatorio simple quedó más cerca del valor real —e incluso la muestra por conveniencia estuvo más cerca que la estratificada—, mirar un solo resultado no alcanza para declarar ganador a un diseño porque en muestras de 20 clientes influye mucho la suerte del sorteo. De hecho, cambiando únicamente a la semilla 4 en el mismo muestreo aleatorio simple, la media estimada se dispara a `1491.50 USD` (`+160.78 USD`). Por lo tanto, se requiere evaluar un método por la solidez de su procedimiento y por cómo representa a toda la población, no por haber acertado por casualidad en un intento aislado.

**P3.** La muestra por conveniencia también tiene 20 filas. ¿Qué defecto tiene y cómo lo delatas en la composición por ciudad? ¿Se corrige tomando más filas?

Observando la composición por ciudad que entrega el código, se detecta de inmediato el defecto del muestreo por conveniencia: los 20 clientes seleccionados pertenecen únicamente a Quito (`20 de 20`), dejando fuera por completo a Guayaquil y Cuenca. Esto ocurre porque el archivo `clientes_400.csv` viene ordenado por ciudad y sus primeras 200 filas corresponden todas a Quito, donde el ingreso promedio es más alto (`1390.50 USD`, frente a `1322.58 USD` en Guayaquil y `1193.50 USD` en Cuenca). Debido a este orden en los datos, el sesgo de selección no se corrige tomando más filas con el mismo corte: aun si se tomaran los primeros 50, 100 o 200 registros con `head()`, la muestra seguiría teniendo 100 % clientes de Quito y continuaría inflando el ingreso promedio real de la empresa.

**P4.** El sorteo aleatorio dio un número distinto en cada semilla. ¿Qué implica esa variabilidad para una empresa que va a decidir con un solo estudio?

Analizando los cinco sorteos del muestreo aleatorio simple, se nota que la media estimada pasa desde `1235.00 USD` en la semilla 3 (`-95.72 USD` por debajo del parámetro) hasta `1491.50 USD` en la semilla 4 (`+160.78 USD` por encima), lo que representa una diferencia de `256.50 USD` aplicando exactamente la misma regla de selección. Para una empresa que va a tomar una decisión comercial basándose en un único estudio, esta variabilidad implica que una muestra pequeña de `n = 20` tiene un margen de variación amplio por puro azar. En consecuencia, se requiere acompañar la estimación con un margen de error o ampliar el tamaño de la muestra cuando la gerencia necesite mayor precisión para definir precios, presupuestos o metas de ventas.

**P5.** ¿Cuándo usarías cada diseño en la práctica? Relaciona cada uno con un uso real (piloto, subgrupos que deben aparecer, conclusión sobre toda la población).

Evaluando las ventajas y límites de cada método en el trabajo diario, se recomienda aplicarlos según el objetivo del estudio:
- **Muestreo por conveniencia (`head`):** Resulta útil únicamente para pruebas técnicas rápidas, como verificar que un script corre sin errores o hacer un piloto interno de una encuesta para ver si las preguntas se entienden, pero nunca para sacar conclusiones sobre toda la cartera de clientes.
- **Muestreo aleatorio simple (`sample`):** Es adecuado cuando se busca una conclusión general sobre toda la población, se tiene el listado completo de clientes para sortear con igual probabilidad y no existen subgrupos muy marcados que corran riesgo de quedar mal representados por azar.
- **Muestreo estratificado (`groupby` + 5 % / `slice_sample`):** Se requiere cuando la población se divide en subgrupos importantes para el negocio —como las ciudades donde opera RetailAndina— y es indispensable garantizar que todos aparezcan en su proporción exacta (`10` de Quito, `6` de Guayaquil y `4` de Cuenca), evitando desbalances casuales como el que ocurrió en el sorteo simple de la semilla 1, donde Cuenca tuvo 8 de los 20 clientes pese a ser la ciudad más pequeña.

## Conclusiones

Analizando la estructura de las variables y los sesgos en los datos, se observa que no se debe depender únicamente del tipo que el sistema asigna de forma automática. Es necesario clasificar con criterio técnico escalas como la satisfacción y el nivel de educación para así evitar que el software calcule promedios erróneos o altere la jerarquía real al ordenarlas alfabéticamente. Del mismo modo, al tomar registros por conveniencia desde el inicio del archivo, se generó un sesgo evidente al seleccionar únicamente clientes de Quito (20/20), lo que demuestra que la representatividad de los datos depende directamente del diseño del muestreo y que un fallo sistemático de este tipo no se soluciona simplemente agregando más filas.

Comparando los resultados obtenidos frente al parámetro real de 1330.72 USD, se evidencia que para respaldar las decisiones comerciales en RetailAndina S.A. es indispensable implementar un muestreo estratificado por ciudad. Este enfoque permite controlar la dispersión y garantiza que cada plaza comercial participe según su peso real dentro del negocio (50 % Quito, 30 % Guayaquil y 20 % Cuenca). De esta manera, la gerencia evita basarse en muestras aleatorias inestables y cuenta con un rango de variación esperado que le permite comprometer recursos con respaldo técnico y claridad operativa.
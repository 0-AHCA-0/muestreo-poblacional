# Informe — Clasificación de variables y población vs. muestra

**Para:** Gerencia de RetailAndina S.A. · **De:** Equipo de Business Intelligence
**Fecha:** 21/10/2026 · **Asunto:** Base de fidelización: tipos de variables y estimación por muestreo

---

## Resumen ejecutivo

Analizando la estructura de la base de fidelización de RetailAndina S.A., se clasificaron sus siete variables junto con el código identificador para definir qué operaciones matemáticas son válidas en cada columna antes de generar reportes comerciales. Posteriormente, tomando la población completa de 400 clientes cuyo ingreso mensual promedio real es de 1330.72 USD, se estimó dicho ingreso con muestras de 20 registros mediante tres diseños: conveniencia, aleatorio simple y estratificado por ciudad. A partir de estas pruebas, se observa que la validez de una muestra depende de cómo se seleccionan los clientes y no solo de cuántos se toman: se requiere un diseño bien estructurado para así evitar sesgos por el orden del archivo y controlar la variación propia del azar antes de tomar decisiones de negocio.

## Parte A — Clasificación de las variables

| Variable | Tipo | Justificación | Verificación en código |
|---|---|---|---|
| cliente_id | Categórica nominal | Funciona solo como código para identificar a cada cliente, por lo que no mide ninguna cantidad ni tiene sentido promediarla. | Texto con 12 códigos únicos desde C001 hasta C012. |
| edad | Numérica continua | Mide el tiempo de vida, donde sí tiene sentido hablar de medio año, aunque en la tabla se anote en años cumplidos enteros. | Entero con 12 valores únicos entre 22 y 48 años. |
| numero_hijos | Numérica discreta | Proviene de contar personas, así que solo toma números enteros y no existe la mitad de un hijo. | Entero con 5 valores únicos de 0 a 4 hijos. |
| genero | Categórica nominal | Agrupa a los clientes en etiquetas descriptivas sin orden entre sí. No es binaria porque incluye una tercera categoría. | Texto con 3 categorías: Femenino, Masculino y Otro. |
| nivel_educacion | Categórica ordinal | Ordena el grado de estudios siguiendo una jerarquía de avance académico, pero sin una distancia numérica entre niveles. | Texto con 4 niveles ordenados desde Primaria hasta Posgrado, comprobando que el mínimo es Primaria. |
| ciudad | Categórica nominal | Indica la ubicación del cliente mediante nombres de ciudades que no tienen jerarquía ni orden natural. | Texto con 3 valores únicos: Quito, Guayaquil y Cuenca. |
| ingresos_mensuales | Numérica continua | Representa dinero en dólares, donde la mitad del valor y los decimales tienen completo sentido práctico. | Entero con 12 valores únicos entre 760 y 2450 USD. |
| satisfaccion | Categórica ordinal | Califica la conformidad del 1 al 5 con un orden de menor a mayor, pero donde un 4 no significa el doble de satisfacción que un 2. | Llega como entero con 4 niveles presentes del 2 al 5. Se declaró su orden de 1 a 5 comprobando que el mínimo es 2. |

**P1.** ¿Qué te dijo el dtype de `satisfaccion` y por qué no basta para clasificarla? ¿Qué pasa si una ordinal queda como texto sin declarar el orden?

Revisando los tipos que detecta el programa por defecto, se observa que la variable satisfacción entra como número entero simplemente porque en el archivo fue guardada con números del 1 al 5. Sin embargo, ese dato técnico no alcanza para clasificarla como numérica, ya que esos números solo son etiquetas de opinión: un cliente con nivel 4 está más conforme que uno con nivel 2, pero no siente el doble de satisfacción, así que promediarlos directamente como si fueran dólares daría una idea equivocada. Por otro lado, si una variable con jerarquía como el nivel de educación se deja como texto común sin declarar su orden, el programa ordena las categorías alfabéticamente y pone Posgrado antes que Primaria y Secundaria, dañando el sentido de las tablas, los gráficos y el cálculo del mínimo. Además, al declarar los niveles a mano hay que escribirlos igual que en la base, porque un pequeño error como escribir Postgrado con t hace que esos dos registros no coincidan con la lista y se pierdan como valores vacíos sin que el programa avise.

## Parte B — Población vs. muestra

### La población y su parámetro

En este ejercicio la población completa corresponde a los 400 clientes de la base de fidelización, distribuidos en 200 de Quito, 120 de Guayaquil y 80 de Cuenca, mientras que la variable de interés es el ingreso mensual en dólares cuyo parámetro poblacional tiene una media real de 1330.72 USD.

Considerando que aquí la base de 400 clientes es pequeña y ya está disponible, se calcula el promedio real de 1330.72 USD para tener un punto de comparación exacto y comprobar qué tan bien funciona cada método de muestreo. En la operación diaria de una empresa con decenas de miles de clientes, levantar información nueva, hacer encuestas telefónicas o auditar registros uno por uno resulta demasiado costoso y lento, por lo que se requiere trabajar con muestras pequeñas sabiendo de antemano qué diseño garantiza resultados confiables.

### Los tres diseños

| Diseño | n | Media estimada | Composición por ciudad | Diferencia vs. parámetro |
|---|---|---|---|---|
| Conveniencia | 20 | 1348.50 USD | Quito: 20, Guayaquil: 0, Cuenca: 0 | +17.78 USD |
| Aleatorio simple | 20 | 1336.00 USD | Cuenca: 8, Quito: 8, Guayaquil: 4 | +5.28 USD |
| Estratificado | 20 | 1287.50 USD | Quito: 10, Guayaquil: 6, Cuenca: 4 | -43.22 USD |

Al repetir cinco veces el sorteo del muestreo aleatorio simple en Python cambiando la semilla del 1 al 5, las medias obtenidas fueron 1336.00 USD en la semilla 1, 1405.00 USD en la semilla 2, 1235.00 USD en la semilla 3, 1491.50 USD en la semilla 4 y 1288.00 USD en la semilla 5.

**P2.** ¿Cuánto vale el parámetro poblacional y cuánto estimó cada diseño? ¿Cuál quedó más cerca y por qué eso **no** alcanza para declarar un ganador?

Comparando los resultados frente al parámetro poblacional real de 1330.72 USD, con la semilla 1 en Python el muestreo por conveniencia estimó 1348.50 USD, el aleatorio simple dio 1336.00 USD y el estratificado marcó 1287.50 USD. Aunque en esta corrida el aleatorio simple quedó a solo 5.28 USD del valor real, e incluso el corte por conveniencia estuvo más cerca que el estratificado, mirar un único resultado no sirve para declarar un ganador porque en muestras pequeñas de 20 personas pesa mucho la suerte del sorteo. Basta con pasar a la semilla 4 en el mismo muestreo aleatorio simple para que el promedio suba hasta 1491.50 USD, alejándose por más de 160 USD del valor real. Por eso un diseño de muestreo se evalúa por qué tan bien representa a los grupos de la población y por evitar sesgos, no por haber acertado de casualidad en un solo intento.

**P3.** La muestra por conveniencia también tiene 20 filas. ¿Qué defecto tiene y cómo lo delatas en la composición por ciudad? ¿Se corrige tomando más filas?

Observando el conteo por ciudad, el problema de la muestra por conveniencia salta a la vista: los 20 clientes elegidos son todos de Quito y no aparece nadie de Guayaquil ni de Cuenca. Esto pasa porque el archivo viene ordenado por ciudad y los primeros 200 registros pertenecen a Quito, que justamente es la plaza con el ingreso promedio más alto con 1390.50 USD, por encima de Guayaquil con 1322.58 USD y Cuenca con 1193.50 USD. Debido a este orden físico en la tabla, el defecto no se arregla tomando más filas con el mismo método: aunque se tomaran los primeros 50, 100 o 200 clientes, toda la muestra seguiría siendo de Quito y seguiría inflando el ingreso promedio real de la cadena.

**P4.** El sorteo aleatorio dio un número distinto en cada semilla. ¿Qué implica esa variabilidad para una empresa que va a decidir con un solo estudio?

Analizando los cinco sorteos del muestreo aleatorio simple, se ve que el promedio estimado baja hasta 1235.00 USD en la semilla 3 y sube hasta 1491.50 USD en la semilla 4, lo que deja una diferencia de 256.50 USD usando exactamente el mismo procedimiento al azar. Para una empresa que va a tomar una decisión comercial guiándose por un solo estudio, esta variación significa que un promedio sacado con apenas 20 clientes puede moverse bastante hacia arriba o hacia abajo por puro azar. Por lo tanto, la gerencia no debe tomar ese número como un dato exacto, sino acompañarlo de un margen de error o pedir una muestra más grande si necesita precisión antes de definir precios o presupuestos.

**P5.** ¿Cuándo usarías cada diseño en la práctica? Relaciona cada uno con un uso real (piloto, subgrupos que deben aparecer, conclusión sobre toda la población).

Evaluando el uso práctico de cada método dentro de la empresa, el muestreo por conveniencia solo conviene usarlo en pruebas piloto rápidas, como revisar que el código funcione bien o probar con los primeros clientes disponibles si las preguntas de una encuesta se entienden, pero nunca para sacar conclusiones sobre toda la clientela. Por su parte, el muestreo aleatorio simple funciona bien cuando se busca una conclusión general sobre toda la base, se tiene la lista completa para sortear sin favoritismos y los clientes son bastante parecidos entre sí. En cambio, el muestreo estratificado es el que se necesita cuando la población está dividida en subgrupos importantes con comportamientos distintos, como las ciudades donde vende RetailAndina, ya que obliga a que cada ciudad entre en su proporción exacta de 10 clientes de Quito, 6 de Guayaquil y 4 de Cuenca, evitando que el azar sobrepondere una ciudad pequeña como pasó en la semilla 1 del sorteo simple donde Cuenca tuvo 8 de los 20 clientes.

## Conclusiones

Analizando la estructura de las variables y los sesgos en los datos, se observa que no se debe depender únicamente del tipo que el sistema asigna de forma automática. Es necesario clasificar con criterio técnico escalas como la satisfacción y el nivel de educación para así evitar que el software calcule promedios erróneos o altere la jerarquía real al ordenarlas alfabéticamente. Del mismo modo, al tomar registros por conveniencia desde el inicio del archivo, se generó un sesgo evidente al seleccionar únicamente clientes de Quito, lo que demuestra que la representatividad de los datos depende directamente del diseño del muestreo y que un fallo sistemático de este tipo no se soluciona simplemente agregando más filas.

Comparando los resultados obtenidos frente al parámetro real de 1330.72 USD, se evidencia que para respaldar las decisiones comerciales en RetailAndina S.A. es indispensable implementar un muestreo estratificado por ciudad. Este enfoque permite controlar la dispersión y garantiza que cada plaza comercial participe según su peso real dentro del negocio con un 50 % de Quito, un 30 % de Guayaquil y un 20 % de Cuenca. De esta manera, la gerencia evita basarse en muestras aleatorias inestables y cuenta con un rango de variación esperado que le permite comprometer recursos con respaldo técnico y claridad operativa.
Comparando los resultados obtenidos frente al parámetro real de 1330.72 USD, se evidencia que para respaldar las decisiones comerciales en RetailAndina S.A. es indispensable implementar un muestreo estratificado por ciudad. Este enfoque permite controlar la dispersión y garantiza que cada plaza comercial participe según su peso real dentro del negocio con un 50 % de Quito, un 30 % de Guayaquil y un 20 % de Cuenca. De esta manera, la gerencia evita basarse en muestras aleatorias inestables y cuenta con un rango de variación esperado que le permite comprometer recursos con respaldo técnico y claridad operativa.

library(dplyr)

poblacion <- read.csv("data/clientes_400.csv")

reporte <- function(nombre, muestra, parametro) {
  # Imprime tamano, media estimada y conteo por ciudad para detectar sesgo de seleccion
  media <- mean(muestra$ingresos_mensuales)
  cat(sprintf("[%s] n=%d  media=%.2f USD  (parametro %.2f, diferencia %+.2f)\n",
              nombre, nrow(muestra), media, parametro, media - parametro))
  cat("    composicion por ciudad: ")
  print(table(muestra$ciudad))
}

# 1. Poblacion completa y parametro real (N = 400)
cat(sprintf("Poblacion: %d clientes x %d columnas\n", nrow(poblacion), ncol(poblacion)))
parametro <- mean(poblacion$ingresos_mensuales)
cat(sprintf("Parametro poblacional - ingreso medio: %.2f USD\n", parametro))
cat("Ciudades en la poblacion: ")
print(table(poblacion$ciudad))
cat("\n")

# 2. Muestra por conveniencia: primeras 20 filas del archivo
# El archivo viene ordenado por ciudad, por lo que solo entran clientes de Quito
muestra_conv <- head(poblacion, 20)

# 3. Muestra aleatoria simple: sorteo equiprobable de 20 clientes (5 % del total)
set.seed(1)
muestra_aas <- poblacion[sample(nrow(poblacion), 20), ]

# Repeticion del sorteo con semillas 1 a 5 para ver como varia la estimacion
cat("Variabilidad del muestreo aleatorio simple (semillas 1 a 5):\n")
for (semilla in 1:5) {
  set.seed(semilla)
  sorteo <- poblacion[sample(nrow(poblacion), 20), ]
  media_sorteo <- mean(sorteo$ingresos_mensuales)
  cat(sprintf("  Semilla %d: media = %.2f USD (diferencia %+.2f)\n",
              semilla, media_sorteo, media_sorteo - parametro))
}
cat("\n")

# 4. Muestra estratificada: 5 % dentro de cada ciudad (afijacion proporcional)
# Garantiza 10 clientes de Quito, 6 de Guayaquil y 4 de Cuenca
set.seed(1)
muestra_est <- poblacion |>
  group_by(ciudad) |>
  slice_sample(prop = 0.05)

# 5. Comparacion final de los tres disenos
reporte("Conveniencia", muestra_conv, parametro)
reporte("Aleatorio simple", muestra_aas, parametro)
reporte("Estratificado", muestra_est, parametro)
cat("\n")

resumen <- data.frame(
  diseno = c("Conveniencia (head)", "Aleatorio simple (sample)", "Estratificado (slice_sample)"),
  n = c(nrow(muestra_conv), nrow(muestra_aas), nrow(muestra_est)),
  media_estimada = round(c(mean(muestra_conv$ingresos_mensuales),
                           mean(muestra_aas$ingresos_mensuales),
                           mean(muestra_est$ingresos_mensuales)), 2),
  diferencia = round(c(mean(muestra_conv$ingresos_mensuales) - parametro,
                       mean(muestra_aas$ingresos_mensuales) - parametro,
                       mean(muestra_est$ingresos_mensuales) - parametro), 2)
)
cat(sprintf("Parametro poblacional: %.2f USD\n", parametro))
print(resumen, row.names = FALSE)

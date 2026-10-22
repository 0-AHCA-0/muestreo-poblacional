clientes <- read.csv("data/clientes.csv", stringsAsFactors = FALSE)

# 1. Estructura general del archivo
cat(sprintf("Dimensiones: %d filas x %d columnas\n\n", nrow(clientes), ncol(clientes)))
print(clientes)
cat("\n")

# 2. Tipos de datos inferidos por R (str)
# Llegan como entero (int): edad, numero_hijos, ingresos_mensuales y satisfaccion.
# Llegan como texto (chr): cliente_id, genero, nivel_educacion y ciudad.
# La columna satisfaccion viene como int pero su naturaleza es categorica ordinal.
str(clientes)
cat("\n")

# 3. Revision de valores unicos por columna
# Confirmamos que genero tiene 3 categorias (Femenino, Masculino, Otro)
cat("Valores unicos por variable:\n")
for (columna in names(clientes)) {
  unicos <- unique(clientes[[columna]])
  cat(sprintf("  %s (%d unicos): %s\n", columna, length(unicos), paste(unicos, collapse = ", ")))
}
cat("\n")

# 4. Definir el orden de las variables ordinales con factores ordenados
educacion_original <- clientes$nivel_educacion

clientes$nivel_educacion <- factor(
  clientes$nivel_educacion,
  levels = c("Primaria", "Secundaria", "Universidad", "Posgrado"),
  ordered = TRUE
)
cat("Nivel educativo minimo:", as.character(min(clientes$nivel_educacion)), "\n")

clientes$satisfaccion <- factor(
  clientes$satisfaccion,
  levels = 1:5,
  ordered = TRUE
)
cat("Satisfaccion minima registrada:", as.character(min(clientes$satisfaccion)), "\n")

# Prueba de error de escritura en los niveles ("Postgrado" con t)
# Los valores que no coinciden con levels pasan a ser NA silenciosamente
educacion_typo <- factor(
  educacion_original,
  levels = c("Primaria", "Secundaria", "Universidad", "Postgrado"),
  ordered = TRUE
)
cat("Valores perdidos (NA) al escribir 'Postgrado' con t:", sum(is.na(educacion_typo)), "\n")

# 5. Resumen final de la clasificacion de variables
clasificacion <- c(
  cliente_id         = "Categorica nominal (identificador)",
  edad               = "Numerica continua (registrada en anos cumplidos, discreta en el archivo)",
  numero_hijos       = "Numerica discreta",
  genero             = "Categorica nominal (3 categorias)",
  nivel_educacion    = "Categorica ordinal",
  ciudad             = "Categorica nominal",
  ingresos_mensuales = "Numerica continua",
  satisfaccion       = "Categorica ordinal"
)

cat("\nResumen de la clasificacion:\n")
for (variable in names(clasificacion)) {
  cat(sprintf("  %-18s %s\n", variable, clasificacion[[variable]]))
}

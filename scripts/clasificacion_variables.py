import pandas as pd

clientes = pd.read_csv("data/clientes.csv")

# 1. Estructura general del archivo
print(f"Dimensiones: {clientes.shape[0]} filas x {clientes.shape[1]} columnas\n")
print("Primeras filas:")
print(clientes.to_string(index=False))
print()

# 2. Tipos de datos que infiere pandas por defecto
# Llegan como entero (int64): edad, numero_hijos, ingresos_mensuales y satisfaccion.
# Llegan como texto (object): cliente_id, genero, nivel_educacion y ciudad.
# Aunque satisfaccion aparece como int64, en realidad representa una escala ordinal.
print("Tipos inferidos (dtype):")
print(clientes.dtypes)
print()

# 3. Revision de valores unicos por columna
# Permite ver que genero tiene 3 categorias en la base (Femenino, Masculino, Otro)
print("Valores unicos por variable:")
for columna in clientes.columns:
    unicos = clientes[columna].unique()
    print(f"  {columna} ({len(unicos)} unicos): {unicos.tolist()}")
print()

# 4. Definir el orden correcto en las variables ordinales
orden_educacion = pd.CategoricalDtype(
    categories=["Primaria", "Secundaria", "Universidad", "Posgrado"],
    ordered=True
)
clientes["nivel_educacion"] = clientes["nivel_educacion"].astype(orden_educacion)
print("Nivel educativo minimo:", clientes["nivel_educacion"].min())

orden_satisfaccion = pd.CategoricalDtype(
    categories=[1, 2, 3, 4, 5],
    ordered=True
)
clientes["satisfaccion"] = clientes["satisfaccion"].astype(orden_satisfaccion)
print("Satisfaccion minima registrada:", clientes["satisfaccion"].min())

# Prueba de error de escritura al declarar categorias ("Postgrado" con t)
# Los registros que no coinciden con la lista se vuelven NaN sin lanzar error
educacion_mal_escrita = pd.CategoricalDtype(
    categories=["Primaria", "Secundaria", "Universidad", "Postgrado"],
    ordered=True
)
faltantes_typo = pd.read_csv("data/clientes.csv")["nivel_educacion"].astype(educacion_mal_escrita).isna().sum()
print(f"Valores perdidos (NaN) al escribir 'Postgrado' con t: {faltantes_typo}")
print()

# 5. Resumen final de la clasificacion de variables
clasificacion = {
    "cliente_id": "Categorica nominal (identificador)",
    "edad": "Numerica continua (registrada en anos cumplidos, discreta en el archivo)",
    "numero_hijos": "Numerica discreta",
    "genero": "Categorica nominal (3 categorias)",
    "nivel_educacion": "Categorica ordinal",
    "ciudad": "Categorica nominal",
    "ingresos_mensuales": "Numerica continua",
    "satisfaccion": "Categorica ordinal",
}

print("Resumen de la clasificacion:")
for variable, tipo in clasificacion.items():
    print(f"  {variable:20s} {tipo}")

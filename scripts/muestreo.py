import pandas as pd

pd.set_option("display.width", 100)


def reporte(nombre, muestra, parametro):
    # Muestra el tamano, la media estimada y el conteo por ciudad para detectar sesgos
    n = len(muestra)
    media = muestra["ingresos_mensuales"].mean()
    comp = muestra["ciudad"].value_counts().to_dict()
    print(f"[{nombre}] n={n}  media={media:.2f} USD  "
          f"(parametro {parametro:.2f}, diferencia {media - parametro:+.2f})")
    print(f"    composicion por ciudad: {comp}")


# 1. Poblacion completa y parametro real (N = 400)
poblacion = pd.read_csv("data/clientes_400.csv")
parametro = poblacion["ingresos_mensuales"].mean()
print(f"Poblacion: {poblacion.shape[0]} clientes x {poblacion.shape[1]} columnas")
print(f"Parametro poblacional - ingreso medio: {parametro:.2f} USD")
print("Ciudades en la poblacion:", poblacion["ciudad"].value_counts().to_dict())
print()

# 2. Muestra por conveniencia: primeras 20 filas del archivo
# Como el CSV esta ordenado por ciudad, este corte selecciona solo clientes de Quito
muestra_conv = poblacion.head(20)

# 3. Muestra aleatoria simple: sorteo equiprobable de 20 clientes (5 % de la base)
muestra_aas = poblacion.sample(20, random_state=1)

# Repeticion del sorteo con semillas 1 a 5 para observar la variabilidad muestral
print("Variabilidad del muestreo aleatorio simple (semillas 1 a 5):")
for semilla in range(1, 6):
    sorteo = poblacion.sample(20, random_state=semilla)
    media_sorteo = sorteo["ingresos_mensuales"].mean()
    print(f"  Semilla {semilla}: media = {media_sorteo:.2f} USD "
          f"(diferencia {media_sorteo - parametro:+.2f})")
print()

# 4. Muestra estratificada: 5 % dentro de cada ciudad manteniendo la proporcion poblacional
# Asegura exactamente 10 de Quito, 6 de Guayaquil y 4 de Cuenca
muestra_est = poblacion.groupby("ciudad", group_keys=False).sample(frac=0.05, random_state=1)

# 5. Comparacion final de los tres disenos frente al parametro
reporte("Conveniencia", muestra_conv, parametro)
reporte("Aleatorio simple", muestra_aas, parametro)
reporte("Estratificado", muestra_est, parametro)
print()

resumen = pd.DataFrame([
    {"diseno": "Conveniencia (head)", "n": len(muestra_conv),
     "media estimada": round(muestra_conv["ingresos_mensuales"].mean(), 2),
     "diferencia": round(muestra_conv["ingresos_mensuales"].mean() - parametro, 2)},
    {"diseno": "Aleatorio simple (sample)", "n": len(muestra_aas),
     "media estimada": round(muestra_aas["ingresos_mensuales"].mean(), 2),
     "diferencia": round(muestra_aas["ingresos_mensuales"].mean() - parametro, 2)},
    {"diseno": "Estratificado (groupby + frac)", "n": len(muestra_est),
     "media estimada": round(muestra_est["ingresos_mensuales"].mean(), 2),
     "diferencia": round(muestra_est["ingresos_mensuales"].mean() - parametro, 2)},
])
print(f"Parametro poblacional: {parametro:.2f} USD")
print(resumen.to_string(index=False))

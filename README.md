# Laboratorio: clasificación de variables y población vs. muestra

**Caso empresarial:** RetailAndina S.A., cadena ecuatoriana de tiendas de consumo masivo.

**Sesión de trabajo:** martes 13 de octubre de 2026 (18:00–20:00) · **Entrega:** lunes 19 de octubre de 2026, 23:59 (el link de tu fork).

## El contexto

La gerencia de RetailAndina recibió dos consultas de su equipo comercial:

1. **La base de fidelización creció y nadie la conoce por dentro.** Antes de analizarla, el equipo quiere saber qué tipo de variables contiene: ¿qué se puede promediar, qué se puede ordenar y qué solo se puede contar?
2. **¿Cuál es el ingreso mensual promedio de los clientes?** La base completa tiene 400 registros y el equipo de BI tomará muestras de 20 para responder. La gerencia ya aprobó la idea, pero el analista jefe pidió una demostración de que la muestra «representa» a la base — y de qué depende esa representatividad.

**Tu rol:** analista del equipo de BI. Clasificas las variables de la base con criterio y verificación en código (Parte A), y después usas la base de 400 como población para comparar tres formas de muestrear y responder la segunda consulta con evidencia (Parte B).

## Objetivos de la práctica

**Objetivo general:** clasificar las variables de un archivo de datos justificando cada decisión y comparar tres diseños de muestreo contra el parámetro poblacional, para explicar por qué el diseño — y no el tamaño — decide la representatividad.

**Al terminar la práctica podrás:**

1. **Clasificar** cualquier variable como numérica (continua o discreta) o categórica (nominal, binaria u ordinal) usando el criterio, no el ejemplo.
2. **Verificar** esa clasificación en código (`dtypes`/`str` y `unique()`/`levels()`) reconociendo que el tipo que infiere el lenguaje es una pista, no la clasificación.
3. **Declarar** el orden de una variable ordinal en código (factor ordenado en R, `CategoricalDtype` en pandas) y explicar la trampa de un nivel mal escrito.
4. **Distinguir** población, muestra y parámetro, y **calcular** el parámetro cuando la población está disponible.
5. **Implementar** tres diseños de muestreo en Python o R (conveniencia, aleatorio simple y estratificado) y **comparar** sus estimaciones con el parámetro.
6. **Interpretar** el sesgo de selección de un archivo ordenado y la variabilidad del sorteo, y **reportar** todo en un informe breve con conclusiones respaldadas por las salidas.

Cada objetivo tiene su sección en `informe.md` y su criterio en `EVALUACION.md`.

## Archivos del repositorio

- `README.md`: este documento, con el contexto del caso y los objetivos
- `informe.md`: la plantilla del informe — el entregable
- `data/clientes.csv`: 12 clientes con 7 variables — el extracto de trabajo de la Parte A
- `data/clientes_400.csv`: 400 clientes (la base de fidelización completa) — la **población** de la Parte B
- `scripts/clasificacion_variables.py` y `.R`: la Parte A, con pasos pendientes (TODOs por completar)
- `scripts/muestreo.py` y `.R`: la Parte B, con pasos pendientes (TODOs por completar)
- `EVALUACION.md`: la rúbrica con la que se evalúa el laboratorio

## Requisitos

- **Python 3.9 o superior** con `pandas` (`pip install pandas`), **o R 4.x** (la Parte B usa `dplyr` para el estratificado: `install.packages("dplyr")`).
- Sin instalación: Google Colab (Python) o Posit Cloud (R), donde ya trabajaron en la Práctica 1.

## Cómo trabajar y entregar

1. Haz un **fork** de este repositorio: tu fork es tu entrega.
2. Trabaja sobre tu copia (clónala con `git clone` o ábrela en Posit Cloud).
3. Completa los **TODOs en orden**: primero `clasificacion_variables`, después `muestreo`. Al terminar cada bloque, corre el script y lee las salidas — el informe se escribe con ellas, no de memoria.
4. Haz un **commit por sección completada**, con mensajes claros; la historia del repositorio se revisa.
5. Completa `informe.md` (resumen, tablas, respuestas y conclusiones) y expórtalo a PDF en `informes/` si tu editor lo permite.
6. **Entrega el link de tu fork** en el aula virtual antes del **lunes 19/10, 23:59**.

**Cómo ejecutar** (desde la raíz del repositorio):

```bash
python scripts/clasificacion_variables.py
python scripts/muestreo.py

Rscript scripts/clasificacion_variables.R
Rscript scripts/muestreo.R
```

La evaluación está detallada en `EVALUACION.md` (rúbrica de 100 puntos; la nota es puntos ÷ 100 × 20).

*Laboratorio complementario, IDSD422, Estadística y Programación para Ciencia de Datos I, 2026-B.*

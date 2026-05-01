# Citi Costa Rica - Optimizador de Analistas

Este proyecto corresponde a la Tarea 6 del curso II-1122 Modelos de Optimización Industrial.

La aplicación permite resolver un modelo de programación lineal para asignar analistas a diferentes procesos bancarios de Citi Costa Rica, minimizando el tiempo de ciclo de las operaciones.

## Descripción del modelo

El modelo busca determinar cuántos analistas asignar a:

- SWIFT
- Cartas de crédito
- Garantías

La función objetivo minimiza el tiempo total de ciclo:

Min Z = 3x1 + 5x2 + 4x3

Sujeto a restricciones de cantidad total de analistas, mínimos requeridos por proceso y capacidad mínima.

## Archivos del proyecto

- `modelo.py`: contiene el modelo de programación lineal.
- `app.py`: contiene la interfaz web creada con Streamlit.
- `requirements.txt`: contiene las librerías necesarias para ejecutar la aplicación.

## Librerías utilizadas

- PuLP
- Streamlit

## Aplicación publicada

URL de la app en Streamlit:

https://citi-cr-solver-3udrm6hvzdappsfjhtgjcc.streamlit.app

## Repositorio

URL del repositorio en GitHub:

https://github.com/TiffanyRodriguezQuiros/citi-cr-solver

## Uso de la aplicación

1. Abrir la URL de Streamlit.
2. Ajustar los parámetros en la barra lateral.
3. Presionar el botón "Optimizar ahora".
4. Revisar la asignación óptima de analistas y el valor de la función objetivo.

## Autora

Tiffany Rodríguez Quirós

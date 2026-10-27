# Análisis de Rendimiento Académico y Hábitos de Sueño con Apache Spark (Procesamiento en Batch)

## Descripción de la Solución
Este proyecto utiliza PySpark para procesar y analizar un conjunto de datos masivo (`student_sleep_screen_time_academic_performance.csv`) que relaciona los hábitos de sueño, el uso de pantallas y el rendimiento académico de estudiantes. La solución implementa operaciones de limpieza de datos, transformación y Análisis Exploratorio de Datos (EDA) utilizando DataFrames.

## Tareas Realizadas en Spark
1. **Carga de Datos:** Lectura del archivo CSV infiriendo el esquema automáticamente.
2. **Limpieza y Transformación:**
   - Estandarización de la columna de género a un formato uniforme ('M' o 'F').
   - Eliminación de registros nulos en columnas clave (calidad de sueño, nivel de energía, CGPA).
   - Filtrado de valores atípicos (horas de estudio semanales > 80, horas de sueño < 3).
3. **Análisis Exploratorio (EDA):**
   - Cálculo del impacto de la calidad del sueño en el promedio académico (CGPA) y el nivel de energía.
   - Evaluación del rendimiento académico según el uso de dispositivos antes de dormir.

## Instrucciones de Ejecución
Para ejecutar este script en un entorno con Apache Spark configurado (ej. Ubuntu/VirtualBox):
1. Clonar el repositorio.
2. Asegurar que el archivo `student_sleep_screen_time_academic_performance.csv` se encuentre en el mismo directorio que el script.
3. Ejecutar el siguiente comando en la terminal:
   ```bash
   spark-submit analisis_batch.py

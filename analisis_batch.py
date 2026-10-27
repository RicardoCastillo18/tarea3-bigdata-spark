from pyspark.sql import SparkSession
from pyspark.sql.functions import col, upper, round

# Iniciar sesion de Spark
spark = SparkSession.builder \
    .appName("Analisis_Batch_Estudiantes") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

print("--- CARGANDO CONJUNTO DE DATOS ---")
df = spark.read.csv("student_sleep_screen_time_academic_performance.csv", header=True, inferSchema=True)
print(f"Total de registros iniciales: {df.count()}")

print("\n--- INICIANDO LIMPIEZA DE DATOS ---")
df_clean = df.withColumn("gender_clean", upper(col("gender").substr(1, 1)))

columnas_con_nulos = ["sleep_quality_score", "energy_level", "concentration_difficulty", "cgpa", "device_free_before_bed"]
df_clean = df_clean.dropna(subset=columnas_con_nulos)

df_clean = df_clean.filter((col("weekly_study_hours") <= 80) & (col("avg_sleep_hours_weekday") >= 3.0))
print(f"Total de registros tras la limpieza: {df_clean.count()}")

print("\n--- ANALISIS EXPLORATORIO DE DATOS (EDA) ---")
print("1. Promedio de CGPA y Nivel de Energia segun la Calidad del Sueno:")
eda_sleep = df_clean.groupBy("sleep_quality_score") \
    .avg("cgpa", "energy_level") \
    .withColumn("avg(cgpa)", round(col("avg(cgpa)"), 2)) \
    .withColumn("avg(energy_level)", round(col("avg(energy_level)"), 2)) \
    .orderBy("sleep_quality_score")
eda_sleep.show()

print("2. Promedio de CGPA segun el uso de dispositivos antes de dormir:")
eda_devices = df_clean.groupBy("device_free_before_bed") \
    .avg("cgpa", "concentration_difficulty") \
    .withColumn("avg(cgpa)", round(col("avg(cgpa)"), 2)) \
    .orderBy("device_free_before_bed")
eda_devices.show()

spark.stop()

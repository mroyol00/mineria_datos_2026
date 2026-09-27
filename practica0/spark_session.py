import os
from pyspark.sql import SparkSession

def crear_sesion_spark():
    # Ruta relativa al .jar del conector, para que funcione en cualquier ordenador
    ruta_jar = os.path.join(os.path.dirname(__file__), "drivers", "mysql-connector-j-26.7.0.jar")

    spark = (SparkSession.builder
             .appName("IBEX35")
             .config("spark.driver.extraClassPath", ruta_jar)
             .getOrCreate())
    return spark
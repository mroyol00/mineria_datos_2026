import glob
import os
from pyspark.sql import SparkSession

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))


def crear_sesion_spark():
    
    jars = glob.glob(os.path.join(RAIZ, "lib", "mysql-connector*.jar"))
    if not jars:
        raise FileNotFoundError(f"No hay ningun mysql-connector*.jar en {os.path.join(RAIZ, 'lib')}")
    ruta_jar = jars[0]

    spark = (SparkSession.builder
             .appName("IBEX35")
             .config("spark.driver.extraClassPath", ruta_jar)
             .getOrCreate())
    return spark
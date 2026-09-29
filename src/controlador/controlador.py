import os
from src.modelo.conexion.spark_session import crear_sesion_spark
from src.modelo.conexion.guardar_datos import guardar_datos_completos, guardar_datos_tratados
from src.modelo.ejercicios.ej1 import ejercicio_1
from src.modelo.ejercicios.ej2 import ejercicio_2

# Ruta relativa a la raiz del proyecto (funciona en cualquier ordenador)
RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
RUTA_CSV = os.path.join(RAIZ, "data", "ibex35_close-2024.csv")


def ejecutar_practica():
    spark = crear_sesion_spark()

    # Ej1: carga, conversion de tipos y renombrado de columnas
    df_raw, df_ej1 = ejercicio_1(spark, RUTA_CSV)

    # Ej2: limpieza y periodo temporal
    df_ej2 = ejercicio_2(df_ej1)

    # TODO: Ej3, Ej4, Ej5 (y opcionales Ej1-c, Ej3-b, Ej6)
    # df_ej3 = ejercicio_3(df_ej2) ...

    # Guardado en MySQL
    guardar_datos_completos(df_raw)      # datos completos del CSV
    guardar_datos_tratados(df_ej2)       # datos tratados (sin columnas nuevas)

    spark.stop()
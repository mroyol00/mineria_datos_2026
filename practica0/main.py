from spark_session import crear_sesion_spark
from ejercicios.ej1 import ejercicio_1


spark = crear_sesion_spark()

df_ej1 = ejercicio_1(spark)
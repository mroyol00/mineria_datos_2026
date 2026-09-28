from spark_session import crear_sesion_spark
from ejercicios.ej1 import ejercicio_1
from ejercicios.ej2 import ejercicio2


spark = crear_sesion_spark()

df_ej1 = ejercicio_1(spark)
df_ej2 = ejercicio2(df_ej1)
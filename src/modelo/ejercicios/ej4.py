from pyspark.sql.functions import *
from pyspark.sql.window import Window


def ejercicio_4(df):
    # Ej4
    print("Ej4")

    empresas = [c for c in df.columns if c not in ("Dia", "Deficiency Notice UNI")]
    df_orden = df.orderBy("Dia")
    datos = []
    for e in empresas:
        con_dato = df_orden.filter(col(e).isNotNull())
        inicial = con_dato.head(1)[0][e]
        final = con_dato.tail(1)[0][e]
        datos.append((e, float(inicial), float(final)))
    variaciones = df.sparkSession.createDataFrame(datos, ["Empresa", "Inicial", "Final"])

    variaciones = variaciones.withColumn(
        "Variación Anual", (col("Final") - col("Inicial")) / col("Inicial") * 100
    )

    variaciones = variaciones.withColumn(
        "Clasificación",
        when(col("Variación Anual") <= -15, "Bajada Fuerte")
        .when(col("Variación Anual") < -1, "Bajada")
        .when(col("Variación Anual") <= 1, "Neutra")
        .when(col("Variación Anual") < 15, "Subida")
        .otherwise("Subida Fuerte")
    )  

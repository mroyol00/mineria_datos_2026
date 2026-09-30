from pyspark.sql.functions import *
from pyspark.sql.window import Window


def ejercicio_3(df):
    # Ej3
    print("Ej3")
    df = df.withColumnRenamed("Fecha", "Dia")
    df.show(10)

    empresas = [c for c in df.columns if c != "Dia"]
    for e in empresas:
        print(e)
        df.select(
            avg(col(e)).alias("Media anual"),
            max(col(e)).alias("Max anual"),
            min(col(e)).alias("Min anual")
        ).show()

    df = df.withColumn(
        "Deficiency Notice UNI",
        when(col("UNI") < 1, True).otherwise(False)
    )
    df.show(100)
    return df
from pyspark.sql.functions import *
from pyspark.sql.window import Window


def ejercicio_5(df):
    # Ej5
    print("Ej5")
    empresas = [c for c in df.columns if c not in ("Dia", "Deficiency Notice UNI")]
    df5 = df
    for e in empresas:
        q1, q2, q3 = df.approxQuantile(e, [0.25, 0.5, 0.75], 0.01 )
        df5 = df5.withColumn(
            f"{e}Cuartil",
            when(col(e).isNull(), lit(None))
            .when(col(e) <= q1, "q1")
            .when(col(e) <= q2, "q2")
            .when(col(e) <= q3, "q3")
            .otherwise("q4")
        )

    # Primera fila del dataframe
    df5.show(1, truncate=False, vertical=True)
    df5.select("AENA", "AENACuartil", "BBVA", "BBVACuartil").show(df5.count(), truncate=False)

    return df5

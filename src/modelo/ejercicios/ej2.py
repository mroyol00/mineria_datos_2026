from pyspark.sql.functions import *


def ejercicio_2(df):
    # Ej2-a
    print("Ej2-a")

    filas_antes = df.count()
    df_sin_duplicados = df.dropDuplicates()
    filas_despues = df_sin_duplicados.count()
    print(f"Filas eliminadas: {filas_antes - filas_despues}")

    columnas_vacias = []
    for c in df_sin_duplicados.columns:
        if c != "Fecha":
            no_nulos = df_sin_duplicados.filter(col(f"`{c}`").isNotNull()).count()
            if no_nulos == 0:
                columnas_vacias.append(c)
    df_ej2 = df_sin_duplicados
    for c in columnas_vacias:
        df_ej2 = df_ej2.drop(c)
    num_empresas = len(df_ej2.columns) - 1
    print(f"Numero de empresas con informacion disponible: {num_empresas}")

    # Ej2-b
    print("Ej2-b")
    fecha_min = df_ej2.select(min("Fecha")).head()[0]
    fecha_max = df_ej2.select(max("Fecha")).head()[0]
    dias_disponibles = df_ej2.select(countDistinct("Fecha")).head()[0]

    print(f"Periodo: {fecha_min} a {fecha_max}")
    print(f"Dias con informacion disponible: {dias_disponibles}")
    print("Es coherente: la bolsa no abre findes ni festivos, por eso hay menos dias que dias naturales en el año.")
    print("No es necesario buscar datos adicionales, el periodo cubre un año completo de cotizacion.")

    return df_ej2

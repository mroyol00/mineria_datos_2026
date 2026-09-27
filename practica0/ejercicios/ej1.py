#Ej1-a
from pyspark.sql.functions import *
from pyspark.sql.types import *
def ejercicio_1(spark):
    #Ej1-a
    print("Ej1-a")

    df = (
        spark.read.option("header", True)
        .option("sep", ";")
        .csv("ibex35_close-2024.csv")
    )

    df.printSchema()

    df_converted = df.withColumn("Fecha", to_date(col("Fecha"), "dd/MM/yyyy"))

    for c in df_converted.columns:
        if c != "Fecha":
            df_converted = df_converted.withColumn(c, col(f"`{c}`").cast("float"))

    df_converted.printSchema()  
    df_converted.show(6)

    #Ej1-b
    print("Ej1-b")
    for c in df_converted.columns:
        if c.endswith(".MC"):
            nuevo = c.replace(".MC", "")
            df_converted = df_converted.withColumnRenamed(c, nuevo)


    df_converted.show(6)
    return df_converted
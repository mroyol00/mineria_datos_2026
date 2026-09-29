URL = "jdbc:mysql://localhost:3306/IBEX35"

PROPIEDADES = {
    "driver": "com.mysql.cj.jdbc.Driver",
    "user": "root",
    "password": "martaroyo"
}

def escribir_tabla(dataframe, nombre_tabla, modo="overwrite"):
    dataframe.write.jdbc(url=URL, table=nombre_tabla, mode=modo, properties=PROPIEDADES)

def leer_tabla(spark, nombre_tabla):
    return spark.read.jdbc(url=URL, table=nombre_tabla, properties=PROPIEDADES)
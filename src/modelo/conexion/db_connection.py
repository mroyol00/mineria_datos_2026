from src.modelo.conexion.spark_session import crear_sesion_spark


class ConexionBD:

    URL = "jdbc:mysql://localhost:3306/IBEX35"

    PROPIEDADES = {
        "driver": "com.mysql.cj.jdbc.Driver",
        "user": "root",
        "password": "martaroyo"
    }

    def __init__(self):
        self.spark = crear_sesion_spark()

    def escribir_tabla(self, dataframe, nombre_tabla, modo="overwrite"):
        dataframe.write.jdbc(url=self.URL, table=nombre_tabla, mode=modo, properties=self.PROPIEDADES)

    def leer_tabla(self, nombre_tabla):
        return self.spark.read.jdbc(url=self.URL, table=nombre_tabla, properties=self.PROPIEDADES)

    def cerrar(self):
        self.spark.stop()
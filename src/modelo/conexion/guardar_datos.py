TABLA = "Datos2024"


def guardar_datos(conexion, df):
    print("Guardando datos en", TABLA)
    conexion.escribir_tabla(df, TABLA)
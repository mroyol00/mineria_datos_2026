from src.modelo.conexion.db_connection import escribir_tabla

TABLA = "Datos2024"

def guardar_datos(df):
    print("Guardando datos en", TABLA)
    escribir_tabla(df, TABLA)

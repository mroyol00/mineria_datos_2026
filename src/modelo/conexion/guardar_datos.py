from src.modelo.conexion.db_connection import escribir_tabla

# El enunciado nombra las dos tablas "Datos2024"; con la misma tabla y modo
# overwrite la segunda borraria la primera, por eso la segunda lleva otro nombre.
TABLA_COMPLETA = "Datos2024"
TABLA_TRATADA = "Datos2024Tratados"


def guardar_datos_completos(df_raw):
    print("Guardando datos completos del CSV en", TABLA_COMPLETA)
    escribir_tabla(df_raw, TABLA_COMPLETA)


def guardar_datos_tratados(df_tratado):
    print("Guardando datos tratados en", TABLA_TRATADA)
    escribir_tabla(df_tratado, TABLA_TRATADA)
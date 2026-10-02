import os
from src.modelo.conexion.db_connection import ConexionBD
from src.modelo.conexion.guardar_datos import guardar_datos
from src.modelo.ejercicios.ej1 import ejercicio_1
from src.modelo.ejercicios.ej2 import ejercicio_2
from src.modelo.ejercicios.ej3 import ejercicio_3
from src.modelo.ejercicios.ej4 import ejercicio_4
from src.modelo.ejercicios.ej5 import ejercicio_5

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
RUTA_CSV = os.path.join(RAIZ, "data", "ibex35_close-2024.csv")


def ejecutar_practica():
    conexion = ConexionBD()

    try:
        df_raw, df_ej1 = ejercicio_1(conexion, RUTA_CSV)

        df_ej2 = ejercicio_2(df_ej1)

        df_ej3 = ejercicio_3(df_ej2)

        df_ej4 = ejercicio_4(df_ej3)

        df_ej5 = ejercicio_5(df_ej4)

        guardar_datos(conexion, df_raw)
        guardar_datos(conexion, df_ej2)
    finally:
        conexion.cerrar()
import os
import json
from datetime import datetime
from typing import Any, Dict, Optional

# Directorio donde se almacenan las partidas
from config import PATH_PARTIDAS,PATH_PARTIDAS_TEMP

def guardar_partida(partida_data: Dict[str, Any],nombre_archivo:Optional[str] = None, temporal: bool = False) -> str:
    """
    Guarda los datos de una partida en un archivo JSON en el directorio definido.

    Parámetros:
    -----------
    partida_data : Dict[str, Any]
        Diccionario con los datos de la partida a guardar.
    temporal : bool, opcional
        Si es True, el archivo se marcará como temporal con el sufijo "_temp".

    Retorna:
    --------
    str
        Nombre del archivo JSON guardado.

    Lanza:
    ------
    RuntimeError
        Si ocurre un error al escribir el archivo.
    """
    # Generar nombre único basado en fecha y hora
    if not nombre_archivo:
        nombre_archivo = datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_archivo = f"partida_{nombre_archivo}"
    if temporal:
        nombre_archivo += "_temp"
    nombre_archivo += ".json"
    camino = PATH_PARTIDAS_TEMP if temporal else PATH_PARTIDAS
    # Ruta completa del archivo
    ruta = os.path.join(camino, nombre_archivo)

    try:
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(partida_data, f, indent=4)
        return nombre_archivo
    except Exception as e:
        raise RuntimeError(f"Error al guardar partida: {e}")

def cargar_partida(nombre_archivo: str) -> Dict[str, Any]:
    """
    Carga una partida desde un archivo JSON.

    Parámetros:
    -----------
    nombre_archivo : str
        Nombre del archivo de partida a cargar.

    Retorna:
    --------
    Dict[str, Any]
        Diccionario con los datos de la partida cargada.

    Lanza:
    ------
    FileNotFoundError
        Si el archivo no existe.
    """
    nombre_archivo += ".json"
    ruta = os.path.join(PATH_PARTIDAS, nombre_archivo)

    if not os.path.exists(ruta):
        raise FileNotFoundError("La partida no existe.")

    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)
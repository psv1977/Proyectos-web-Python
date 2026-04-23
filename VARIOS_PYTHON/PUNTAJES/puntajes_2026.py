#Este codigo es para ir extrayendo la informacion desde un archivo cvs que contiene los puntajes de la PAES 2026
#en primer lugar hay que cragar el archivo en el código

import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
archivo_csv = BASE_DIR / "ArchivoC_Adm2026REG.csv"

df = pd.read_csv(archivo_csv, sep=";")


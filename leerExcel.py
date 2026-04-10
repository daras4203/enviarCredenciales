import pandas as pd
from config import ARCHIVO_USUARIOS

def cargar_usuarios():
    
    df = pd.read_excel(ARCHIVO_USUARIOS)

    usuarios = []

    for index, row in df.iterrows():

        usuario = {
            "nombre": row["Nombre"],
            "correo": row["email"],
            "password": row["password"]
        }

        usuarios.append(usuario)

    return usuarios
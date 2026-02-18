import pandas as pd
from sodapy import Socrata

def consultar_datos(nombre_departamento, limite_registros):
    client = Socrata("www.datos.gov.co", None)
    
    # IMPORTANTE: Usamos el parámetro 'where' con comillas simples
    # para que la API entienda que buscamos el TEXTO del departamento.
    # Ejemplo: departamento_nom = 'RISARALDA'
    
    filtro = f"departamento_nom = '{nombre_departamento.upper()}'"
    
    results = client.get("gt2j-8ykr", 
                         limit=limite_registros, 
                         where=filtro) # Cambiamos el parámetro directo por 'where'
    
    return pd.DataFrame.from_records(results)
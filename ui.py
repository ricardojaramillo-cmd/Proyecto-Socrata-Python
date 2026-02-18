import pandas as pd

def pedir_parametros():
    departamento = input("Ingrese el nombre del departamento: ")
    while True:
        try:
            limite = int(input("Ingrese el número de registros a consultar: "))
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")
    return departamento, limite

def mostrar_resultados(df):
    if df is None or df.empty:
        print("\n[!] No se encontraron resultados para esta consulta.")
        return

    # 1. Definimos las columnas que queremos (mapeo Técnico -> Usuario)
    columnas_deseadas = {
        'ciudad_municipio_nom': 'Ciudad',
        'departamento_nom': 'Departamento',
        'edad': 'Edad',
        'fuente_tipo_contagio': 'Tipo',
        'estado': 'Estado',
        'pais_viajo_1_nom': 'País Procedencia'
    }

    # 2. El encabezado de la tabla (usando format como pide el requerimiento)
    header_format = "{:<20} | {:<15} | {:<6} | {:<12} | {:<12} | {:<15}"
    print("\n" + "="*95)
    print(header_format.format(*columnas_deseadas.values()))
    print("-" * 95)

    # 3. Recorremos el DataFrame con seguridad
    for _, fila in df.iterrows():
        # Usamos fila.get('columna', 'N/A') para que si la columna NO EXISTE, 
        # el programa no falle y ponga 'N/A' en su lugar.
        print(header_format.format(
            str(fila.get('ciudad_municipio_nom', 'N/A'))[:20],
            str(fila.get('departamento_nom', 'N/A'))[:15],
            str(fila.get('edad', 'N/A')),
            str(fila.get('fuente_tipo_contagio', 'N/A')),
            str(fila.get('estado', 'N/A')),
            str(fila.get('pais_viajo_1_nom', 'N/A'))
        ))
    print("="*95 + "\n")
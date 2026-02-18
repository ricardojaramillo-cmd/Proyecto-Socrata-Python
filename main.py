from api import consultar_datos
from ui import pedir_parametros, mostrar_resultados

def ejecutar_app():
    # 1. Capturar datos del usuario
    depto, limite = pedir_parametros()
    
    print(f"\nConsultando {limite} registros en {depto}...")
    
    try:
        # 2. Obtener datos de la API
        data = consultar_datos(depto, limite)
        
        # 3. Mostrar resultados formateados
        mostrar_resultados(data)
        
    except Exception as e:
        print(f"Ocurrió un error en la consulta: {e}")

if __name__ == "__main__":
    ejecutar_app()
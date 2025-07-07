import requests
from datetime import datetime

FERIADOS_API = 'https://api.boostr.cl/holidays.json'

def verificar_feriado(fecha):
    """Verifica si la fecha es feriado, y si es irrenunciable."""
    try:
        response = requests.get(FERIADOS_API, timeout=10)
        if response.status_code == 200:
            data = response.json().get("data", [])
            fecha_str = fecha.strftime('%Y-%m-%d')
            for feriado in data:
                if feriado["date"] == fecha_str:
                    return {
                        'es_feriado': True,
                        'irrenunciable': feriado["inalienable"],
                        'titulo': feriado["title"]
                    }
    except Exception as e:
        print("Error consultando API de feriados:", e)

    return {
        'es_feriado': False,
        'irrenunciable': False,
        'titulo': None
    }   
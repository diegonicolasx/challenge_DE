import orjson
from typing import List, Tuple
from datetime import datetime
from collections import defaultdict, Counter

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    """
    Función que busca consultar por las 10 fechas en donde más se hicieron tweets,
    junto al usuario que más hizo tweet en cada fecha, que tiene un enfasis
    en ser eficiente utilizando el tiempo, para lo cual, se decidio
    por utilizar la librería orjson para cargar el archivo json, ya que,
    según su documentación, es una librería rápida en cuanto a gestionar el 
    tiempo, debido a que esta escrita en rust.
    La función busca reconocer cada línea del archivo json y eliminar los espacios
    en blanco entre cada objeto json del archivo, para que puedan ser cargados
    mediante el metodo loads().
    """
    with open(file_path, 'rb') as file:
        date_user_count = defaultdict(Counter)

        for line in file:
            cleaned_line = line.strip()  
            data = orjson.loads(cleaned_line)
            current_date = None
            current_username = None            
            #print(data)
            for key in data:
                if key in ["date"]:
                    value = data[key]
                    current_date = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S%z").date()
                elif key in ["user"]:
                    current_username = data[key]["username"]
            
            if current_date and current_username:
                    date_user_count[current_date][current_username] += 1
                    current_date = None
                    current_username = None

        top_ten_dates = sorted(date_user_count.items(), key=lambda x: sum(x[1].values()), reverse=True)[:10]
    
        result = []
        for date, user_counts in top_ten_dates:
            top_user = max(user_counts, key=user_counts.get)
            result.append((date, top_user))
    
        return result
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
    Antes de realizar la carga de datos del archivo json, se establece un contador en formato
    diccionario llamado date_user_count, el cual permitirá contar las veces de ocurrencia de una
    fecha junto a los usuarios, de esta manera se busca obtener el objetivo de la consulta.
    A medida que se va cargando cada objeto json del archivo json, se irá interando
    por sus claves o keys para encontrar las clave que son de "date" y las que son de "user".
    De estas claves se pueden extraer los valores de fecha y de nombre de usuario.
    Cada vez que se repita una fecha junto a un nombre de usuario, se irá agregando un 1
    al contador, de esta manera despues se pueden obtener las fechas mas repetidas junto
    al usuario que mas activo estuvo ese día.
    Al final, se ordenará el diccionario que se creo de acuerdo a la fecha mas repetida
    y se irán almacenando las fechas más repetidas junto al usuario más activo en formato tupla
    dentro de una lista que será el resultado que retorna la función.
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
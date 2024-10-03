import ijson
from typing import List, Tuple
from datetime import datetime
from collections import defaultdict, Counter

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    """
    Función que busca consultar por las 10 fechas en donde más se hicieron tweets,
    junto al usuario que más hizo tweet en cada fecha, que tiene un enfasis
    en ser eficiente utilizando la memoria, para lo cual, se decidio
    por utilizar la librería ijson para cargar el archivo json, ya que,
    según su documentación, es una eficiente en el uso de la memoria, ya que,
    va leyendo cada línea del archvio json en streaming, lo que significa, que 
    no almacena los datos que lee en memoria, por lo que, utiliza poca de esta.
    La función busca reconocer cada línea del archivo json y eliminar los espacios
    en blanco entre cada objeto json del archivo, para que puedan ser cargados
    mediante el metodo parse().
    Antes de realizar la carga de datos del archivo json, se establece un contador en formato
    diccionario llamado date_user_count, el cual permitirá contar las veces de ocurrencia de una
    fecha junto a los usuarios, de esta manera se busca obtener el objetivo de la consulta.
    A medida que se va cargando cada objeto json del archivo json, se irá interando
    por sus "prefix", "event" y "value". Prefix hace referencia a las clave en cada objeto json,
    event al tipo de dato y value al valor que tiene cada clave.
    Con los prefix de "date" se pueden extraer las fechas y con el "prefix" de "user.username"
    se pueden extraer los nombres de usuario.    
    Cada vez que se repita una fecha junto a un nombre de usuario, se irá agregando un 1
    al contador, de esta manera despues se pueden obtener las fechas mas repetidas junto
    al usuario que mas activo estuvo ese día.
    Al final, se ordenará el diccionario que se creo de acuerdo a la fecha mas repetida
    y se irán almacenando las fechas más repetidas junto al usuario más activo en formato tupla
    dentro de una lista que será el resultado que retorna la función.
    """
    date_user_count = defaultdict(Counter)
    
    with open(file_path, 'rb') as file:        
        for line in file:
            cleaned_line = line.strip()             
            parser = ijson.parse(cleaned_line)
            current_date = None
            current_username = None
        
            for prefix, event, value in parser:
                if prefix.endswith('date') and event == 'string':
                    current_date = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S%z").date()
                elif prefix.endswith('user.username') and event == 'string':
                    current_username = value
            
                if current_date and current_username:
                    date_user_count[current_date][current_username] += 1
                    current_date = None
                    current_username = None
    
    # Get the top ten dates by total tweet count
        top_ten_dates = sorted(date_user_count.items(), key=lambda x: sum(x[1].values()), reverse=True)[:10]
    
        result = []
        for date, user_counts in top_ten_dates:
            top_user = max(user_counts, key=user_counts.get)
            result.append((date, top_user))
    
        return result
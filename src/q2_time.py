import orjson
import emoji
from typing import List, Tuple
from collections import Counter

def is_emoji(char):
    return char in emoji.EMOJI_DATA

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    """
    Función que busca consultar por los 10 emojis más utilizados junto a su conteo
    de uso, que tiene un enfasis en ser eficiente utilizando el tiempo, para lo cual, 
    se decidio por utilizar la librería orjson para cargar el archivo json, ya que,
    según su documentación, es una librería rápida en cuanto a gestionar el 
    tiempo, debido a que esta escrita en rust.
    La función busca reconocer cada línea del archivo json y eliminar los espacios
    en blanco entre cada objeto json del archivo, para que puedan ser cargados
    mediante el metodo loads().
    Antes de realizar la carga de datos del archivo json, se crea una fución auxiliar llamada
    is_emoji que permite identificar los emojis dentro de las cadenas de texto que son
    los tweets. Luego, dentro de la función principal se crea un contador para almacenar
    las emojis que se encontrarán en los tweets, esto permitirá luego contar estos mismos emojis
    para poder determinar cuales son los 10 más usados en todos los tweets     
    A medida que se va cargando cada objeto json del archivo json, se irá interando
    por sus claves o keys para encontrar la indicada para obtener el objetivo que se busca,
    la cual es content, que tiene todo el contenido el tweet realizado.
    Con el key de "content" se puede extraer el texto completo del tweet dentro del cual
    se le aplicará la función auxiliar is_emoji para identificar los emojis.
    Cada vez que detecte un emoji con la manera descrita anteriormente, lo almacenará en el objeto contador
    que se creo en un principio, para al final consultar por los 10 más repetidos.
    """
    emoji_counter = Counter()
    
    with open(file_path, 'rb') as file:
        for line in file:
            cleaned_line = line.strip()  
            data = orjson.loads(cleaned_line)

            for key in data:
                if key in ["content"]:
                    tweet = data[key]
                    for i in tweet:
                          if is_emoji(i):                            
                            emoji_counter.update(i)
                            
    return emoji_counter.most_common(10)
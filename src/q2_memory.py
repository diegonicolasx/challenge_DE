import ijson
import emoji
from typing import List, Tuple
from collections import Counter

def is_emoji(char):
    return char in emoji.EMOJI_DATA

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    """
    Función que busca consultar por los 10 emojis más utilizados junto a su conteo
    de uso, que tiene un enfasis en ser eficiente utilizando la memoria, para lo cual, 
    se decidio por utilizar la librería ijson para cargar el archivo json, ya que,
    según su documentación, es una eficiente en el uso de la memoria, ya que,
    va leyendo cada línea del archvio json en streaming, lo que significa, que 
    no almacena los datos que lee en memoria, por lo que, utiliza poca de esta.
    La función busca reconocer cada línea del archivo json y eliminar los espacios
    en blanco entre cada objeto json del archivo, para que puedan ser cargados
    mediante el metodo parse().
    Antes de realizar la carga de datos del archivo json, se crea una fución auxiliar llamada
    is_emoji que permite identificar los emojis dentro de las cadenas de texto que son
    los tweets. Luego, dentro de la función principal se crea un contador para almacenar
    las emojis que se encontrarán en los tweets, esto permitirá luego contar estos mismos emojis
    para poder determinar cuales son los 10 más usados en todos los tweets     
    A medida que se va cargando cada objeto json del archivo json, se irá interando
    por sus "prefix", "event" y "value". Prefix hace referencia a las clave en cada objeto json,
    event al tipo de dato y value al valor que tiene cada clave.
    Con el prefix de "content" se puede extraer el texto completo del tweet dentro del cual
    se le aplicará la función auxiliar is_emoji para identificar los emojis.
    Cada vez que detecte un emoji con la manera descrita anteriormente, lo almacenará en el objeto contador
    que se creo en un principio, para al final consultar por los 10 más usados.
    """
    emoji_counter = Counter()

    with open(file_path, 'rb') as file:        
        for line in file:
            cleaned_line = line.strip()             
            parser = ijson.parse(cleaned_line)

            for prefix, event, value in parser:
                if prefix.endswith("content"):
                    tweet = value
                    for i in tweet:
                        if is_emoji(i):                            
                            emoji_counter.update(i)
                            
    return emoji_counter.most_common(10)
                            
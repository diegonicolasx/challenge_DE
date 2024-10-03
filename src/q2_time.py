import orjson
import emoji
from typing import List, Tuple
from collections import defaultdict, Counter

def is_emoji(char):
    return char in emoji.EMOJI_DATA

def q2_time(file_path: str) -> List[Tuple[str, int]]:
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
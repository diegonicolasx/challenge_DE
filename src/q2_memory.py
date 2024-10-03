import ijson
import emoji
from typing import List, Tuple
from collections import Counter

def is_emoji(char):
    return char in emoji.EMOJI_DATA

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
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
                            
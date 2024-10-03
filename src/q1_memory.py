import ijson
from typing import List, Tuple
from datetime import datetime
from collections import defaultdict, Counter

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
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
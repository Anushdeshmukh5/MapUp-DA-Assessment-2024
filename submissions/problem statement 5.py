import re
from typing import List

def find_all_dates(text: str) -> List[str]:
   
    patterns = [
        r'\b(\d{2})-(\d{2})-(\d{4})\b',  # dd-mm-yyyy
        r'\b(\d{2})/(\d{2})/(\d{4})\b',  # mm/dd/yyyy
        r'\b(\d{4})\.(\d{2})\.(\d{2})\b'   # yyyy.mm.dd
    ]
    
   
    combined_pattern = '|'.join(patterns)
   
    matches = re.findall(combined_pattern, text)
    
    
    valid_dates = []
    for match in matches:
       
        if match[0]:  # dd-mm-yyyy
            valid_dates.append(f"{match[0]}-{match[1]}-{match[2]}")
        elif match[3]:  # mm/dd/yyyy
            valid_dates.append(f"{match[3]}/{match[4]}/{match[5]}")
        elif match[6]:  # yyyy.mm.dd
            valid_dates.append(f"{match[6]}.{match[7]}.{match[8]}")
    
    return valid_dates

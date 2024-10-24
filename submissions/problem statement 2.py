from typing import List, Dict

def group_by_length(lst: List[str]) -> Dict[int, List[str]]:
   
    length_dict = {}
    
    for string in lst:
        length = len(string)
        if length not in length_dict:
            length_dict[length] = []
        length_dict[length].append(string)
    
    return dict(sorted(length_dict.items()))


from typing import Dict, Any

def flatten_dict(nested_dict: Dict[str, Any], sep: str = '.') -> Dict[str, Any]:
  
    def _flatten(current_dict, parent_key=''):
        items = []
        for k, v in current_dict.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
              
                items.extend(_flatten(v, new_key).items())
            elif isinstance(v, list):
                               for i, item in enumerate(v):
                    if isinstance(item, dict):
                        items.extend(_flatten(item, f"{new_key}[{i}]").items())
                    else:
                        items.append((f"{new_key}[{i}]", item))
            else:
                                items.append((new_key, v))
        return dict(items)
    
    return _flatten(nested_dict)


import pandas as pd
import numpy as np

def find_ids_within_ten_percentage_threshold(df: pd.DataFrame, reference_id: int) -> pd.DataFrame:
  
    
    reference_avg = df[df['id_start'] == reference_id]['distance'].mean()
    
    if np.isnan(reference_avg):  
        return pd.DataFrame(columns=['id_start', 'average_distance']) 
    
   
    lower_bound = reference_avg * 0.9
    upper_bound = reference_avg * 1.1
    
    
    average_distances = df.groupby('id_start')['distance'].mean().reset_index()
    
    
    filtered_ids = average_distances[(average_distances['distance'] >= lower_bound) & 
                                      (average_distances['distance'] <= upper_bound)]
    
    
    sorted_ids = filtered_ids.sort_values(by='distance')
    
    return sorted_ids

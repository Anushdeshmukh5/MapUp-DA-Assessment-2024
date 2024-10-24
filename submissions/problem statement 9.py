import pandas as pd

def calculate_distance_matrix(df: pd.DataFrame) -> pd.DataFrame:
   
    unique_ids = pd.unique(df[['id', 'id_2']].values.ravel('K'))
    
    distance_matrix = pd.DataFrame(0, index=unique_ids, columns=unique_ids)

    for _, row in df.iterrows():
        id1 = row['id']
        id2 = row['id_2']
        distance = row['distance']  
        
        distance_matrix.at[id1, id2] = distance
        distance_matrix.at[id2, id1] = distance  

    
    for k in unique_ids:
        for i in unique_ids:
            for j in unique_ids:
                if distance_matrix.at[i, j] > distance_matrix.at[i, k] + distance_matrix.at[k, j]:
                    distance_matrix.at[i, j] = distance_matrix.at[i, k] + distance_matrix.at[k, j]

    return distance_matrix



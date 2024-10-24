import pandas as pd

def unroll_distance_matrix(df: pd.DataFrame) -> pd.DataFrame:
   
    unrolled_data = []

       for id_start in df.index:
        for id_end in df.columns:
           
            if id_start != id_end:
                distance = df.at[id_start, id_end]
               
                unrolled_data.append({'id_start': id_start, 'id_end': id_end, 'distance': distance})

   
    unrolled_df = pd.DataFrame(unrolled_data)

    return unrolled_df

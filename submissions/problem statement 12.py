import pandas as pd

def calculate_toll_rate(df: pd.DataFrame) -> pd.DataFrame:
    
   
    rate_coefficients = {
        'moto': 0.8,
        'car': 1.2,
        'rv': 1.5,
        'bus': 2.2,
        'truck': 3.6
    }

  
    for vehicle, rate in rate_coefficients.items():
        df[vehicle] = df['distance'] * rate

    return df

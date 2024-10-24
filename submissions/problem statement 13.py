import pandas as pd
import numpy as np
from datetime import time

def calculate_time_based_toll_rates(df: pd.DataFrame) -> pd.DataFrame:
  
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
   
    df['start_day'] = np.random.choice(days, size=len(df))  
    df['end_day'] = np.random.choice(days, size=len(df))
    
   
    df['start_time'] = pd.to_datetime(['00:00:00']*len(df)).dt.time
    df['end_time'] = pd.to_datetime(['23:59:59']*len(df)).dt.time

    
    def apply_discount(row):
       
        if row['start_day'] in days[:5]:  
            if row['start_time'] >= time(0, 0) and row['start_time'] < time(10, 0):
                discount_factor = 0.8
            elif row['start_time'] >= time(10, 0) and row['start_time'] < time(18, 0):
                discount_factor = 1.2
            elif row['start_time'] >= time(18, 0) and row['start_time'] <= time(23, 59):
                discount_factor = 0.8
        else:  
            discount_factor = 0.7

      
        for vehicle in ['moto', 'car', 'rv', 'bus', 'truck']:
            row[vehicle] *= discount_factor
        
        return row

    
    df = df.apply(apply_discount, axis=1)
    
    return df


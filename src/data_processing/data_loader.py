import pandas as pd
import numpy as np

def load_data(path='../data/raw/combined_data.csv'):
    df = pd.read_csv(path)
    return df

def preprocess(df):
    df.dropna(subset=["Value"], inplace=True)
    
    df['Time'] = pd.to_datetime(df['Time'], format='%H:%M', errors='coerce')
    df = df[df['Time'].notna()]
    
    df['Hour'] = df['Time'].dt.hour
    df['Minute'] = df['Time'].dt.minute
    
    df['Hour_sin'] = np.sin(2 * np.pi * df['Hour'] / 24)
    df['Hour_cos'] = np.cos(2 * np.pi * df['Hour'] / 24)
    df['Min_sin']  = np.sin(2 * np.pi * df['Minute'] / 60)
    df['Min_cos']  = np.cos(2 * np.pi * df['Minute'] / 60)
    
    df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
    df.dropna(subset=["Value"], inplace=True)
    
    X = df[["Code", "Hour_sin", "Hour_cos", "Min_sin", "Min_cos"]]
    y = df[["Value"]]
    
    return X, y



# import tarfile
# import os
# import pandas as pd

# def extract_and_combine(file_path, extract_to_folder='data/extracted', output_csv='combined_data.csv'):
#     try:
#         with tarfile.open(file_path, 'r') as tar:
#             tar.extractall(path=extract_to_folder)
        
#         file_names = [f for f in os.listdir(extract_to_folder) if f.startswith('data-')]
        
#         if not file_names:
#             print("No 'data-' files found in the extracted folder.")
#             return

#         dataframes = []
#         for f in file_names:
#             df = pd.read_csv(os.path.join(extract_to_folder, f), delimiter='\t', header=None)
#             df.columns = ['Date', 'Time', 'Code', 'Value']
#             dataframes.append(df)
        
#         if dataframes:
#             combined_df = pd.concat(dataframes, ignore_index=True)
#             combined_df.to_csv(output_csv, index=False)
#             print(f"Combined CSV file saved as: {output_csv}")
#         else:
#             print("No data files were combined.")
    
#     except Exception as e:
#         print(f"Error: {str(e)}")

# extract_and_combine('data/raw/diabetes-data.tar', extract_to_folder='data/extracted/Diabetes-Data', output_csv='data/raw/combined_data.csv')

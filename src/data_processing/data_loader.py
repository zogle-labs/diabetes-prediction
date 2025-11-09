import tarfile
import os
import pandas as pd

def extract_and_combine(file_path, extract_to_folder='data/extracted', output_csv='combined_data.csv'):
    try:
        with tarfile.open(file_path, 'r') as tar:
            tar.extractall(path=extract_to_folder)
        
        file_names = [f for f in os.listdir(extract_to_folder) if f.startswith('data-')]
        
        if not file_names:
            print("No 'data-' files found in the extracted folder.")
            return

        dataframes = [pd.read_csv(os.path.join(extract_to_folder, f), delimiter='\t', header=None) for f in file_names]
        if dataframes:
            pd.concat(dataframes, ignore_index=True).to_csv(output_csv, index=False)
            print(f"Combined CSV file saved as: {output_csv}")
        else:
            print("No data files were combined.")
    
    except Exception as e:
        print(f"Error: {str(e)}")

extract_and_combine('data/raw/diabetes-data.tar', extract_to_folder='data/extracted/Diabetes-Data', output_csv='data/raw/combined_data.csv')

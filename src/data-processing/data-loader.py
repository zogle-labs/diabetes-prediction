import tarfile
import os
import pandas as pd

def count_and_extract_files(file_path, extract_to_folder='data/extracted'):
    try:
        with tarfile.open(file_path, 'r') as tar:
            file_list = tar.getnames()
            tar.extractall(path=extract_to_folder)
            num_files = len(file_list)
            
            return num_files, file_list
    except Exception as e:
        return str(e), []

def combine_files_to_csv(extracted_folder='data/extracted/Diabetes-Data', output_csv='combined_data.csv'):
    try:
        file_names = [f for f in os.listdir(extracted_folder) if f.startswith('data-')]
        if not file_names:
            print("No 'data-' files found in the extracted folder.")
            return

        dataframes = []
        for file_name in file_names:
            file_path = os.path.join(extracted_folder, file_name)

            try:
                df = pd.read_csv(file_path, delimiter='\t', header=None) 
                dataframes.append(df)
            except Exception as e:
                print(f"Error reading {file_name}: {str(e)}")
        
        if dataframes:
            combined_df = pd.concat(dataframes, ignore_index=True)
            combined_df.to_csv(output_csv, index=False)
            print(f"Combined CSV file saved as: {output_csv}")
        else:
            print("No data files were combined.")
        
    except Exception as e:
        print(f"Error occurred during file combination: {str(e)}")


file_path = 'data/raw/diabetes-data.tar'
num_files, file_list = count_and_extract_files(file_path)

print(f"Number of files in the tar archive: {num_files}")
print("First few files in the archive:", file_list[:5])

# Combine the extracted files into a single CSV file
combine_files_to_csv(extracted_folder='data/extracted/Diabetes-Data', output_csv='data/raw/combined_data.csv')

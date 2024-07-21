# Loading the Data
import pandas as pd
import glob
import os

file_path = 'dataset/'

all_files = glob.glob(os.path.join(file_path, "*.tsv"))

combined_df = pd.DataFrame()

for file in all_files:
    df = pd.read_csv(file, sep='\t')
    combined_df = pd.concat([combined_df, df], ignore_index=True)

print("Combined DataFrame:")
df = combined_df
print(df.head())

import pandas as pd
import glob

# Define the pattern to match the filenames
file_pattern = 'invoices/*.xlsx'

# Use glob to get a list of filenames matching the pattern
file_list = glob.glob(file_pattern)


# Loop through the filenames and read them into DataFrames
for file in file_list:
    df = pd.read_excel(file,sheet_name="Sheet 1")
    print(df)



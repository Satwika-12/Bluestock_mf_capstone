
import pandas as pd
from pathlib import Path

# Location of the downloaded datasets
raw_folder = Path("data/raw")

# Get all CSV files from the folder
csv_files = list(raw_folder.glob("*.csv"))

print("Number of CSV files:", len(csv_files))

# Read and inspect each dataset
for csv_file in sorted(csv_files):
    print("\n" + "-" * 50)
    print("Dataset:", csv_file.name)

    data = pd.read_csv(csv_file)

    print("Rows and columns:", data.shape)
    print("\nColumn names and data types:")
    print(data.dtypes)

    print("\nFirst five records:")
    print(data.head())
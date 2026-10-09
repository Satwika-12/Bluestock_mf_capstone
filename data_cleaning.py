import pandas as pd
from pathlib import Path

raw_folder = Path("data/raw")
csv_files = list(raw_folder.glob("*.csv"))

print("=== Checking Missing Values & Duplicates ===")
for csv_file in sorted(csv_files):
    df = pd.read_csv(csv_file)
    
    missing_count = df.isnull().sum().sum()
    duplicate_count = df.duplicated().sum()
    
    print(f"File: {csv_file.name}")
    print(f"   Missing Values: {missing_count}")
    print(f"   Duplicate Rows: {duplicate_count}")
    print("-" * 40)
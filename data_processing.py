import pandas as pd
from pathlib import Path

raw_folder = Path("data/raw")
processed_folder = Path("data/processed")
processed_folder.mkdir(parents=True, exist_ok=True)

csv_files = list(raw_folder.glob("*.csv"))

print("=== Processing & Saving to Processed Folder ===")
for csv_file in csv_files:
    df = pd.read_csv(csv_file)
    
    # Simple data cleaning: drop completely empty rows/columns if any
    df = df.dropna(how='all')
    
    # Save to processed folder
    output_path = processed_folder / csv_file.name
    df.to_csv(output_path, index=False)
    print(f"Processed and saved: {csv_file.name}")

print("\nAll datasets processed successfully!")
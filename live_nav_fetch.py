
import requests
import pandas as pd
from pathlib import Path

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url, timeout=30)
response.raise_for_status()

data = response.json()

nav_data = pd.DataFrame(data["data"])

output_dir = Path("Data/raw")
output_dir.mkdir(parents=True, exist_ok=True)

output_file = output_dir / "hdfc_top100_direct_nav.csv"
nav_data.to_csv(output_file, index=False)

print("Scheme:", data["meta"]["scheme_name"])
print("Records:", len(nav_data))
print("Saved to:", output_file)
print(nav_data.head())



import requests
import pandas as pd
from pathlib import Path

scheme_ids = [125497, 119551, 120503, 118632, 119092, 120841]

output_dir = Path("Data/raw")
output_dir.mkdir(parents=True, exist_ok=True)

for scheme_id in scheme_ids:
    url = f"https://api.mfapi.in/mf/{scheme_id}"
    
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    
    data = response.json()
    nav_data = pd.DataFrame(data["data"])
    
    # Scheme name ni clean chesi safe filename ga convert cheyyadam
    scheme_name = data['meta']['scheme_name']
    safe_name = "".join(c if c.isalnum() else "_" for c in scheme_name.lower())
    
    output_file = output_dir / f"{safe_name}_nav.csv"
    nav_data.to_csv(output_file, index=False)
    
    print(f"Scheme: {scheme_name}")
    print(f"Records: {len(nav_data)}")
    print(f"Saved to: {output_file}\n" + "-"*40)
import pandas as pd
from pathlib import Path
from ydata_profiling import ProfileReport

data_dir = Path("data")

for csv_file in data_dir.glob("*.csv"):
    print(f"Generating report for {csv_file.name}...")

    df = pd.read_csv(csv_file, low_memory=False, on_bad_lines="skip",)

    ProfileReport(
        df,
        title=csv_file.stem,
        explorative=True,
        minimal=True,
    ).to_file(data_dir / f"{csv_file.stem}_eda.html")

print("Done!")

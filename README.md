# Readme

Generates exploratory data analysis (EDA) reports for CSV files using [ydata-profiling](https://github.com/ydataai/ydata-profiling).

## What it does

`script.py` scans the `data/` directory for `*.csv` files, loads each one into a pandas DataFrame, and produces a minimal `ydata-profiling` HTML report next to the source file (e.g. `constituent.csv` → `constituent_eda.html`).

## Requirements

- Python 3.11.11 (see `.python-version`)
- Dependencies listed in `requirements.txt`:
  - `pandas`
  - `ydata-profiling`
  - `setuptools`

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

1. Place the CSV files you want profiled into the `data/` directory.
2. Run the script:

   ```bash
   python script.py
   ```
3. An `<name>_eda.html` report is generated for each CSV in `data/`.

## Notes

- Malformed rows in the CSVs are skipped (`on_bad_lines="skip"`).
- `data_old/` contains a previous batch of source CSVs and their generated reports, kept for reference.

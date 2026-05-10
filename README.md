# FYP

This repository contains the current working code and supporting documents for an FYP focused on identifying suitable solar farm locations using geospatial analysis and predicted solar energy availability.

## Current scope

The code currently in the repository covers early-stage data access and regional aggregation for NASA POWER datasets. The main notebook:

- opens the NASA POWER `SYN1DEG` and `MERRA2` daily temporal Zarr datasets
- extracts selected solar and meteorological variables
- aggregates those variables over:
  - Peninsular Malaysia
  - East Malaysia
  - USA

This is the data preparation stage for later modelling and GIS-based analysis.

## Repository structure

```text
FYP/
|-- notebooks/
|   |-- nasa_power_data_understanding.ipynb
|   `-- data_preparation_&_modelling.ipynb
|-- docs/
|   |-- reviews/
|   |   `-- Amir_IR_Fixes_and_Suggestions_Highlighted.docx
|   `-- data_exploration_report.md
|-- .gitignore
|-- README.md
`-- requirements.txt
```

## Requirements

Install the current notebook dependencies with:

```bash
pip install -r requirements.txt
```

## Notes

- `notebooks/nasa_power_data_understanding.ipynb` is the main notebook — it covers data access, regional aggregation, and full exploratory analysis across all three regions.
- `docs/reviews/Amir_IR_Fixes_and_Suggestions_Highlighted.docx` contains highlighted IR review suggestions and is kept under `docs/` instead of the repo root.

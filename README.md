# regenerative-data-enrichment-oracle-v1
Minimal working prototype of the Situated Insight Climate-Enrichment Oracle v1.0. Processes land steward practice logs with climate-derived Disease Favorability Index (DFI) anomalies using Python, xarray, and NetCDF datasets. Demonstrates DAO-ready enrichment pipelines for regenerative data infrastructure.

# Disease Anomaly Enrichment Pipeline

This repository implements a minimal working example of the Situated Insight Climate-Enrichment Oracle v1.0 for DAO-oriented regenerative data pipelines.

## Overview

This pipeline performs enrichment of land steward practice logs with climate-derived Disease Favorability Index (DFI) anomalies.

- ✅ Practice logs contain planting dates.
- ✅ Climate data includes temperature and precipitation.
- ✅ The pipeline calculates a disease pressure score based on warmth and moisture during the first 30 days after planting.
- ✅ Anomalies are calculated relative to a climatological baseline (1981–2010).
- ✅ Output includes enriched logs suitable for DAO-level integration.

## Pipeline Structure

/data/
    practice_logs.csv
    /climate_data/
        temperature_sample.nc
        precipitation_sample.nc

/enrichment/
    climate_loader.py
    climatology.py
    dfi_calc.py
    enrichment_oracle.py
    run_enrichment.py

/utils/
    config.py

## Dependencies

Install Python dependencies via:
pip install -r requirements.txt

## Usage
Simply run the enrichment pipeline:
python enrichment/run_enrichment.py

## Future Extensions

- Multi-variable oracles
- Bioregional DAO integration
- Smart contract triggers
- Multi-agent pipeline architecture
- Expanded climate datasets (ERA5, CHIRPS, MODIS NDVI, etc)

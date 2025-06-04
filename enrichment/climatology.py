import numpy as np

def calculate_climatology(climate_ds, baseline_years):
    baseline = climate_ds.sel(time=slice(f"{baseline_years[0]}-01-01", f"{baseline_years[1]}-12-31"))
    climatology_mean = baseline.groupby("time.dayofyear").mean("time")
    return climatology_mean

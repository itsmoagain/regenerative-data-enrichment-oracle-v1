import numpy as np
import pandas as pd
from datetime import timedelta

def compute_dfi(precip_ts, temp_ts, window_days, precip_threshold, temp_min, temp_max):
    dfi = 0
    for date in precip_ts.time.values:
        prec = precip_ts.sel(time=date).values.item()
        temp = temp_ts.sel(time=date).values.item()

        if prec > precip_threshold and (temp_min <= temp <= temp_max):
            dfi += 1
    return dfi

def generate_dfi_anomaly(practice_row, precip_ds, temp_ds, climatology, params):
    date = pd.to_datetime(practice_row['date'])
    lat = practice_row['lat']
    lon = practice_row['lon']

    # Subset nearest grid point
    precip_point = precip_ds.sel(lat=lat, lon=lon, method="nearest")
    temp_point = temp_ds.sel(lat=lat, lon=lon, method="nearest")

    # Extract window
    window = pd.date_range(date, date + timedelta(days=params['window_days']))
    precip_window = precip_point.sel(time=window)
    temp_window = temp_point.sel(time=window)

    # Calculate DFI for this planting
    observed_dfi = compute_dfi(precip_window, temp_window, params['window_days'],
                                params['precip_threshold'], params['temp_min'], params['temp_max'])

    # Get climatology for this window (simplified to DOY matching)
    doy = date.dayofyear
    clim_mean = climatology.sel(dayofyear=doy).values.item()

    anomaly = observed_dfi - clim_mean

    return observed_dfi, clim_mean, anomaly

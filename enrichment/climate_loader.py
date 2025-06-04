import xarray as xr
from utils import config

def load_precip_data():
    filepath = f"{config.CLIMATE_DATA_DIR}/precipitation_sample.nc"
    precip_ds = xr.open_dataset(filepath)
    return precip_ds

def load_temp_data():
    filepath = f"{config.CLIMATE_DATA_DIR}/temperature_sample.nc"
    temp_ds = xr.open_dataset(filepath)
    return temp_ds

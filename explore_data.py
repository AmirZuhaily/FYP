import pandas as pd
import s3fs
import xarray as xr

def main():
    print("Connecting to S3...")
    fs = s3fs.S3FileSystem(anon=True)

    SYN1DEG_DAILY = "s3://nasa-power/syn1deg/temporal/power_syn1deg_daily_temporal_utc.zarr"
    MERRA2_DAILY = "s3://nasa-power/merra2/temporal/power_merra2_daily_temporal_utc.zarr"

    print("Opening Zarr datasets...")
    syn_ds = xr.open_zarr(SYN1DEG_DAILY, storage_options={"anon": True})
    merra_ds = xr.open_zarr(MERRA2_DAILY, storage_options={"anon": True})

    print("Selecting Peninsular Malaysia and slicing time to 2020...")
    bounds = {
        "lat_min": 1,
        "lat_max": 8,
        "lon_min": 98,
        "lon_max": 105
    }

    # Slice region and time
    syn_region = syn_ds.sel(
        lat=slice(bounds["lat_min"], bounds["lat_max"]),
        lon=slice(bounds["lon_min"], bounds["lon_max"]),
        time=slice("2020-01-01", "2020-12-31")
    )
    
    merra_region = merra_ds.sel(
        lat=slice(bounds["lat_min"], bounds["lat_max"]),
        lon=slice(bounds["lon_min"], bounds["lon_max"]),
        time=slice("2020-01-01", "2020-12-31")
    )

    SYN1DEG_VARS = ["ALLSKY_SFC_SW_DWN", "CLOUD_AMT", "AOD_55", "PW", "ALLSKY_KT", "PSH"]
    MERRA2_VARS = ["RH2M", "WS2M", "T2M_MAX", "PS"]

    print("Aggregating data...")
    syn_data = {}
    for var in SYN1DEG_VARS:
        syn_data[var] = syn_region[var].mean(dim=["lat", "lon"]).to_series()
        
    merra_data = {}
    for var in MERRA2_VARS:
        merra_data[var] = merra_region[var].mean(dim=["lat", "lon"]).to_series()

    df_syn = pd.DataFrame(syn_data)
    df_merra = pd.DataFrame(merra_data)

    df_combined = pd.concat([df_syn, df_merra], axis=1).dropna()

    print("\n--- Data Exploration ---")
    print("\n1. Basic Information:")
    print(df_combined.info())
    
    print("\n2. Summary Statistics:")
    print(df_combined.describe().to_string())
    
    print("\n3. Correlation Matrix:")
    print(df_combined.corr().to_string())
    
    print("\n4. Missing Values:")
    print(df_combined.isnull().sum().to_string())

if __name__ == "__main__":
    main()

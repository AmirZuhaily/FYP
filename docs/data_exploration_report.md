# Data Exploration & Understanding Report

## Overview
This report details the findings from the data exploration of the NASA POWER `SYN1DEG` and `MERRA2` daily datasets, specifically focusing on the **Peninsular Malaysia** region for the year **2020**. 

The goal of this exploration is to understand the distribution, quality, and relationships of solar and meteorological variables to identify suitable parameters for solar farm location analysis.

## 1. Dataset Characteristics
The aggregated dataset contains 366 daily observations (Year 2020) for the following variables:
- **SYN1DEG**: `ALLSKY_SFC_SW_DWN` (GHI/Target), `CLOUD_AMT`, `AOD_55`, `PW`, `ALLSKY_KT`, `PSH`
- **MERRA2**: `RH2M`, `WS2M`, `T2M_MAX`, `PS`

### Missing Values
A check for missing values indicates that there are **0 missing values** across all aggregated variables. The data is complete for the specified timeframe and region.

## 2. Summary Statistics
The table below summarizes the key statistical properties of the variables over Peninsular Malaysia:

| Variable | Mean | Std Dev | Min | Max | Description |
|---|---|---|---|---|---|
| **ALLSKY_SFC_SW_DWN** | 16.58 | 2.50 | 7.95 | 23.35 | Global Horizontal Irradiance (kWh/m²/day) |
| **CLOUD_AMT** | 76.51 | 6.78 | 51.68 | 91.80 | Cloud Amount (%) |
| **AOD_55** | 0.20 | 0.08 | 0.07 | 0.65 | Aerosol Optical Depth |
| **PW** | 5.37 | 0.26 | 4.39 | 5.92 | Precipitable Water (cm) |
| **ALLSKY_KT** | 0.45 | 0.07 | 0.22 | 0.64 | Clearness Index |
| **PSH** | 4.60 | 0.69 | 2.21 | 6.48 | Peak Sun Hours |
| **RH2M** | 85.34 | 2.37 | 78.47 | 91.07 | Relative Humidity at 2m (%) |
| **WS2M** | 1.83 | 0.40 | 1.09 | 3.42 | Wind Speed at 2m (m/s) |
| **T2M_MAX** | 29.89 | 0.77 | 27.63 | 31.95 | Max Temperature at 2m (°C) |
| **PS** | 992.51 | 1.25 | 988.66 | 996.34 | Surface Pressure (kPa) |

*Observations:*
- **Solar Irradiance:** The mean `ALLSKY_SFC_SW_DWN` is 16.58, with significant variance indicating seasonal or weather-driven fluctuations.
- **Cloud Cover:** Average cloud amount is consistently high (~76%), typical for a tropical region like Malaysia.

## 3. Correlation Analysis
A correlation matrix was computed to understand the linear relationships between the target variable (`ALLSKY_SFC_SW_DWN`) and meteorological predictors.

### Positive Correlations with GHI (`ALLSKY_SFC_SW_DWN`)
- **`ALLSKY_KT` (0.978)**: Almost perfect positive correlation, as the clearness index directly governs how much solar radiation reaches the surface.
- **`PSH` (1.000)**: Peak Sun Hours are perfectly correlated since it is derived directly from GHI.
- **`T2M_MAX` (0.646)**: Higher solar irradiance naturally leads to higher daily maximum temperatures.

### Negative Correlations with GHI
- **`CLOUD_AMT` (-0.745)**: Strong negative correlation; increased cloud cover significantly reduces solar irradiance reaching the ground.
- **`RH2M` (-0.600)**: Higher relative humidity is often associated with more cloud cover and precipitation, thus lowering solar irradiance.
- **`PW` (-0.586)**: More precipitable water in the atmosphere scatters and absorbs solar radiation.
- **`AOD_55` (-0.415)**: Higher aerosol optical depth (air pollution/particulates) mildly reduces GHI.

## Conclusion
The data exploration confirms that the target variable `ALLSKY_SFC_SW_DWN` is highly dependent on `CLOUD_AMT`, `ALLSKY_KT`, and `RH2M`. The dataset is clean with no missing values at the regional aggregation level, making it highly suitable for training machine learning models to predict solar energy availability. Next steps should involve incorporating spatial variation (grid-level analysis) rather than regional averages, to pinpoint exact suitable solar farm locations.

# Time Series Analysis and Forecasting for Stock Market: Apple (AAPL) & Tesla (TSLA)

**Prepared by:** Krishna Shukla
**Date:** 30-11-2025

## 1. Introduction
This project analyses historical stock prices of Apple Inc. (AAPL) and Tesla, Inc. (TSLA) using time series forecasting techniques: ARIMA, SARIMA, Prophet, and LSTM.

## 2. Dataset
Source: Yahoo Finance (via yfinance).
We use 'Close' price, resampled to business days and forward-filled for missing entries.

## 3. Preprocessing
- Read CSV and set datetime index.
- Resample to business days: `.asfreq('B').ffill()`
- Visualize closing price, returns, log-returns, rolling mean and std.
- Perform ADF test to check stationarity.

## 4. Models
- ARIMA: handles autoregression and moving-average structure.
- SARIMA: ARIMA with seasonality component.
- Prophet: flexible model for multiple seasonalities and changepoints.
- LSTM: deep learning sequence model using past 60 days.

## 5. Evaluation
Metrics: MAE and RMSE on last 60 business days (or 20% of series).

## 6. Results
(After running, paste metrics from `results/<TICKER>/metrics.json` here and include `forecast_plot.png`.)

## 7. Conclusion & Future Work
- Summarize which model performed best for each ticker.
- Discuss limitations: market volatility, news events, small test window.
- Future work: ensemble methods, include technical indicators or news sentiment, hyperparameter tuning.

## References
- Project brief provided by instructor.
- yfinance, statsmodels, Prophet, TensorFlow docs.

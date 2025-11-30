#!/usr/bin/env python3
"""
Fully working pipeline WITHOUT LSTM and WITHOUT Prophet.
This works on ANY laptop (Windows/Linux/Mac).
"""

import os, argparse, warnings, json
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_absolute_error, mean_squared_error

def load_csv(path):
    return pd.read_csv(path, parse_dates=True, index_col=0)

def resample_close(df):
    df = df.asfreq('B').ffill()
    return df['Close']

def train_arima(series):
    model = ARIMA(series, order=(5,1,0)).fit()
    return model

def train_sarima(series):
    model = SARIMAX(series, order=(1,1,1), seasonal_order=(1,1,1,5)).fit(disp=False)
    return model

def forecast(model, steps):
    return model.forecast(steps=steps)

def evaluate(true, pred):
    mae = mean_absolute_error(true, pred)
    mse = mean_squared_error(true, pred)
    rmse = np.sqrt(mse)
    return mae, rmse

def plot_forecasts(series, test, forecasts, outpath):
    plt.figure(figsize=(12,6))
    plt.plot(series.index, series.values, label="Actual", linewidth=1.5)
    for name, fc in forecasts.items():
        plt.plot(test.index, fc.values, label=name)
    plt.legend()
    plt.savefig(outpath)
    plt.close()

def run_pipeline(csv_path, output_dir='results'):

    os.makedirs(output_dir, exist_ok=True)

    df = load_csv(csv_path)
    series = resample_close(df)

    test_len = max(30, int(len(series)*0.2))
    train = series[:-test_len]
    test = series[-test_len:]

    results = {}
    forecasts = {}

    # ARIMA
    arima = train_arima(train)
    arima_fc = forecast(arima, len(test))
    arima_fc = pd.Series(arima_fc, index=test.index)
    results["ARIMA"] = dict(zip(["mae","rmse"], evaluate(test, arima_fc)))
    forecasts["ARIMA"] = arima_fc

    # SARIMA
    sarima = train_sarima(train)
    sarima_fc = forecast(sarima, len(test))
    sarima_fc = pd.Series(sarima_fc, index=test.index)
    results["SARIMA"] = dict(zip(["mae","rmse"], evaluate(test, sarima_fc)))
    forecasts["SARIMA"] = sarima_fc

    json.dump(results, open(os.path.join(output_dir, "metrics.json"), "w"), indent=2)

    plot_forecasts(series, test, forecasts, os.path.join(output_dir, "forecast_plot.png"))

    print("Saved:", output_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_csv", required=True)
    parser.add_argument("--output_dir", default="results")
    args = parser.parse_args()
    run_pipeline(args.input_csv, args.output_dir)

#!/usr/bin/env python3
"""
download_data.py
Download historical stock data using yfinance and save as CSV files per ticker.
Usage: python download_data.py --tickers AAPL TSLA --start 2018-01-01 --end 2025-11-28
"""
import argparse, os
import yfinance as yf
import pandas as pd

def download(ticker, start, end, interval='1d', outdir='data'):
    os.makedirs(outdir, exist_ok=True)
    df = yf.download(ticker, start=start, end=end, interval=interval, progress=False)
    if df.empty:
        print(f"No data for {ticker} in range {start} to {end}.")
        return
    df.to_csv(os.path.join(outdir, f"{ticker}.csv"))
    print(f"Saved {ticker} -> {outdir}/{ticker}.csv")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--tickers', nargs='+', required=True)
    parser.add_argument('--start', default='2018-01-01')
    parser.add_argument('--end', default='2025-11-28')
    parser.add_argument('--outdir', default='data')
    args = parser.parse_args()
    for t in args.tickers:
        download(t, args.start, args.end, outdir=args.outdir)

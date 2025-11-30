#!/bin/bash
python3 download_data.py --tickers AAPL TSLA --start 2018-01-01 --end 2025-11-28 --outdir data
python3 modeling_pipeline.py --input_csv data/AAPL.csv --output_dir results/AAPL
python3 modeling_pipeline.py --input_csv data/TSLA.csv --output_dir results/TSLA

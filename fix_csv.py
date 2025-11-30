import pandas as pd
import sys

input_path = sys.argv[1]
output_path = sys.argv[2]

# Read the CSV normally
df = pd.read_csv(input_path, header=None)

# Drop first 2 useless rows: Ticker row + the 'Date,,,,,' row
df = df.drop(index=[1, 2])

# Set the first row as header
df.columns = df.iloc[0]
df = df.drop(index=0)

# Now rename the first column to 'Date'
df = df.rename(columns={df.columns[0]: "Date"})

# Convert date column
df["Date"] = pd.to_datetime(df["Date"])

# Set index
df = df.set_index("Date")

# Save cleaned CSV
df.to_csv(output_path)

print("✔ Clean CSV saved to:", output_path)


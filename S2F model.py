# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 13:32:01 2023

@author: Lenovo
"""
import json
import requests
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Define the function to fit the data
def s2f_model(x, a, b):
  return a * x + b

# Extract the data from the Bitcoin Core RPC API
url = "http://bitcoin:password@localhost:8332"
headers = {'content-type': 'application/json'}

# Get the current block count
payload = {
  "method": "getblockcount",
  "params": []
}
response = requests.post(url, data=json.dumps(payload), headers=headers).json()
block_count = response['result']

# Extract the data for each block
data = []
for block_height in range(block_count):
  # Get the block hash
  payload = {
    "method": "getblockhash",
    "params": [block_height]
  }
  response = requests.post(url, data=json.dumps(payload), headers=headers).json()
  block_hash = response['result']

  # Get the block data
  payload = {
    "method": "getblock",
    "params": [block_hash]
  }
  response = requests.post(url, data=json.dumps(payload), headers=headers).json()
  block_data = response['result']

  # Extract the relevant data from the block
  block_time = block_data['time']
  block_size = block_data['size']
  block_txs = block_data['tx']
  block_reward = block_data['reward']

  # Calculate the stock-to-flow (S2F) value for the block
  block_s2f = block_reward / block_size
  
  # Extract the S2F values and price
s2f = df["S2F"]
price = df["price"]

# Fit the data to the model
params, _ = curve_fit(s2f_model, s2f, price)
a, b = params

# Predict the price for a given S2F value
s2f_prediction = 50
price_prediction = s2f_model(s2f_prediction, a, b)
print(f"Predicted price for S2F = {s2f_prediction}: {price_prediction:.2f}")

# Plot the data and the fitted model
plt.scatter(s2f, price)
x = np.linspace(min(s2f), max(s2f), 100)
y = s2f_model(x, a, b)
plt.plot(x, y)
plt.xlabel("S2F")
plt.ylabel("Price")
plt.show()


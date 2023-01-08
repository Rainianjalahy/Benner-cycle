import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load the data
data = pd.read_csv("business_cycle_data.csv")

# Split the data into features (X) and labels (y)
X = data[["GDP_growth", "unemployment_rate", "inflation", "consumer_confidence"]]
y = data["business_cycle_stage"]

# Train a random forest classifier
model = RandomForestClassifier()
model.fit(X, y)

# Predict the current stage of the business cycle
gdp_growth = 3.5
unemployment_rate = 4.0
inflation = 2.0
consumer_confidence = 0.8

current_stage = model.predict([[gdp_growth, unemployment_rate, inflation, consumer_confidence]])[0]
print(current_stage)

import fastf1
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error

# Enable cache
fastf1.Cache.enable_cache('fastf1_cache')

# --- Function to load fastest lap per driver ---
def load_fastest_lap(year, gp_round, session_name):
    session = fastf1.get_session(year, gp_round, session_name)
    session.load()
    laps = session.laps

    # Unique driver codes
    driver_codes = laps['Driver'].unique()

    # Get fastest lap per driver manually
    records = []
    for code in driver_codes:
        driver_laps = laps.pick_driver(code).pick_fastest()
        if pd.notnull(driver_laps['LapTime']):
            records.append({
                'DriverCode': code,
                f'{session_name.upper()} Time (s)': driver_laps['LapTime'].total_seconds()
            })

    df = pd.DataFrame(records)
    return df

# --- Load Imola 2025 FP1 & FP2 data ---
fp1_data = load_fastest_lap(2025, 7, 'FP1')
fp2_data = load_fastest_lap(2025, 7, 'FP2')

# --- Qualifying Data 2025 ---
qualifying_2025 = pd.DataFrame({
    "Driver": ["Lando Norris", "Oscar Piastri", "Max Verstappen", "George Russell", "Yuki Tsunoda",
               "Alexander Albon", "Charles Leclerc", "Lewis Hamilton", "Pierre Gasly", "Carlos Sainz",
               "Fernando Alonso", "Lance Stroll"],
    "QualifyingTime (s)": [75.096, 75.180, 75.481, 75.546, 75.670,
                           75.737, 75.755, 75.973, 75.980, 76.062, 76.4, 76.5]
})

# --- Driver Code Mapping ---
driver_mapping = {
    "Lando Norris": "NOR", "Oscar Piastri": "PIA", "Max Verstappen": "VER", "George Russell": "RUS",
    "Yuki Tsunoda": "TSU", "Alexander Albon": "ALB", "Charles Leclerc": "LEC", "Lewis Hamilton": "HAM",
    "Pierre Gasly": "GAS", "Carlos Sainz": "SAI", "Lance Stroll": "STR", "Fernando Alonso": "ALO"
}
qualifying_2025["DriverCode"] = qualifying_2025["Driver"].map(driver_mapping)

# --- Merge FP1 & FP2 with qualifying data ---
fp_data = qualifying_2025.merge(fp1_data, on="DriverCode", how="left") \
                         .merge(fp2_data, on="DriverCode", how="left")

# --- Check for missing data ---
print("\n⚠️ Missing FP1/FP2 data:\n", fp_data[fp_data.isna().any(axis=1)])

# --- Model Training ---
X = fp_data[['FP1 Time (s)', 'FP2 Time (s)']]
y = fp_data['QualifyingTime (s)']

# --- Train Gradient Boosting ---
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
model.fit(X_train, y_train)

# --- Predict ---
fp_data['PredictedQualifyingTime (s)'] = model.predict(X)

# --- Results ---
fp_data = fp_data.sort_values(by="PredictedQualifyingTime (s)")
print("\n🏁 Predicted Imola 2025 Qualifying Results:\n")
print(fp_data[['Driver', 'PredictedQualifyingTime (s)']])

# --- Model Evaluation ---
y_pred = model.predict(X_test)
print(f"\n🔍 Model MAE on Test Set: {mean_absolute_error(y_test, y_pred):.3f} seconds")

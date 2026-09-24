import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load Dataset
df = pd.read_csv('sepsis_icu_dataset.csv')

X = df[['heart_rate', 'temperature', 'spo2', 'wbc_count', 'lactate', 'creatinine']]
y = df['sepsis_onset']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save Model
with open('sepsis_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as 'sepsis_model.pkl'!")

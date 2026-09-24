import pandas as pd
import numpy as np

np.random.seed(42)
num_patients = 100
hours_per_patient = 24
data = []

for patient_id in range(1, num_patients + 1):
    base_hr = np.random.normal(75, 10)
    base_temp = np.random.normal(36.8, 0.4)
    base_wbc = np.random.normal(7, 2)
    base_lactate = np.random.normal(1.0, 0.3)
    base_creatinine = np.random.normal(0.9, 0.2)
    
    will_develop_sepsis = np.random.choice([0, 1], p=[0.7, 0.3])
    
    for hour in range(1, hours_per_patient + 1):
        hr = base_hr + np.random.normal(0, 3)
        temp = base_temp + np.random.normal(0, 0.2)
        spo2 = max(88, min(100, np.random.normal(97, 1.5)))
        wbc = base_wbc + np.random.normal(0, 0.3)
        lactate = base_lactate + np.random.normal(0, 0.1)
        creatinine = base_creatinine + np.random.normal(0, 0.05)
        
        sepsis_target = 0
        if will_develop_sepsis and hour >= 12:
            sepsis_target = 1
            hr += (hour - 12) * 2.5
            temp += (hour - 12) * 0.15
            spo2 -= (hour - 12) * 0.4
            wbc += (hour - 12) * 0.8
            lactate += (hour - 12) * 0.25
            creatinine += (hour - 12) * 0.1

        data.append({
            'patient_id': patient_id,
            'hour': hour,
            'heart_rate': round(hr, 1),
            'temperature': round(temp, 1),
            'spo2': round(spo2, 1),
            'wbc_count': round(wbc, 2),
            'lactate': round(lactate, 2),
            'creatinine': round(creatinine, 2),
            'sepsis_onset': sepsis_target
        })

df = pd.DataFrame(data)
df.to_csv('sepsis_icu_dataset.csv', index=False)
print("✅ Dataset 'sepsis_icu_dataset.csv' successfully generated!")

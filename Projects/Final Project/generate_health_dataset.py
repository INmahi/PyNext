import random
import numpy as np
import pandas as pd
from datetime import datetime

NUM_ROWS = 800
random.seed(42)
np.random.seed(42)

# Regions of Bangladesh
regions = [
    "Dhaka","Chattogram","Rajshahi","Khulna","Barishal","Sylhet","Rangpur","Mymensingh"
]

# Helper functions
first_names = ["Amina","Rahim","Karim","Hasan","Farah","Nasrin","Jamil","Nadia","Sadia","Rafi","Sumaiya","Imran","Shakil","Tania","Sabbir","Lamia","Arif","Tanvir","Joya","Fahim"]
last_names = ["Ahmed","Hossain","Khan","Chowdhury","Islam","Rahman","Sheikh","Sarker","Hasan","Barman","Mollah","Biswas","Talukdar","Mia","Rumi","Akter","Ali","Begum","Azad","Sultan"]
sexes = ["M","F"]
smoker_status_values = ["never","former","current"]
yes_mid_no = ["no","mid","yes"]  # For tri-level categorical
binary_yes_no = ["no","yes"]
exercise_levels = ["sedentary","light","moderate","active","athlete"]

# Distributions
ages = np.clip(np.random.normal(42, 14, NUM_ROWS).round(), 18, 85).astype(int)
heights = np.random.normal(162, 9, NUM_ROWS).round(1)  # cm
weights = np.random.normal(66, 13, NUM_ROWS).round(1)  # kg (no BMI column as requested)

# Blood pressure with correlation to age
systolic = np.random.normal(110 + (ages-40)*0.6, 12, NUM_ROWS).round()
diastolic = np.random.normal(70 + (ages-40)*0.3, 8, NUM_ROWS).round()

# Heart and other vitals
resting_hr = np.random.normal(74, 9, NUM_ROWS).round().astype(int)
body_temp_c = np.random.normal(36.7, 0.3, NUM_ROWS).round(2)
spo2_pct = np.clip(np.random.normal(97, 1.2, NUM_ROWS), 90, 100).round(1)

# Lifestyle
smoker_status = np.random.choice(smoker_status_values, NUM_ROWS, p=[0.58, 0.22, 0.20])
exercise_minutes_per_week = np.random.gamma(4, 45, NUM_ROWS).round()  # right-skewed
sleep_hours = np.clip(np.random.normal(6.8, 1.1, NUM_ROWS), 3.5, 10.0).round(1)
alcohol_freq = np.random.choice(["none","monthly","weekly","daily"], NUM_ROWS, p=[0.35,0.30,0.25,0.10])

# Family history & conditions (text yes/no)
family_history_diabetes = np.random.choice(binary_yes_no, NUM_ROWS, p=[0.55,0.45])
family_history_heart = np.random.choice(binary_yes_no, NUM_ROWS, p=[0.52,0.48])
# Chronic conditions tri-level: no (0 risk), mid (monitor), yes (diagnosed)
chronic_kidney = np.random.choice(yes_mid_no, NUM_ROWS, p=[0.82,0.10,0.08])
hypertension_dx = np.where(systolic>140, "yes", np.where(systolic>125, "mid", "no"))

diabetes_stage = np.random.choice(["none","prediabetes","type2"], NUM_ROWS, p=[0.70,0.18,0.12])

# Labs (some correlation)
fasting_glucose = np.random.normal(90, 12, NUM_ROWS) + np.where(diabetes_stage=="prediabetes",15,0) + np.where(diabetes_stage=="type2",35,0)
fasting_glucose = fasting_glucose.round(1)

hba1c = np.random.normal(5.4, 0.4, NUM_ROWS) + np.where(diabetes_stage=="prediabetes",0.5,0) + np.where(diabetes_stage=="type2",1.4,0)
hba1c = hba1c.round(2)

total_chol = np.random.normal(185, 32, NUM_ROWS).round(1)
hdl = np.random.normal(49, 11, NUM_ROWS).round(1)
ldl = (total_chol - hdl - np.random.normal(30, 8, NUM_ROWS)).round(1)
triglycerides = np.abs(np.random.normal(140, 70, NUM_ROWS)).round(1)

creatinine = np.clip(np.random.normal(0.95 + (ages-40)*0.005, 0.18, NUM_ROWS), 0.5, 2.5).round(2)
# Simplified eGFR estimation (not clinically precise)
egfr = np.clip(110 - (ages*0.7) - (creatinine*8), 15, 130).round(1)

alt = np.abs(np.random.normal(26, 11, NUM_ROWS)).round(1)
ast = np.abs(np.random.normal(24, 9, NUM_ROWS)).round(1)
vitamin_d = np.clip(np.random.normal(38, 12, NUM_ROWS), 5, 90).round(1)
crp = np.abs(np.random.normal(2.2, 3.5, NUM_ROWS)).round(2)

# Derived categorical classification fields (kept as text intentionally)
# risk tri-level based on combination of factors
risk_category = []
for i in range(NUM_ROWS):
    score = 0
    if systolic[i] > 140 or diastolic[i] > 90: score += 2
    if hba1c[i] > 6.4: score += 2
    elif hba1c[i] > 5.7: score += 1
    if ldl[i] > 160: score += 2
    elif ldl[i] > 130: score += 1
    if triglycerides[i] > 250: score += 1
    if smoker_status[i] == "current": score += 1
    if family_history_heart[i] == "yes": score += 1
    if score >= 5: risk_category.append("yes")
    elif score >= 3: risk_category.append("mid")
    else: risk_category.append("no")

# Additional usage metrics
wearable_steps_avg = np.random.normal(7200, 2500, NUM_ROWS).round()
telehealth_usage = np.random.choice(binary_yes_no, NUM_ROWS, p=[0.65,0.35])
medication_count = np.random.poisson(1.6, NUM_ROWS)
doctor_visits_last_year = np.random.poisson(2.4, NUM_ROWS)
last_checkup_days_ago = np.random.randint(5, 365, NUM_ROWS)
# Enrollment years 2018-2025 inclusive (8 years) - adjust probability vector to length 8
enrollment_year = np.random.choice(
    list(range(2018, 2026)),
    NUM_ROWS,
    p=[0.06, 0.09, 0.11, 0.14, 0.16, 0.17, 0.15, 0.12]  # sums to 1.00
)

# Build DataFrame
data = {
    "id": range(1, NUM_ROWS+1),
    "fname": np.random.choice(first_names, NUM_ROWS),
    "lname": np.random.choice(last_names, NUM_ROWS),
    "age": ages,
    "sex": np.random.choice(sexes, NUM_ROWS, p=[0.51,0.49]),
    "country_region": np.random.choice(regions, NUM_ROWS),
    "height_cm": heights,
    "weight_kg": weights,
    "systolic_bp": systolic.astype(int),
    "diastolic_bp": diastolic.astype(int),
    "resting_hr": resting_hr,
    "body_temp_c": body_temp_c,
    "spo2_pct": spo2_pct,
    "smoker_status": smoker_status,
    "exercise_minutes_per_week": exercise_minutes_per_week,
    "sleep_hours": sleep_hours,
    "alcohol_freq": alcohol_freq,
    "family_history_diabetes": family_history_diabetes,
    "family_history_heart": family_history_heart,
    "chronic_kidney_disease": chronic_kidney,
    "hypertension_status": hypertension_dx,
    "diabetes_stage": diabetes_stage,
    "fasting_glucose_mgdl": fasting_glucose,
    "hba1c_pct": hba1c,
    "total_cholesterol_mgdl": total_chol,
    "hdl_mgdl": hdl,
    "ldl_mgdl": ldl,
    "triglycerides_mgdl": triglycerides,
    "creatinine_mgdl": creatinine,
    "egfr": egfr,
    "alt_u_l": alt,
    "ast_u_l": ast,
    "vitamin_d_ngml": vitamin_d,
    "crp_mg_l": crp,
    "risk_category": risk_category,
    "wearable_steps_avg": wearable_steps_avg,
    "telehealth_usage": telehealth_usage,
    "medication_count": medication_count,
    "doctor_visits_last_year": doctor_visits_last_year,
    "last_checkup_days_ago": last_checkup_days_ago,
    "enrollment_year": enrollment_year
}

df = pd.DataFrame(data)

# Introduce missing values randomly for selected columns
cols_with_missing = ["vitamin_d_ngml","crp_mg_l","wearable_steps_avg","exercise_minutes_per_week","triglycerides_mgdl"]
for col in cols_with_missing:
    mask = np.random.rand(NUM_ROWS) < 0.15  # 15% missing
    df.loc[mask, col] = np.nan

# Add some deliberate outliers
outlier_indices = np.random.choice(df.index, 8, replace=False)
df.loc[outlier_indices[:2], 'triglycerides_mgdl'] = df['triglycerides_mgdl'].max() * 4
if 'wearable_steps_avg' in df.columns:
    df.loc[outlier_indices[2:4], 'wearable_steps_avg'] = 35000
# very low heart rate (athletic) and very high
df.loc[outlier_indices[4:6], 'resting_hr'] = [38, 130]
# extreme systolic/diastolic
df.loc[outlier_indices[6], ['systolic_bp','diastolic_bp']] = [210, 130]
df.loc[outlier_indices[7], ['systolic_bp','diastolic_bp']] = [85, 45]

# Save CSV
output_path = r"c:/Users/DELL/PyNext/Projects/Final Project/health_dataset.csv"
df.to_csv(output_path, index=False)
print(f"Generated dataset saved to {output_path} with shape {df.shape}")

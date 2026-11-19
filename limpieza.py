import os
import pandas as pd

df = pd.read_csv('data_raw/WA_Fn-UseC_-Telco-Customer-Churn.csv')

df['TotalCharges'] = pd.to_numeric(df['TotalCharges'].astype(str).str.strip(), errors='coerce')
print("Nulos en TotalCharges:", df['TotalCharges'].isna().sum())
df['TotalCharges'] = df['TotalCharges'].fillna(0)

os.makedirs('data_clean', exist_ok=True)

df_clientes = df[['customerID', 'gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'Churn']]
df_servicios = df[['customerID', 'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']]
df_facturacion = df[['customerID', 'Contract', 'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges', 'TotalCharges']]

df_clientes.to_csv('data_clean/clientes.csv', index=False)
df_servicios.to_csv('data_clean/servicios.csv', index=False)
df_facturacion.to_csv('data_clean/facturacion.csv', index=False)

print("Tablas creadas en data_clean/")

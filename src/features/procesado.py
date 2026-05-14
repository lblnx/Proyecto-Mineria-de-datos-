import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Cargar los datos limipios
df_dest = pd.read_csv("data/interim/bird_migration_OD_clean.csv")

#idnetificar las columnas numericas 
numeric_cols = df_dest.select_dtypes(include=[np.number]).columns
#Aplicar Standar scaler
scaler = StandardScaler()
df_scaler = df_dest.copy()
df_scaler[numeric_cols] = scaler.fit_transform(df_scaler[numeric_cols])
# Guardar el dataset procesado
df_scaler.to_csv("data/processed/bird_migration_OD_scaled.csv", index=False)

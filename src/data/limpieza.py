import pandas as pd
import numpy as np

df_dest = pd.read_csv("data/bird_migration_with_origin_destination.csv")

def clean_data(df):
    # Identificar columnas numéricas y categóricas
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    categorical_cols = df.select_dtypes(exclude=[np.number]).columns

    # 1. Tratamiento de valores faltantes
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].median())
    
    for col in categorical_cols:
        df[col] = df[col].fillna(df[col].mode()[0] if not df[col].mode().empty else "Unknown")

    # 2. Tratamiento de outliers (Método IQR)
    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        # Limitamos los valores a los rangos permitidos (Capping)
        df[col] = df[col].clip(lower=lower_bound, upper=upper_bound)

    for col in numeric_cols:
        min_val = df[col].min()
        max_val = df[col].max()
        df[col] = (df[col] - min_val) / (max_val - min_val)
    
    return df

df_dest = clean_data(df_dest)

import pandas as pd

# Cargar los datos procesados
df_dest = pd.read_csv("data/processed/bird_migration_OD_scaled.csv")
# Seleccionar las columnas relevantes para el análisis
columnas_seleccionadas = ['Species', 'Region', 'Start_Latitude', 'Start_Longitude', 'End_Latitude', 'End_Longitude','Flight_Distance_km', 'Flight_Duration_hours', 'Average_Speed_kmph', 'Max_Altitude_m','Temperature_C', 'Wind_Speed_kmph']
# Filtramos el dtaset
df_seleccion = df_dest[columnas_seleccionadas]
# Guardar el dataset seleccionado
df_seleccion.to_csv("data/processed/bird_migration_OD_selected.csv", index=False)
import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans

df = pd.read_csv("data/processed/bird_migration_OD_selected.csv")

# K.means
X = df[['End_Latitude', 'End_Longitude']]
kmeans = KMeans(n_clusters=5, random_state=42)
df['Cluster_Destino'] = kmeans.fit_predict(X).astype(str)

df['Start_Lat_Vis'] = df['Start_Latitude'] * 20
df['Start_Lon_Vis'] = df['Start_Longitude'] * 40 - 20
df['End_Lat_Vis'] = df['End_Latitude'] * 20
df['End_Lon_Vis'] = df['End_Longitude'] * 40 - 20

# Tomamos 50 aves para que la animación sea muy fluida
df_muestra = df.head(50).reset_index()
num_pasos = 25 # Cuántos "cuadros" dura el vuelo (a mayor número, más lento y suave)
frames_vuelo = []

for index, row in df_muestra.iterrows():
    # Avance x punto
    lat_step = (row['End_Lat_Vis'] - row['Start_Lat_Vis']) / num_pasos
    lon_step = (row['End_Lon_Vis'] - row['Start_Lon_Vis']) / num_pasos
    
    for paso in range(num_pasos + 1):
        frames_vuelo.append({
            'ID_Ave': index,
            'Species': row['Species'],
            'Cluster_Destino': row['Cluster_Destino'],
            'Paso_Tiempo': paso,
            'Lat_Actual': row['Start_Lat_Vis'] + (lat_step * paso),
            'Lon_Actual': row['Start_Lon_Vis'] + (lon_step * paso)
        })

# Crear el DataFrame y ordenarlo por tiempo
df_animacion = pd.DataFrame(frames_vuelo)
df_animacion = df_animacion.sort_values(by=['Paso_Tiempo', 'ID_Ave'])

# Usamos Plotly Express
fig = px.scatter_geo(
    df_animacion,
    lat="Lat_Actual",
    lon="Lon_Actual",
    color="Species",
    animation_frame="Paso_Tiempo", 
    animation_group="ID_Ave",      
    hover_name="Species",          # Título al pasar el mouse
    hover_data={"Cluster_Destino": True, "Paso_Tiempo": False}, # Agrega el Cluster al texto
    projection="orthographic",     
    title="Migración Animada por Especie",
    color_discrete_sequence=px.colors.qualitative.Pastel # Cambié a una paleta de colores más suave
)

# Detalles visuales del mundo
fig.update_traces(marker=dict(size=8, opacity=0.8, line=dict(width=1, color='DarkSlateGrey')))
fig.update_geos(
    showland=True, landcolor="rgb(243, 243, 243)",
    showocean=True, oceancolor="#e0f3f8",
    countrycolor="rgb(204, 204, 204)"
)

# Guardar archivo
fig.write_html("animacion_globo_3d.html")
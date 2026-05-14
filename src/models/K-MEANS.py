import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos seleccionados
df_seleccion = pd.read_csv("data/processed/bird_migration_OD_selected.csv")
# Seleccion de variables
X = df_seleccion[['End_Latitude', 'End_Longitude']]
# Aplicar K-Means
kmeans = KMeans(n_clusters=5, random_state=42)
df_seleccion['Cluster_D'] = kmeans.fit_predict(X)
# Visualización de los clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_seleccion, x='End_Longitude', y='End_Latitude', hue='Cluster_D', palette='Set1')
plt.title('Clusters de Destino de Migración de Aves')
plt.xlabel('Longitud de Destino')
plt.ylabel('Latitud de Destino')
plt.legend(title='Cluster')
plt.savefig("reports/figures/kmeans_clusters.png")
plt.close()




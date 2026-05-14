import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos
df_knn = pd.read_csv("data/processed/bird_migration_OD_selected.csv")
# Seleccionar características y variable objetivo
variables_vuelo = ['Start_Latitude', 'Start_Longitude']
X = df_knn[variables_vuelo]
y = df_knn['Species']
# Dividir el conjunto en 80 20
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Entrenamos el modelo
knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train, y_train)
# Hacer predicciones y evaluar
y_pred = knn_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión del modelo KNN (Accuracy): {accuracy * 100:.2f}%")
print("\nReporte de Clasificación (Regiones):")
print(classification_report(y_test, y_pred))
# Visualización de la matriz de confusión
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=knn_model.classes_, 
            yticklabels=knn_model.classes_)
plt.title('Matriz de Confusión - KNN (Región por Origen)')
plt.ylabel('Región Real')
plt.xlabel('Región Predicha')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("reports/figures/knn_confusion_matrix.png")
plt.close()



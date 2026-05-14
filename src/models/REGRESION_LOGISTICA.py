import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

df_rl = pd.read_csv("data/processed/bird_migration_OD_selected.csv")

# Seleccionar características y variable objetivo
variables_seleccionadas = ['Temperature_C', 'Wind_Speed_kmph', 'Flight_Distance_km']
X = df_rl[variables_seleccionadas]
y = df_rl['Species']

# Dividir el conjunto en 80 20
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenamos el modelo
rl_model = LogisticRegression(max_iter=1000, random_state=42)
rl_model.fit(X_train, y_train)

# Hacer predicciones y evaluar
y_pred = rl_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Precisión del modelo Regresión Logística: {accuracy * 100:.2f}%")
print("\nReporte de Clasificación:")
print(classification_report(y_test, y_pred))

# Visualización de la matriz de confusión
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=rl_model.classes_, 
            yticklabels=rl_model.classes_)
plt.title('Matriz de Confusión - Regresión Logística (Especies)')
plt.ylabel('Etiqueta Real')
plt.xlabel('Predicción del Modelo')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("reports/figures/rl_confusion_matrix.png")
plt.close()
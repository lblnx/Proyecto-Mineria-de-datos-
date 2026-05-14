import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

# Cargar los datos
df_rf = pd.read_csv("data/processed/bird_migration_OD_selected.csv")
# Seleccionar características y variable objetivo
variables_vuelo = ['Max_Altitude_m', 'Average_Speed_kmph', 'Flight_Distance_km', 'Flight_Duration_hours']
X = df_rf[variables_vuelo]
y = df_rf['Species']
# Dividir el conjunto en 80 20
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Entrenamos el modelo
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
# Hacer predicciones y evaluar
y_pred = rf_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
# visualizacion
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=rf_model.classes_, 
            yticklabels=rf_model.classes_)
plt.title('Matriz de Confusión - Random Forest (Especies vs Vuelo)')
plt.ylabel('Etiqueta Real')
plt.xlabel('Predicción del Modelo')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("reports/figures/rf_confusion_matrix.png")
plt.close()








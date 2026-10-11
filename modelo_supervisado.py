import numpy as np
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text

# 1. Dataset sintético del sistema de transporte
np.random.seed(42)
n_muestras = 120

datos = {
    "hora_pico": np.random.choice([0, 1], size=n_muestras, p=[0.4, 0.6]),
    "lluvia": np.random.choice([0, 1], size=n_muestras, p=[0.7, 0.3]),
    "congestion_vial": np.random.randint(1, 6, size=n_muestras),
    "pasajeros_estacion": np.random.randint(20, 200, size=n_muestras),
    "distancia_km": np.round(np.random.uniform(2.0, 15.0, size=n_muestras), 2),
}

df_supervisado = pd.DataFrame(datos)

# Definir regla base para la etiqueta (supervisado)
df_supervisado["retraso_critico"] = (
    (df_supervisado["hora_pico"] == 1)
    & (df_supervisado["congestion_vial"] >= 4)
    | (
        (df_supervisado["lluvia"] == 1)
        & (df_supervisado["pasajeros_estacion"] > 100)
    )
).astype(int)

df_supervisado.to_csv("datos_supervisado.csv", index=False)

# 2. Separación de características (X) y objetivo (y)
X = df_supervisado.drop("retraso_critico", axis=1)
y = df_supervisado["retraso_critico"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# 3. Entrenamiento con Árbol de Decisión (Palma Méndez, Cap. 17)
clf = DecisionTreeClassifier(criterion="entropy", max_depth=3, random_state=42)
clf.fit(X_train, y_train)

# 4. Evaluación y Pruebas
y_pred = clf.predict(X_test)

print("--- RESULTADOS MODELO SUPERVISADO ---")
print("Matriz de Confusión:")
print(confusion_matrix(y_test, y_pred))
print("\nMétricas de Clasificación:")
print(classification_report(y_test, y_pred))
print("\nReglas del Árbol de Decisión:")
print(export_text(clf, feature_names=list(X.columns)))
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler


def main():
    # 1. Dataset sintético de estaciones de transporte
    np.random.seed(42)
    n_estaciones = 60
    datos_cluster = {
        "estacion_id": [f"Estacion_{i+1}" for i in range(n_estaciones)],
        "afluencia_promedio": np.random.randint(50, 1500, size=n_estaciones),
        "tiempo_espera_min": np.round(
            np.random.uniform(2.0, 18.0, size=n_estaciones),
            1,
        ),
        "transbordos_hora": np.random.randint(10, 400, size=n_estaciones),
        "capacidad_uso_porc": np.round(
            np.random.uniform(30.0, 99.0, size=n_estaciones),
            1,
        ),
    }

    df_no_supervisado = pd.DataFrame(datos_cluster)
    df_no_supervisado.to_csv("datos_no_supervisado.csv", index=False)

    # 2. Preprocesamiento (Escalado de variables numéricas)
    caracteristicas = [
        "afluencia_promedio",
        "tiempo_espera_min",
        "transbordos_hora",
        "capacidad_uso_porc",
    ]
    X_cluster = df_no_supervisado[caracteristicas]

    scaler = StandardScaler()
    X_escalado = scaler.fit_transform(X_cluster)

    # 3. Agrupamiento K-Means
    k = 3
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    df_no_supervisado["cluster"] = kmeans.fit_predict(X_escalado)

    # 4. Evaluación del modelo
    silueta = silhouette_score(X_escalado, df_no_supervisado["cluster"])

    print("--- RESULTADOS MODELO NO SUPERVISADO ---")
    print(f"Coeficiente Silhouette: {silueta:.3f}\n")
    print("Centroides por Grupo (Promedios reales):")
    resumen_clusters = df_no_supervisado.groupby("cluster")[caracteristicas].mean()
    print(resumen_clusters)


if __name__ == "__main__":
    main()
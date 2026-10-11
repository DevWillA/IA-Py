```markdown
# Modelos de Machine Learning para el Transporte Masivo - Ibagué 🚌🤖

Este repositorio contiene la implementación práctica de modelos de **Aprendizaje Supervisado** y **Aprendizaje No Supervisado** aplicados al sistema de transporte de la ciudad de Ibagué. El proyecto integra la predicción de retrasos críticos operativos y la segmentación estratégica de estaciones para optimizar la toma de decisiones sobre la flota.

---

## 👥 Equipo de Trabajo

- **William Javier Amaya:** 
  - Estructuración y descripción del dataset de Aprendizaje Supervisado (`datos_supervisado.csv`).
  - Preprocesamiento, estandarización de variables y evaluación métrica de clusters (`modelo_no_supervisado.py`).
- **Miguel Ángel Tabares:** 
  - Formulación del dataset de estaciones (`datos_no_supervisado.csv`).
  - Entrenamiento del clasificador de Árbol de Decisión e interpretación de reglas y matrices de confusión (`modelo_supervisado.py`).

---

## 📂 Estructura del Proyecto

El repositorio está organizado en los siguientes archivos de datos y código fuente:

```text
├── datos_supervisado.csv       # Dataset con 120 registros para predicción de retrasos (con etiquetas)
├── datos_no_supervisado.csv    # Dataset con 60 estaciones de transporte masivo (sin etiquetas)
├── modelo_supervisado.py       # Script del Árbol de Decisión (Clasificación binaria)
├── modelo_no_supervisado.py     # Script de Agrupamiento K-Means (Clustering)
└── README.md                   # Documentación general del proyecto

```

---

## 📊 Descripción de los Componentes

### 1. Aprendizaje Supervisado: Árboles de Decisión (`modelo_supervisado.py`)

* **Objetivo:** Predecir si una ruta o viaje presentará un retraso crítico superior a 15 minutos (`retraso_critico`: `1` = Sí, `0` = No).
* **Características de entrada:** `hora_pico`, `lluvia`, `congestion_vial` (1-5), `pasajeros_estacion` y `distancia_km`.
* **Algoritmo:** `DecisionTreeClassifier` implementado bajo el criterio de **entropía** y profundidad máxima (`max_depth=3`), previniendo el sobreajuste (basado en Palma Méndez, Cap. 17).
* **Resultados:**
* Exactitud (Accuracy): **90%** sobre el conjunto de test (30 muestras).
* Sensibilidad (Recall) para eventos críticos: **1.00 (100%)**.
* Regla primaria inferida: Si `congestion_vial > 3.5` y `hora_pico == 1`, se clasifica con alta certidumbre como retraso crítico.



### 2. Aprendizaje No Supervisado: Agrupamiento K-Means (`modelo_no_supervisado.py`)

* **Objetivo:** Segmentar y perfilar 60 estaciones de transporte sin supervisión previa de etiquetas, facilitando la redistribución de flota y recursos.
* **Variables analizadas:** `afluencia_promedio`, `tiempo_espera_min`, `transbordos_hora` y `capacidad_uso_porc`.
* **Preprocesamiento:** Escalado de datos mediante `StandardScaler` para equilibrar la escala de pasajeros frente a tiempos en minutos.
* **Algoritmo:** `KMeans` con $k=3$ centroides (basado en Palma Méndez, Cap. 16).
* **Resultados:**
* **Cluster 0 (Alta Demanda):** Afluencia promedio masiva (~1.168 pax/h) y tiempos de espera altos (~11.8 min). Requiere refuerzo de frecuencias troncales.
* **Cluster 1 (Saturación de Infraestructura):** Ocupación física crítica (~87.6% de capacidad en plataforma). Requiere control de aforos.
* **Cluster 2 (Nodos de Conexión Ágil):** Esperas cortas (~6.8 min) y alto volumen de transbordo (~288 transbordos/h).



---

## 🚀 Instrucciones de Ejecución

### Prerrequisitos

Tener instalado Python 3.8 o superior junto a las siguientes librerías:

```bash
pip install pandas numpy scikit-learn

```

### Ejecución de los Modelos

1. **Clonar el repositorio:**
```bash
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_REPOSITORIO>

```


2. **Ejecutar el modelo supervisado:**
```bash
python modelo_supervisado.py

```


*Salida:* Imprime la matriz de confusión, el reporte de clasificación (precisión/recall) y la estructura de reglas del árbol.
3. **Ejecutar el modelo no supervisado:**
```bash
python modelo_no_supervisado.py

```


*Salida:* Imprime el coeficiente Silhouette y la tabla de centroides reales por cada cluster.

---

## 📹 Sustentación y Entregables

* El enlace al video de sustentación donde participan ambos integrantes en cámara explicando los comandos, los datos y los resultados se encuentra detallado en el documento PDF de la entrega.
* El log del repositorio Git evidencia las contribuciones y commits individuales de **William Amaya** y **Miguel Tabares**.

---

## 📚 Bibliografía

* Palma Méndez, J. T. (2008). *Inteligencia artificial: métodos, técnicas y aplicaciones*. Madrid: McGraw-Hill España.
* Capítulo 16: Técnicas de agrupamiento.
* Capítulo 17: Aprendizaje de árboles y reglas de decisión.



```

```
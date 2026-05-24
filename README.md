# F1 Performance Predictor

Aplicación interactiva desarrollada con Streamlit para analizar y predecir el rendimiento de pilotos de Fórmula 1 utilizando datos históricos reales de las temporadas 2021-2024.

La aplicación permite simular distintos escenarios de carrera, comparar pilotos y equipos, analizar rendimiento en lluvia y estudiar diferencias frente a compañeros de equipo mediante técnicas de Machine Learning y análisis de datos.

---

# Objetivo del proyecto

El objetivo principal del proyecto es desarrollar una solución de análisis predictivo aplicada al mundo de la Fórmula 1 utilizando datos históricos reales.

La aplicación permite:

- Predecir probabilidades de:
  - Top 10
  - Top 5
  - Podio
  - Victoria

- Comparar:
  - pilotos
  - equipos
  - rendimiento frente al compañero
  - rendimiento en lluvia

- Simular escenarios hipotéticos:
  - pilotos en otros equipos
  - temporadas distintas
  - diferentes circuitos y condiciones

---

# Tecnologías utilizadas

- Python
- Streamlit
- Pandas
- Scikit-learn
- Plotly
- FastF1
- Joblib
- Matplotlib

---

# Dataset

Los datos han sido obtenidos utilizando la librería FastF1 a partir de datos históricos oficiales de Fórmula 1 entre las temporadas 2021 y 2024.

Se incluyen variables como:

- posición de salida
- posición final
- puntos
- neumáticos
- temperatura
- lluvia
- paradas en boxes
- tiempo medio por vuelta
- rendimiento frente al compañero
- métricas históricas de piloto y equipo

---

# Estructura del proyecto

```text
f1-performance-predictor/
│
├── main.py
├── README.md
├── requirements.txt
│
├── data/
│   ├── f1_dataset.csv
│   ├── f1_dataset_clean.csv
│   └── f1_dataset_features.csv
│
├── models/
│   ├── model_top10.joblib
│   ├── model_top5.joblib
│   ├── model_top3.joblib
│   └── model_victory.joblib
│
├── src/
│   ├── 01_download_data.py
│   ├── 02_merge_datasets.py
│   ├── 03_clean_dataset.py
│   ├── 04_train_models.py
│   └── 05_feature_engineering.py
│
└── notebooks/
    └── 01_exploratory_analysis.py 

# -*- coding: utf-8 -*-
"""
Created on Sun May 24 14:16:25 2026

@author: cpcch
"""

import pandas as pd
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report
)

# ======================================
# RUTA BASE
# ======================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ======================================
# CARGAR DATASET
# ======================================

data_path = os.path.join(
    BASE_DIR,
    "data",
    "f1_dataset_features.csv"
)

df = pd.read_csv(data_path)

print("Dataset cargado correctamente.")
print(df.head())

# ======================================
# VARIABLES DE ENTRADA
# ======================================

features = [
    "GridPosition",
    "PitStops",
    "AvgLapTime",
    "AirTemp",
    "TrackTemp",
    "Rain",
    "DriverAvgFinish",
    "DriverTop10Rate",
    "TeamAvgFinish",
    "TeamTop10Rate",
    "TeammateDiff",
    "BeatsTeammate",
    "DriverVsTeammatePace"
]

X = df[features]

# ======================================
# VARIABLES OBJETIVO
# ======================================

targets = {
    "Top10": "model_top10.joblib",
    "Top5": "model_top5.joblib",
    "Top3": "model_top3.joblib",
    "Victory": "model_victory.joblib"
}

# ======================================
# ENTRENAR MODELOS
# ======================================

for target, filename in targets.items():

    print(f"\n==============================")
    print(f"ENTRENANDO MODELO: {target}")
    print(f"==============================")

    y = df[target]

    # División train/test
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # Modelo
    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42
    )

    # Entrenar
    model.fit(X_train, y_train)

    # Predicciones
    predictions = model.predict(X_test)

    # Métricas
    accuracy = accuracy_score(y_test, predictions)

    print(f"\nAccuracy: {accuracy:.4f}")

    print("\nClassification Report:")
    print(classification_report(y_test, predictions))

    # Guardar modelo
    model_path = os.path.join(
        BASE_DIR,
        "models",
        filename
    )

    joblib.dump(model, model_path)

    print(f"\nModelo guardado en:")
    print(model_path)

print("\nTodos los modelos fueron entrenados correctamente.")
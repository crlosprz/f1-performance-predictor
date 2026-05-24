# -*- coding: utf-8 -*-
"""
Created on Sat May 23 19:24:13 2026

@author: cpcch
"""
import fastf1

fastf1.Cache.enable_cache("cache")

session = fastf1.get_session(2024, "Monza", "R")
session.load()

resultados = session.results[[
    "Abbreviation",
    "TeamName",
    "Position",
    "GridPosition",
    "Points"
]].copy()

resultados.columns = [
    "Piloto",
    "Equipo",
    "PosicionFinal",
    "PosicionSalida",
    "Puntos"
]

print(resultados.head())

vueltas = session.laps[[
    "Driver",
    "LapNumber",
    "Compound",
    "TyreLife"
]].copy()

vueltas.columns = [
    "Piloto",
    "NumeroVuelta",
    "Neumatico",
    "VidaNeumatico"
]

print(vueltas.head())

print(session.weather_data.head())

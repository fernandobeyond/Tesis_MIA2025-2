# DDoS Detection - Repository (simulated)

Estructura mínima del repositorio para el proyecto de detección DDoS.

- `data/` : raw, interim, processed (ej. ddos_balanceado.csv en processed)
- `notebooks/` : notebooks exploratorios
- `src/` : scripts para preprocess, dataset, models, train, utils
- `logs/` : logs de ejecución y métricas
- `models/`: artefactos guardados (xgb, cnnlstm, meta)

Este repositorio está pensado como plantilla para reproducir el pipeline descrito
en los papers: XGBoost (tabular) + CNN1D-LSTM (secuencias) + blending/meta-learner.

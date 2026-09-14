"""Treina e serializa um modelo simples de previsão de churn para o lab.

Gera dados sintéticos apenas para fins didáticos — em um cenário real,
substitua por um dataset de verdade.
"""
import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib

np.random.seed(42)
n = 2000

idade = np.random.randint(18, 90, n)
meses = np.random.randint(0, 72, n)
valor_mensal = np.random.uniform(20, 200, n)

# regra sintética: clientes novos e com mensalidade alta têm mais chance de churn
prob_churn = 1 / (1 + np.exp(-(0.03 * (40 - idade) + 0.05 * (12 - meses) + 0.01 * (valor_mensal - 80))))
churn = (np.random.rand(n) < prob_churn).astype(int)

df = pd.DataFrame({
    "idade": idade,
    "meses": meses,
    "valor_mensal": valor_mensal,
})

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", RandomForestClassifier(n_estimators=150, random_state=42)),
])

pipeline.fit(df, churn)

joblib.dump(pipeline, "modelo_churn.joblib")
print("Modelo salvo em modelo_churn.joblib")

#!/bin/bash
# Edite BUCKET_NAME e REGION antes de rodar. Execute a partir da raiz do
# repositório do seu projeto (onde está a pasta .git).
set -e

BUCKET_NAME="meu-bucket-dvcstore"
REGION="us-east-1"

echo "1) Criando o bucket S3 (ignora erro se já existir)..."
aws s3 mb "s3://$BUCKET_NAME" --region "$REGION" || true

echo "2) Inicializando o DVC..."
dvc init -f

echo "3) Configurando o S3 como remote padrão..."
dvc remote add -d -f storage "s3://$BUCKET_NAME/dvcstore"
git add .dvc/config
git commit -m "Configura o S3 como remote do DVC" || true

echo "4) Versionando o dataset (ajuste o caminho conforme seu projeto)..."
if [ -f "dados/dataset.csv" ]; then
  dvc add dados/dataset.csv
  git add dados/dataset.csv.dvc dados/.gitignore
  git commit -m "Versiona dataset.csv com o DVC" || true

  echo "5) Enviando os dados para o S3..."
  dvc push
else
  echo "Aviso: dados/dataset.csv não encontrado — pulei as etapas 4 e 5."
  echo "Ajuste o caminho no script e rode 'dvc add' + 'dvc push' manualmente."
fi

echo "Pronto. Em outra máquina, 'git clone' + 'dvc pull' recupera os dados exatos."

#!/bin/bash
# Edite as três variáveis abaixo antes de rodar.
set -e

AWS_REGION="us-east-1"
ECR_URI="123456789012.dkr.ecr.us-east-1.amazonaws.com/minha-app-ml"
IMAGE_TAG="latest"

echo "1) Autenticando o Docker no ECR..."
aws ecr get-login-password --region "$AWS_REGION" \
  | docker login --username AWS --password-stdin "$(echo "$ECR_URI" | cut -d'/' -f1)"

echo "2) Buildando a imagem..."
docker build -t minha-app-ml .

echo "3) Criando a tag para o ECR..."
docker tag minha-app-ml:latest "$ECR_URI:$IMAGE_TAG"

echo "4) Enviando (push) para o ECR..."
docker push "$ECR_URI:$IMAGE_TAG"

echo "Pronto! Imagem publicada em $ECR_URI:$IMAGE_TAG"
echo "Agora crie (ou atualize) o serviço no AWS App Runner apontando para essa imagem."

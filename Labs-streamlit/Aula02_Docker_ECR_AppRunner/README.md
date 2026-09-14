# Lab AWS — Publicando a imagem no Amazon ECR e rodando no AWS App Runner

Complementa a Parte 03 (boas práticas e orquestração): em vez de publicar a
imagem no Docker Hub, vamos publicá-la em um registry privado na AWS e rodá-la
como um serviço gerenciado.

## Arquivos deste lab
- `Dockerfile` — mesma estrutura vista na Parte 02 da aula
- `app.py` / `requirements.txt` — aplicação de exemplo a ser containerizada
- `build_push.sh` — script com todos os comandos de build + push para o ECR
- `apprunner.yaml` — configuração do serviço no AWS App Runner

## Pré-requisitos
- AWS CLI instalada e configurada (`aws configure`)
- Docker instalado localmente
- Uma conta AWS com permissão para ECR e App Runner

## Passo a passo

### 1. Crie um repositório no Amazon ECR
```bash
aws ecr create-repository --repository-name minha-app-ml --region us-east-1
```
Guarde a URI retornada, algo como:
`123456789012.dkr.ecr.us-east-1.amazonaws.com/minha-app-ml`

### 2. Autentique o Docker no ECR
```bash
aws ecr get-login-password --region us-east-1 \
  | docker login --username AWS --password-stdin 123456789012.dkr.ecr.us-east-1.amazonaws.com
```

### 3. Build, tag e push da imagem
Use o script `build_push.sh` (edite a variável `ECR_URI` no topo do arquivo
com a URI do seu repositório) ou rode manualmente:
```bash
docker build -t minha-app-ml .
docker tag minha-app-ml:latest 123456789012.dkr.ecr.us-east-1.amazonaws.com/minha-app-ml:latest
docker push 123456789012.dkr.ecr.us-east-1.amazonaws.com/minha-app-ml:latest
```

### 4. Crie o serviço no AWS App Runner
Pelo Console (mais simples para a primeira vez):
- AWS App Runner → Create service
- Repository type: **Container registry** → **Amazon ECR**
- Selecione a imagem que você acabou de enviar
- Porta: `8501` (a mesma exposta no Dockerfile)
- Deployment trigger: manual ou automático a cada push na imagem

Ou via CLI, usando `apprunner.yaml` como referência de configuração do runtime.

### 5. Acesse a URL pública
O App Runner expõe uma URL do tipo:
```
https://xxxxxxxxx.us-east-1.awsapprunner.com
```

## Referência
AWS Documentation — Amazon ECR e AWS App Runner:
https://docs.aws.amazon.com/AmazonECR/ · https://docs.aws.amazon.com/apprunner/

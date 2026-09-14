# Lab AWS — Usando o Amazon S3 como remote do DVC

Complementa a Parte 03 (DVC para dados e pipelines): o Git guarda só o
ponteiro `.dvc` — os dados de verdade precisam de um armazenamento remoto.
Neste lab, esse remote é um bucket do Amazon S3.

## Arquivos deste lab
- `setup_dvc_s3.sh` — todos os comandos, na ordem, prontos para rodar
- `dvc.yaml` — exemplo de pipeline reprodutível (preparar → treinar), como
  visto na Parte 03
- `requirements.txt`

## Pré-requisitos
- Git e DVC instalados (`pip install "dvc[s3]"`)
- AWS CLI configurada (`aws configure`) com permissão de leitura/escrita no bucket
- Um repositório Git já iniciado no projeto

## Passo a passo

### 1. Crie um bucket S3 dedicado a dados versionados
```bash
aws s3 mb s3://meu-bucket-dvcstore --region us-east-1
```

### 2. Inicialize o DVC no projeto (junto com o Git)
```bash
git init            # se ainda não existir
dvc init
git commit -m "Inicializa o DVC"
```

### 3. Configure o S3 como remote
```bash
dvc remote add -d storage s3://meu-bucket-dvcstore/dvcstore
git add .dvc/config
git commit -m "Configura o S3 como remote do DVC"
```

### 4. Versione um dataset
```bash
dvc add dados/dataset.csv
git add dados/dataset.csv.dvc dados/.gitignore
git commit -m "Versiona dataset.csv com o DVC"
```

### 5. Envie os dados reais para o S3
```bash
dvc push
```
O Git guarda só o ponteiro (`dataset.csv.dvc`); o arquivo em si agora vive no
bucket.

### 6. Reproduza em outra máquina (ou depois de um `git clone`)
```bash
git clone <repo>
cd <repo>
dvc pull        # baixa a versão exata dos dados apontada pelo commit
dvc repro       # reexecuta o pipeline (ver dvc.yaml) apenas onde algo mudou
```

## O fluxo completo da aula, nesta ordem
```
git checkout <commit-de-3-meses-atrás>
dvc pull
dvc repro
```
Reproduz exatamente o código (Git), os dados (DVC + S3) e, combinado ao
MLflow, também os parâmetros e métricas daquele experimento.

## Referência
DVC Documentation — Amazon S3 remote: https://dvc.org/doc/user-guide/data-management/remote-storage/amazon-s3

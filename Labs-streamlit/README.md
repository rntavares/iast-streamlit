# Labs AWS — Deploy e Monitoramento de Modelos de Machine Learning

Arquivos de apoio para os laboratórios práticos na AWS de cada aula
(referenciados na Parte 03 de cada apresentação).

| Pasta | Aula | Lab |
|---|---|---|
| `Aula01_Streamlit_EC2/` | Pipeline de ML e Deploy no Streamlit | Deploy do app Streamlit em uma instância Amazon EC2 |
| `Aula02_Docker_ECR_AppRunner/` | Containerização com Docker | Publicar a imagem no Amazon ECR e rodar no AWS App Runner |
| `Aula03_Drift_SageMakerModelMonitor/` | Monitoramento de Drift | Configurar o Amazon SageMaker Model Monitor |
| `Aula04_MLflow_DVC_S3/` | Versionamento com MLflow e DVC | Usar o Amazon S3 como remote do DVC |

Cada pasta tem seu próprio `README.md` com o passo a passo completo, mais os
scripts/arquivos de código necessários (Dockerfile, requirements.txt, scripts
Python/bash, etc.).

**Nota:** os comandos e nomes de recursos (buckets, roles, regiões) usam
placeholders (`meu-bucket`, `123456789012`, `us-east-1`). Ajuste-os para a sua
conta AWS antes de rodar.

# Lab AWS — Monitorando drift com o Amazon SageMaker Model Monitor

Complementa a Parte 03 (reagindo ao drift): em vez do Evidently rodando no seu
notebook, vamos configurar a AWS para capturar o tráfego de um endpoint em
produção e comparar automaticamente contra a distribuição de referência do
treino — o mesmo PSI / Kolmogorov-Smirnov da aula, agora gerenciado pela AWS.

## Arquivos deste lab
- `enable_data_capture.py` — habilita a captura de dados no endpoint
- `baseline_job.py` — gera a baseline estatística a partir dos dados de treino
- `create_monitoring_schedule.py` — cria o agendamento de monitoramento
- `requirements.txt`

## Pré-requisitos
- Um endpoint do SageMaker já em produção (ou o exemplo mínimo comentado nos
  scripts, caso queira testar do zero)
- Um bucket S3 para guardar os dados capturados e a baseline
- Permissões de execução (role) do SageMaker configuradas

## Passo a passo

### 1. Habilite Data Capture no endpoint
Rode `enable_data_capture.py` — ele reconfigura o endpoint para gravar uma
amostra (ou 100%) das requisições e respostas no S3.
```bash
python enable_data_capture.py
```

### 2. Gere a baseline estatística
A partir do dataset de treino (o mesmo usado para treinar o modelo), o
SageMaker calcula estatísticas de referência (médias, distribuições, tipos de
dados) que servirão de comparação.
```bash
python baseline_job.py
```

### 3. Crie o Monitoring Schedule
Define a frequência com que a AWS compara produção vs baseline (por exemplo,
a cada hora).
```bash
python create_monitoring_schedule.py
```

### 4. Acompanhe os resultados
- Violações de drift aparecem no S3 (relatórios) e podem ser vistas no
  Amazon SageMaker Studio, na aba "Model Monitor" do endpoint.
- Configure um alarme no **Amazon CloudWatch** sobre a métrica
  `feature_baseline_drift_*` para ser notificado automaticamente.

## Referência
AWS Documentation — Amazon SageMaker Model Monitor:
https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html

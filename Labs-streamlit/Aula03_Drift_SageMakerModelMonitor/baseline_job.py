"""Gera a baseline estatística a partir dos dados de treino.

Essa é a "janela de referência" da aula: o SageMaker calcula estatísticas
(distribuições, tipos, valores ausentes) sobre o dataset de treino, que
servirão de comparação para os dados de produção capturados pelo Data Capture.

Ajuste as constantes abaixo antes de rodar.
"""
import boto3
from sagemaker.model_monitor import DefaultModelMonitor
from sagemaker.model_monitor.dataset_format import DatasetFormat
from sagemaker.session import Session

ROLE_ARN = "arn:aws:iam::123456789012:role/SageMakerExecutionRole"
TRAINING_DATA_S3 = "s3://meu-bucket/dados/treino.csv"
BASELINE_OUTPUT_S3 = "s3://meu-bucket/monitoramento/baseline"

session = Session(boto_session=boto3.Session())

monitor = DefaultModelMonitor(
    role=ROLE_ARN,
    instance_count=1,
    instance_type="ml.m5.xlarge",
    volume_size_in_gb=20,
    max_runtime_in_seconds=1800,
    sagemaker_session=session,
)

monitor.suggest_baseline(
    baseline_dataset=TRAINING_DATA_S3,
    dataset_format=DatasetFormat.csv(header=True),
    output_s3_uri=BASELINE_OUTPUT_S3,
)

print("Job de baseline enviado. Isso equivale à 'janela de referência' vista na aula.")
print(f"Estatísticas e schema serão salvos em: {BASELINE_OUTPUT_S3}")

"""Habilita Data Capture em um endpoint existente do SageMaker.

Data Capture grava uma amostra (ou 100%) das requisições e respostas do
endpoint no S3 — é a partir desses dados que o Model Monitor compara a
distribuição de produção contra a baseline de treino.

Ajuste as constantes abaixo antes de rodar.
"""
import boto3
from sagemaker.model_monitor import DataCaptureConfig
from sagemaker.predictor import Predictor
from sagemaker.session import Session

ENDPOINT_NAME = "meu-endpoint-em-producao"
S3_CAPTURE_PATH = "s3://meu-bucket/monitoramento/data-capture"
SAMPLING_PERCENTAGE = 100  # 100% em desenvolvimento; reduza em alto volume de produção

session = Session(boto_session=boto3.Session())

data_capture_config = DataCaptureConfig(
    enable_capture=True,
    sampling_percentage=SAMPLING_PERCENTAGE,
    destination_s3_uri=S3_CAPTURE_PATH,
)

predictor = Predictor(endpoint_name=ENDPOINT_NAME, sagemaker_session=session)
predictor.update_data_capture_config(data_capture_config=data_capture_config)

print(f"Data Capture habilitado no endpoint '{ENDPOINT_NAME}'.")
print(f"As requisições/respostas serão gravadas em: {S3_CAPTURE_PATH}")

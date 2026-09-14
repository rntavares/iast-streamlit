"""Cria o Monitoring Schedule — o agendamento que compara produção vs baseline.

Equivalente ao "gatilho de re-treino por agendamento" da aula, mas aqui
agendando a checagem de drift em si (não o re-treino). Rode depois de
enable_data_capture.py e baseline_job.py.

Ajuste as constantes abaixo antes de rodar.
"""
import boto3
from sagemaker.model_monitor import CronExpressionGenerator, DefaultModelMonitor
from sagemaker.session import Session

ROLE_ARN = "arn:aws:iam::123456789012:role/SageMakerExecutionRole"
ENDPOINT_NAME = "meu-endpoint-em-producao"
BASELINE_STATISTICS_S3 = "s3://meu-bucket/monitoramento/baseline/statistics.json"
BASELINE_CONSTRAINTS_S3 = "s3://meu-bucket/monitoramento/baseline/constraints.json"
REPORTS_OUTPUT_S3 = "s3://meu-bucket/monitoramento/reports"

session = Session(boto_session=boto3.Session())

monitor = DefaultModelMonitor(
    role=ROLE_ARN,
    instance_count=1,
    instance_type="ml.m5.xlarge",
    volume_size_in_gb=20,
    max_runtime_in_seconds=1800,
    sagemaker_session=session,
)

monitor.create_monitoring_schedule(
    monitor_schedule_name=f"{ENDPOINT_NAME}-drift-schedule",
    endpoint_input=ENDPOINT_NAME,
    output_s3_uri=REPORTS_OUTPUT_S3,
    statistics=BASELINE_STATISTICS_S3,
    constraints=BASELINE_CONSTRAINTS_S3,
    schedule_cron_expression=CronExpressionGenerator.hourly(),
)

print("Monitoring Schedule criado — checagem de drift a cada hora.")
print(f"Relatórios de violação serão salvos em: {REPORTS_OUTPUT_S3}")
print("Configure um alarme no CloudWatch sobre as métricas 'feature_baseline_drift_*'.")

# 🚀 FIAP — Pós-Graduação IAST: Fazendo o seu primeiro deploy com Streamlit
### Pipelines de Machine Learning, Containerização com Docker, Monitoramento de Drift e Versionamento na AWS

[![GitLab](https://img.shields.io/badge/GitLab-Repository-fc6d26?logo=gitlab&logoColor=white)](https://gitlab.com/rntavares/fiap-iast-streamlit)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Docker](https://img.shields.io/badge/Container-Docker-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![AWS](https://img.shields.io/badge/Cloud-AWS-232F3E?logo=amazon-aws&logoColor=white)](https://aws.amazon.com/)
[![MLflow](https://img.shields.io/badge/Tracking-MLflow-0194E2?logo=mlflow&logoColor=white)](https://mlflow.org/)
[![DVC](https://img.shields.io/badge/Data_Version-DVC-945DD6?logo=dvc&logoColor=white)](https://dvc.org/)

Repositório oficial de materiais, apresentações, documentação técnica e laboratórios práticos da disciplina **"Fazendo o seu primeiro deploy com Streamlit"** do curso de **Pós-Graduação em Inteligência Artificial para Soluções Tecnológicas (IAST)** da **FIAP**.

🔗 **Repositório GitLab:** [https://gitlab.com/rntavares/fiap-iast-streamlit](https://gitlab.com/rntavares/fiap-iast-streamlit)

---

## 🎯 Visão Geral da Disciplina

Esta disciplina guia os alunos por toda a jornada de transformação de um modelo de Machine Learning em uma aplicação web interativa e profissional utilizando **Streamlit**, avançando pelas etapas de **conteinerização com Docker**, **deploy escalável na AWS**, **monitoramento contínuo de Drift** e **versionamento de ponta a ponta com MLflow e DVC**.

```
 ┌─────────────┐     ┌──────────────┐     ┌─────────────┐     ┌─────────────┐
 │   AULA 01   │ ──▶ │   AULA 02    │ ──▶ │   AULA 03   │ ──▶ │   AULA 04   │
 │Pipeline ML  │     │Container com │     │Monitoramento│     │Versionamento│
 │& Streamlit  │     │Docker & ECR  │     │  de Drift   │     │MLflow & DVC │
 └─────────────┘     └──────────────┘     └─────────────┘     └─────────────┘
```

---

## 💻 Primeiros Passos & Clonando o Repositório

### Clonar via HTTPS:
```bash
git clone https://gitlab.com/rntavares/fiap-iast-streamlit.git
cd fiap-iast-streamlit
```

### Clonar via SSH:
```bash
git clone git@gitlab.com:rntavares/fiap-iast-streamlit.git
cd fiap-iast-streamlit
```

### Vincular este diretório a um novo repositório Git:
```bash
git init
git remote add origin https://gitlab.com/rntavares/fiap-iast-streamlit.git
git branch -M main
git add .
git commit -m "feat: initial commit - material completo do curso"
git push -u origin main
```

---

## 📂 Estrutura do Repositório

```text
fiap-iast-streamlit/
├── 📚 Docs-Aulas-streamlit/        # Apostilas e documentação teórica
│   ├── capitulos/                  # Capítulos detalhados em .docx (Aulas 01 a 04)
│   ├── desafio/                    # Especificação do Desafio Final Integrado
│   └── roteiros/                   # Roteiro pedagógico da disciplina
│
├── 🛠️ Labs-streamlit/              # Laboratórios práticos passo a passo
│   ├── Aula01_Streamlit_EC2/       # Lab 01: Deploy do app Streamlit no Amazon EC2
│   ├── Aula02_Docker_ECR_AppRunner/# Lab 02: Containerização, Amazon ECR & AWS App Runner
│   ├── Aula03_Drift_SageMaker.../  # Lab 03: Monitoramento com SageMaker Model Monitor
│   └── Aula04_MLflow_DVC_S3/       # Lab 04: Versionamento de dados com DVC e Amazon S3
│
└── 📊 PPTs-Aulas-streamlit/        # Slides e apresentações (PowerPoint)
    ├── Aula01_Pipeline_ML_Streamlit.pptx
    ├── Aula02_Containerizacao_Docker.pptx
    ├── Aula03_Monitoramento_Drift.pptx
    └── Aula04_Versionamento_MLflow_DVC.pptx
```

---

## 📖 Trilha de Aprendizagem & Conteúdo das Aulas

### 🔹 Aula 01 — Pipeline de ML e Deploy no Streamlit
* **Teoria:** Criação de interfaces de Machine Learning reativas e intuitivas com Streamlit, arquitetura de componentes, sessões e fluxo de dados.
* **Lab Prático (`Labs-streamlit/Aula01_Streamlit_EC2`):**
  * Provisionamento e configuração de instância Amazon EC2.
  * Configuração de Security Groups, ambiente Python e execução do app Streamlit como serviço.

### 🔹 Aula 02 — Containerização com Docker & Deploy Serverless na AWS
* **Teoria:** Fundamentos de Docker para Data Science, escrita de `Dockerfile` otimizado, boas práticas de camadas (*multi-stage*) e isolamento de dependências.
* **Lab Prático (`Labs-streamlit/Aula02_Docker_ECR_AppRunner`):**
  * Build da imagem Docker da aplicação Streamlit.
  * Publicação da imagem no Amazon ECR (Elastic Container Registry).
  * Deploy escalável e automatizado via AWS App Runner.

### 🔹 Aula 03 — Monitoramento de Modelos em Produção & Data Drift
* **Teoria:** Ciclo pós-deploy, identificação de *Data Drift* e *Concept Drift*, degradação de acurácia e estratégias de re-treinamento.
* **Lab Prático (`Labs-streamlit/Aula03_Drift_SageMakerModelMonitor`):**
  * Configuração de baseline de dados e métricas estatísticas de qualidade.
  * Execução e agendamento de análises com Amazon SageMaker Model Monitor.

### 🔹 Aula 04 — Versionamento de Dados e Modelos com MLflow, DVC e S3
* **Teoria:** Governança completa de dados (*Data Lineage*), rastreabilidade de experimentos e versionamento de grandes volumes de dados sem sobrecarregar o Git.
* **Lab Prático (`Labs-streamlit/Aula04_MLflow_DVC_S3`):**
  * Configuração do DVC (Data Version Control) com storage remoto no Amazon S3.
  * Registro de experimentos e métricas com MLflow Tracking integrado.

---

## 🛠️ Pré-requisitos & Ambiente

Para executar os laboratórios práticos, você precisará:

1. **Conta AWS:** Acesso aos serviços utilizados (EC2, ECR, App Runner, SageMaker, S3).
2. **AWS CLI:** Instalado e configurado (`aws configure`).
3. **Python:** Versão 3.10 ou superior.
4. **Docker:** Docker Desktop ou Docker Engine para build e push das imagens.
5. **Git & DVC:** Para controle de versão de código e dados.

---

## ⚠️ Cuidados com Custos na AWS

> **ATENÇÃO:** Lembre-se de encerrar as instâncias EC2, serviços do App Runner e endpoints do SageMaker após a conclusão de cada laboratório para evitar cobranças indesejadas no Free Tier / Faturamento da AWS.

---

## 🏆 Desafio Final Integrado

O diretório `Docs-Aulas-streamlit/desafio/` traz a especificação do **Desafio Final Integrado**, onde os alunos desenvolvem e publicam uma aplicação completa em Streamlit conteinerizada na nuvem com versionamento e monitoramento.

---

## 👨‍🏫 Autor & Coordenação

* **Professor / Autor:** Rafael Tavares ([@rntavares](https://gitlab.com/rntavares))
* **Curso:** Pós-Graduação em Inteligência Artificial para Soluções Tecnológicas (IAST)
* **Instituição:** [FIAP](https://www.fiap.com.br)

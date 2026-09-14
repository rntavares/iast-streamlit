# Lab AWS — Deploy do Streamlit em uma instância EC2

Complementa o deploy no Streamlit Community Cloud (Parte 03): agora publicamos
o mesmo `app.py` em uma instância própria na AWS.

## Arquivos deste lab
- `train_model.py` — treina e serializa o modelo de exemplo (`modelo_churn.joblib`)
- `app.py` — aplicação Streamlit de predição (a mesma da Parte 02/03 da aula)
- `requirements.txt` — dependências
- `user_data.sh` — script opcional de inicialização da EC2 (instala tudo sozinho no boot)

## Passo a passo

### 1. Crie a instância EC2
- AMI: Ubuntu Server 22.04 LTS
- Tipo: `t2.micro` (elegível ao Free Tier)
- Crie ou selecione um par de chaves (`.pem`) para acesso SSH

### 2. Libere a porta no Security Group
Adicione uma regra de entrada (inbound):
- Tipo: Custom TCP
- Porta: `8501`
- Origem: `0.0.0.0/0` (ou seu IP, para testes)

### 3. Conecte via SSH e instale as dependências
```bash
ssh -i sua-chave.pem ubuntu@<IP_PUBLICO_DA_INSTANCIA>

sudo apt update && sudo apt install -y python3-pip python3-venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4. Suba os arquivos do projeto
Do seu computador local:
```bash
scp -i sua-chave.pem app.py train_model.py requirements.txt ubuntu@<IP_PUBLICO_DA_INSTANCIA>:~/
```

### 5. Gere o modelo e rode a aplicação
Já conectado na instância:
```bash
python train_model.py                 # cria modelo_churn.joblib
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```

### 6. Acesse pelo IP público
```
http://<IP_PUBLICO_DA_INSTANCIA>:8501
```

## Deixando a aplicação rodando permanentemente (opcional)
Para não perder a aplicação ao fechar o SSH, rode com `nohup` ou configure um
serviço systemd:
```bash
nohup streamlit run app.py --server.port 8501 --server.address 0.0.0.0 &
```

## Automatizando com user_data.sh (opcional)
Ao criar a instância, cole o conteúdo de `user_data.sh` no campo "User data"
(seção "Advanced details"). A instância já sobe com tudo instalado e a
aplicação rodando, sem precisar de SSH manual.

## Referência
AWS Documentation — Amazon EC2 User Guide: https://docs.aws.amazon.com/ec2/

#!/bin/bash
# Cole este conteúdo no campo "User data" ao criar a instância EC2
# (EC2 > Launch instance > Advanced details > User data).
# A instância sobe já com o ambiente pronto e a app rodando.
#
# IMPORTANTE: este script não copia app.py/train_model.py sozinho — depois do
# boot, envie os arquivos do projeto via scp (ou clone de um repositório Git)
# para /home/ubuntu/ antes de rodar train_model.py.

set -e
apt update
apt install -y python3-pip python3-venv

su - ubuntu -c "
  python3 -m venv /home/ubuntu/venv
  source /home/ubuntu/venv/bin/activate
  pip install streamlit scikit-learn pandas joblib
"

echo "Ambiente pronto. Envie app.py, train_model.py e requirements.txt via scp,"
echo "rode 'python train_model.py' e depois 'streamlit run app.py --server.port 8501 --server.address 0.0.0.0'."

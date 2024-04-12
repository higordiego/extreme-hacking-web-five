import jwt
import json
from datetime import datetime, timedelta

# Seu JSON
json_data = {
    "username": "kaecee",
    "role": "admin",
    "exp": 1712679535
}

# Adiciona 5 minutos ao tempo de expiração atual
expiration_time = datetime.utcfromtimestamp(json_data['exp']) + timedelta(minutes=5)

# Atualiza o tempo de expiração no JSON
json_data['exp'] = int(expiration_time.timestamp())

# Chave secreta para assinatura do JWT (substitua pela sua chave real)
secret_key = "keondraluvsheryl"

# Cria o token JWT com o tempo de expiração atualizado
token = jwt.encode(json_data, secret_key, algorithm="HS256")

print("Token JWT gerado com 5 minutos adicionados ao tempo de expiração:")
print(token)
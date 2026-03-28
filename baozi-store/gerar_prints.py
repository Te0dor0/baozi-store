#!/usr/bin/env python3
import requests
import json
from datetime import datetime
import os

# Cores para terminal
VERDE = '\033[92m'
VERMELHO = '\033[91m'
AZUL = '\033[94m'
AMARELO = '\033[93m'
RESET = '\033[0m'
NEGRITO = '\033[1m'

BASE_URL = "http://localhost:8080/api"
OUTPUT_DIR = "/home/ubuntu/baozi-store/prints"

# Criar diretório de saída
os.makedirs(OUTPUT_DIR, exist_ok=True)

def print_request(metodo, endpoint, dados=None):
    print(f"\n{NEGRITO}{AZUL}{'='*70}{RESET}")
    print(f"{NEGRITO}{AZUL}REQUEST: {metodo} {endpoint}{RESET}")
    print(f"{NEGRITO}{AZUL}{'='*70}{RESET}")
    print(f"URL: {BASE_URL}{endpoint}")
    print(f"Método: {metodo}")
    if dados:
        print(f"Body:\n{json.dumps(dados, indent=2, ensure_ascii=False)}")

def print_response(response):
    print(f"\n{NEGRITO}{VERDE}{'='*70}{RESET}")
    print(f"{NEGRITO}{VERDE}RESPONSE{RESET}")
    print(f"{NEGRITO}{VERDE}{'='*70}{RESET}")
    print(f"Status Code: {response.status_code}")
    print(f"Headers: Content-Type: {response.headers.get('Content-Type', 'N/A')}")
    try:
        print(f"Body:\n{json.dumps(response.json(), indent=2, ensure_ascii=False)}")
    except:
        print(f"Body:\n{response.text}")

def salvar_print(titulo, conteudo, numero):
    filename = f"{OUTPUT_DIR}/{numero:02d}_{titulo.replace(' ', '_').lower()}.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(conteudo)
    print(f"\n{AMARELO}✓ Salvo: {filename}{RESET}")

# ==================== TESTES ====================

print(f"\n{NEGRITO}{AMARELO}{'='*70}{RESET}")
print(f"{NEGRITO}{AMARELO}TESTES DA API BAOZI STORE{RESET}")
print(f"{NEGRITO}{AMARELO}{'='*70}{RESET}")

# 1. POST - Criar Cliente
print(f"\n{NEGRITO}1. POST - CRIAR CLIENTE{RESET}")
cliente_data = {
    "nome": "DiegoSilva4751079",
    "clienteDesde": "2024-01-15"
}
print_request("POST", "/clientes", cliente_data)
response = requests.post(f"{BASE_URL}/clientes", json=cliente_data)
print_response(response)
cliente_id = response.json()['id']

# 2. POST - Criar Produto
print(f"\n{NEGRITO}2. POST - CRIAR PRODUTO{RESET}")
produto_data = {
    "nome": "Pão Chinês Tradicional",
    "preco": 15.50,
    "estoque": True
}
print_request("POST", "/produtos", produto_data)
response = requests.post(f"{BASE_URL}/produtos", json=produto_data)
print_response(response)
produto_id = response.json()['id']

# 3. POST - Criar Pedido
print(f"\n{NEGRITO}3. POST - CRIAR PEDIDO{RESET}")
pedido_data = {
    "clienteId": cliente_id,
    "produtoId": produto_id,
    "quantidade": 5
}
print_request("POST", "/pedidos", pedido_data)
response = requests.post(f"{BASE_URL}/pedidos", json=pedido_data)
print_response(response)
pedido_id = response.json()['id']

# 4. GET - Listar todos os Clientes
print(f"\n{NEGRITO}4. GET - LISTAR TODOS OS CLIENTES{RESET}")
print_request("GET", "/clientes")
response = requests.get(f"{BASE_URL}/clientes")
print_response(response)

# 5. GET - Consultar Cliente por ID
print(f"\n{NEGRITO}5. GET - CONSULTAR CLIENTE POR ID{RESET}")
print_request("GET", f"/clientes/{cliente_id}")
response = requests.get(f"{BASE_URL}/clientes/{cliente_id}")
print_response(response)

# 6. GET - Listar todos os Produtos
print(f"\n{NEGRITO}6. GET - LISTAR TODOS OS PRODUTOS{RESET}")
print_request("GET", "/produtos")
response = requests.get(f"{BASE_URL}/produtos")
print_response(response)

# 7. GET - Consultar Produto por ID
print(f"\n{NEGRITO}7. GET - CONSULTAR PRODUTO POR ID{RESET}")
print_request("GET", f"/produtos/{produto_id}")
response = requests.get(f"{BASE_URL}/produtos/{produto_id}")
print_response(response)

# 8. GET - Listar todos os Pedidos
print(f"\n{NEGRITO}8. GET - LISTAR TODOS OS PEDIDOS{RESET}")
print_request("GET", "/pedidos")
response = requests.get(f"{BASE_URL}/pedidos")
print_response(response)

# 9. GET - Consultar Pedido por ID
print(f"\n{NEGRITO}9. GET - CONSULTAR PEDIDO POR ID{RESET}")
print_request("GET", f"/pedidos/{pedido_id}")
response = requests.get(f"{BASE_URL}/pedidos/{pedido_id}")
print_response(response)

# 10. DELETE - Deletar Cliente
print(f"\n{NEGRITO}10. DELETE - DELETAR CLIENTE{RESET}")
print_request("DELETE", f"/clientes/{cliente_id}")
response = requests.delete(f"{BASE_URL}/clientes/{cliente_id}")
print(f"Status Code: {response.status_code}")

# 11. Verificar se cliente foi deletado
print(f"\n{NEGRITO}11. GET - VERIFICAR LISTAGEM APÓS DELETE{RESET}")
print_request("GET", "/clientes")
response = requests.get(f"{BASE_URL}/clientes")
print_response(response)

print(f"\n{NEGRITO}{AMARELO}{'='*70}{RESET}")
print(f"{NEGRITO}{AMARELO}TESTES CONCLUÍDOS COM SUCESSO!{RESET}")
print(f"{NEGRITO}{AMARELO}{'='*70}{RESET}\n")

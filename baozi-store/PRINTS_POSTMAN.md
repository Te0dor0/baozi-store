# Prints dos Testes Postman - API Baozi Store

## 1. POST - Criar Cliente

**Request:**
```
POST http://localhost:8080/api/clientes
Content-Type: application/json

{
  "nome": "DiegoSilva4751079",
  "clienteDesde": "2024-01-15"
}
```

**Response (Status 201):**
```json
{
  "id": 2,
  "nome": "DiegoSilva4751079",
  "clienteDesde": "2024-01-15"
}
```

---

## 2. POST - Criar Produto

**Request:**
```
POST http://localhost:8080/api/produtos
Content-Type: application/json

{
  "nome": "Pão Chinês Tradicional",
  "preco": 15.50,
  "estoque": true
}
```

**Response (Status 201):**
```json
{
  "id": 2,
  "nome": "Pão Chinês Tradicional",
  "preco": 15.5,
  "estoque": true
}
```

---

## 3. POST - Criar Pedido

**Request:**
```
POST http://localhost:8080/api/pedidos
Content-Type: application/json

{
  "clienteId": 2,
  "produtoId": 2,
  "quantidade": 5
}
```

**Response (Status 201):**
```json
{
  "id": 2,
  "clienteId": 2,
  "produtoId": 2,
  "quantidade": 5
}
```

---

## 4. GET - Listar Todos os Clientes

**Request:**
```
GET http://localhost:8080/api/clientes
```

**Response (Status 200):**
```json
[
  {
    "id": 2,
    "nome": "DiegoSilva4751079",
    "clienteDesde": "2024-01-15"
  }
]
```

---

## 5. GET - Consultar Cliente por ID

**Request:**
```
GET http://localhost:8080/api/clientes/2
```

**Response (Status 200):**
```json
{
  "id": 2,
  "nome": "DiegoSilva4751079",
  "clienteDesde": "2024-01-15"
}
```

---

## 6. GET - Listar Todos os Produtos

**Request:**
```
GET http://localhost:8080/api/produtos
```

**Response (Status 200):**
```json
[
  {
    "id": 2,
    "nome": "Pão Chinês Tradicional",
    "preco": 15.5,
    "estoque": true
  }
]
```

---

## 7. GET - Consultar Produto por ID

**Request:**
```
GET http://localhost:8080/api/produtos/2
```

**Response (Status 200):**
```json
{
  "id": 2,
  "nome": "Pão Chinês Tradicional",
  "preco": 15.5,
  "estoque": true
}
```

---

## 8. GET - Listar Todos os Pedidos

**Request:**
```
GET http://localhost:8080/api/pedidos
```

**Response (Status 200):**
```json
[
  {
    "id": 2,
    "clienteId": 2,
    "produtoId": 2,
    "quantidade": 5
  }
]
```

---

## 9. GET - Consultar Pedido por ID

**Request:**
```
GET http://localhost:8080/api/pedidos/2
```

**Response (Status 200):**
```json
{
  "id": 2,
  "clienteId": 2,
  "produtoId": 2,
  "quantidade": 5
}
```

---

## 10. DELETE - Deletar Cliente

**Request:**
```
DELETE http://localhost:8080/api/clientes/2
```

**Response (Status 204):**
```
No Content
```

---

## 11. GET - Verificar Listagem Após Delete

**Request:**
```
GET http://localhost:8080/api/clientes
```

**Response (Status 200):**
```json
[]
```

---

## Resumo dos Testes

✓ **POST Clientes** - Criação bem-sucedida
✓ **POST Produtos** - Criação bem-sucedida
✓ **POST Pedidos** - Criação bem-sucedida
✓ **GET Clientes (todos)** - Listagem bem-sucedida
✓ **GET Clientes (por ID)** - Consulta bem-sucedida
✓ **GET Produtos (todos)** - Listagem bem-sucedida
✓ **GET Produtos (por ID)** - Consulta bem-sucedida
✓ **GET Pedidos (todos)** - Listagem bem-sucedida
✓ **GET Pedidos (por ID)** - Consulta bem-sucedida
✓ **DELETE Clientes** - Exclusão bem-sucedida
✓ **Verificação após DELETE** - Confirmado

Todos os endpoints CRUD foram testados e validados com sucesso!

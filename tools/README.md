# Tools: Módulo

Este módulo contém duas funcionalidades principais:

1. **Formatação de entrada do usuário com validação usando Pydantic**
2. **Extração de informações da web usando a API Tavily**

---

## 🚀 Funcionalidades

### 📥 `user_input_function`

Valida e formata um dicionário contendo informações do usuário.

- **Entrada:** dicionário com os campos:
  - `URL` (str): URL informada pelo usuário
  - `Problem` (str): Descrição do problema principal
  - `Details` (str): Detalhes adicionais fornecidos
- **Saída:** string formatada com os dados.

**Exemplo:**
```python
user_input = {
    "URL": "https://example.com",
    "Problem": "Erro de carregamento",
    "Details": "A página trava ao rolar para baixo"
}

print(user_input_function(user_input))
```

---

### 🌐 `WebSearch`

Classe para extrair conteúdo de uma URL utilizando a API [Tavily](https://www.tavily.com/).

- **Inicialização:**
```python
search = WebSearch("https://example.com")
```

- **Método:** `web_search()`
  - Faz uma requisição à API Tavily para extrair o conteúdo da URL fornecida.
  - Imprime o conteúdo extraído no terminal.
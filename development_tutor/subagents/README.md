# Agentes: Módulo

Este módulo define uma classe `Agents` que orquestra dois agentes de linguagem (LLMs) com funções distintas:

- Um agente para **ler e interpretar documentação** extraída da web
- Um agente para **resolver o problema do usuário** com base nas instruções fornecidas

---

## 📦 Estrutura do Módulo

```python
from google.adk.agents.llm_agent import Agent
from ..shared import constants, prompts
from ..tools.search_engine.web_search_tool import WebSearch
from ..tools.base_input.user_input import user_input_function
```

---

## ⚙️ Classe: `Agents`

### `__init__(self, user_url: str, user_input: dict)`
Inicializa a classe com:

- `user_url`: URL para extração de documentação técnica ou referência
- `user_input`: dicionário com os dados fornecidos pelo usuário

Internamente, ele:
- Processa a entrada com `user_input_function`
- Cria uma instância da ferramenta `WebSearch`

---

### 🧠 Método: `bring_solution()`

Cria um **agente solucionador** que:

- Usa o modelo definido em `constants.BASE_MODEL`
- Recebe instruções do prompt `prompts.RESUME_USER_INPUT`
- Utiliza a entrada formatada do usuário como ferramenta para resolução

**Retorno:** objeto `Agent` pronto para uso.

---

### 📖 Método: `read_docs()`

Cria um **agente leitor** que:

- Utiliza o mesmo modelo base
- Tem como objetivo entender a documentação obtida da web
- Usa a saída do `WebSearch.web_search()` como ferramenta principal
- Recebe instruções do prompt `prompts.READ_DESTROY_CONQUER_DONE`

**Retorno:** objeto `Agent` focado em leitura e entendimento da documentação.
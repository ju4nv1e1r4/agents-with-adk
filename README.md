
# Development Tutor Agent

O **Development Tutor Agent** é um assistente virtual baseado em inteligência artificial, projetado para ajudar desenvolvedores na solução de problemas técnicos e fornecer assistência sobre temas de programação. O agente é composto por subagentes especializados, como o **Researcher**, que realiza buscas na web para garantir que as informações fornecidas estão sempre atualizadas. Este projeto foi desenvolvido com Google ADK (Agent Development Kit)

##  O que é ADK?

O Agent Development Kit (ADK) é uma estrutura flexível e modular para o desenvolvimento e a implantação de agentes de IA. O ADK pode ser usado com LLMs populares e ferramentas de IA generativa de código aberto e foi projetado com foco na integração com o ecossistema do Google e os modelos Gemini. O ADK facilita o início do uso de agentes simples, impulsionados pelos modelos Gemini e pelas ferramentas de IA do Google, ao mesmo tempo que fornece o controle e a estrutura necessários para arquiteturas e orquestrações de agentes mais complexas.

## Funcionalidades

- **Researcher**: Realiza pesquisas em tempo real na web sobre temas relacionados ao desenvolvimento e programação, garantindo que as respostas sejam sempre baseadas nas informações mais recentes.
- **Development Tutor**: Instrui o usuário, guiando-o em uma jornada de aprendizado técnico com foco em linguagens de programação, frameworks e ferramentas.

## Arquitetura

O projeto é composto por um conjunto de agentes que colaboram entre si para fornecer respostas completas e detalhadas. O fluxo de trabalho do agente principal inclui:

1. **Greetings**: O agente se apresenta ao usuário de forma jocosa e coleta informações sobre a solicitação.
2. **Search**: O agente realiza uma busca em tempo real, utilizando o subagente **Researcher**, para garantir que as informações fornecidas estão atualizadas.
3. **Tone**: Ajuste do tom de resposta para um estilo técnico, amigável e jovial.
4. **Key Constraints**: Respostas direcionadas para solucionar problemas de forma prática e eficiente.

## Como Rodar

### Pré-requisitos

- Python 3.8 ou superior
- Dependências listadas no arquivo `requirements.txt`

### Passos para execução

1. Clone o repositório:

   ```bash
   git clone git@github.com:ju4nv1e1r4/agents-with-adk.git
   ```

2. Crie um ambiente virtual e ative-o:

   ```bash
   python3 -m venv env
   source env/bin/activate  # Linux/macOS
   env\Scripts\activate     # Windows
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente no arquivo `.env`:

   ```bash
      # If using Gemini via Google AI Studio
    GOOGLE_GENAI_USE_VERTEXAI="False"
    GOOGLE_API_KEY="paste-your-actual-key-here"
    
    # # If using Gemini via Vertex AI on Google CLoud
    # GOOGLE_CLOUD_PROJECT="your-project-id"
    # GOOGLE_CLOUD_LOCATION="your-location" #e.g. us-central1
    # GOOGLE_GENAI_USE_VERTEXAI="True"
   
   ```

   > Caso esteja utilizando o Google Cloud, descomente e configure as variáveis apropriadas para o Vertex AI.

5. Para rodar o agente no terminal, use o seguinte comando:

   ```bash
   adk run development_tutor/
   ```

6. Para rodar a interface web localmente:

   ```bash
   adk web
   ```

   Acesse a aplicação em [http://localhost:8000](http://localhost:8000).

## Como Funciona

1. O **Development Tutor** começa uma conversa com o usuário, perguntando como pode ajudar.
2. O subagente **Researcher** realiza uma pesquisa na web para garantir que as respostas estejam sempre atualizadas.
3. O **Development Tutor** fornece respostas com exemplos e explicações detalhadas.
4. O agente ajusta seu tom para ser técnico, amigável e jovial, garantindo uma experiência de aprendizado leve e informativa.

Seguem alguns prints do funcionamento no diretório img/.

## Estrutura do Projeto

```
.
├── development_tutor/
│   ├── agent.py              # main agent
│   ├── prompt.py             # Prompt base for main agent
│   ├── shared_libraries/     # Constants
│   ├── sub_agents/           # SubAgents
│   │   └── researcher/       # Researcher Agent
│   │       ├── agent.py
│   │       ├── prompt.py
│   └── tools/                # Tools
│       └── search.py         # Google Search Tool
└── README.md
```

## Próximos Passos

- **Deploy no Google Cloud**: O próximo passo é levar esse projeto para a nuvem, utilizando o Google Cloud para hospedar o agente e garantir que ele possa ser acessado globalmente.
  
---

Este projeto foi desenvolvido com foco em ajudar desenvolvedores de todas as áreas a encontrar soluções rápidas e precisas para seus problemas de programação.

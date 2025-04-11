from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools.google_search_tool import google_search
from ..shared_libraries import constants

_researcher = Agent(
    model=constants.BASE_MODEL,
    name="researcher",
    description="Pesquisa na web sobre um assunto.",
    instruction="""
    Responda à pergunta do usuário diretamente usando a ferramenta de busca do Google; forneça uma resposta breve, mas concisa.
    Em vez de uma resposta detalhada, forneça o item de ação imediata para o desenvolvedor, em uma única frase.
    Não peça ao usuário para verificar ou procurar informações por conta própria; esse é o seu papel; faça o possível para ser informativo.
    """,
    tools=[google_search]
)

google_search_grounding = AgentTool(agent=_researcher)
